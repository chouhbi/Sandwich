# Sandwich 
A simple static site generator that sandwiches HTML files with a common header and footer.

# Why ?
- You need to quickly wrap some html files with a common header and footer without the overhead of a full static site generator. 

- You don't want to learn *yet another templating language* just to make 3 pages with the same header and footer.


# Usage

1. Add `sandwich.py` to your root directory.

`curl -o sandwich.py https://raw.githubusercontent.com/chouhbi/sandwich/main/sandwich.py`

2. Place your `top.html` and `bottom.html` templates in the root directory.
```
┌── sandwich.py
├── top.html
└── bottom.html
```

3. Place your HTML files in the `pages/` directory.
```
┌── sandwich.py
├── top.html
├── bottom.html
└── pages
    ├── page1.html
    ├── page2.html
    └── page3.html
```
4. Place any assets (CSS, JS, images) in the `public/` directory.
```
┌── sandwich.py
├── top.html
├── bottom.html
├── pages
│   ├── page1.html
│   ├── page2.html
│   └── page3.html
└── public
    ├── styles.css
    └── script.js
```
5. Run `sandwich.py` to generate the sandwiched HTML files in the `build/` directory.
```
┌── sandwich.py
├── top.html
├── bottom.html
├── pages
│   ├── page1.html
│   ├── page2.html
│   └── page3.html
├── public
│   ├── styles.css
│   └── script.js
└── build
    ├── page1.html
    ├── page2.html
    ├── page3.html
    ├── styles.css
    └── script.js
```
