from os import listdir, path, makedirs
from shutil import copy2

PAGES_DIRECTORY = "pages"
PUBLIC_DIRECTORY = "public"
BUILD_DIRECTORY = "build"
TOP = "top.html"
BOTTOM = "bottom.html"

# Create output folder if it doesn't exist
if not path.exists(BUILD_DIRECTORY):
    makedirs(BUILD_DIRECTORY)

# Sandwich each .html file in PAGES_DIRECTORY with TOP and BOTTOM 
# and write to BUILD_DIRECTORY
for filename in listdir(PAGES_DIRECTORY):
    if filename.endswith(".html"):
        with open(path.join(PAGES_DIRECTORY, filename), "r", encoding="utf-8") as f:
            content = f.read()
        # Add top and bottom HTML
        with open(TOP, "r", encoding="utf-8") as f:
            top_content = f.read()
        with open(BOTTOM, "r", encoding="utf-8") as f:
            bottom_content = f.read()

        content = f"{top_content}\n{content}\n{bottom_content}"
        with open(path.join(BUILD_DIRECTORY, filename), "w", encoding="utf-8") as f:
            f.write(content)

# Copy files from PUBLIC_DIRECTORY into BUILD_DIRECTORY
for asset in listdir(PUBLIC_DIRECTORY):
    src_path = path.join(PUBLIC_DIRECTORY, asset)
    dest_path = path.join(BUILD_DIRECTORY, asset)
    copy2(src_path, dest_path)
