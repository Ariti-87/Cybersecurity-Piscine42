# Spider & Scorpion – Image Downloader & Metadata Analyzer

## 📝 Project Overview
This project consists of **two programs** for working with images from websites:

1. **Spider** – recursively downloads images from a given URL.
2. **Scorpion** – parses image files for EXIF and other metadata.

Both programs are written in **Python** and the logic is fully implemented manually.
> ❌ Using external tools like `wget` or `scrapy` is not allowed.

---

## 🕷️ Spider

The **Spider** program allows you to extract all images from a website, recursively.
It supports the following file extensions by default:

- `.jpg` / `.jpeg`
- `.png`
- `.gif`
- `.bmp`

### Usage
```sh
./spider.py [-r] [-l N] [-p PATH] URL
```

### Options
- `-r` : download images recursively  
- `-l [N]` : maximum recursion depth (default: 5)  
- `-p [PATH]` : path to save downloaded images (default: `./data/`)  

### Example
```sh
python spider.py -r -l 3 -p ./downloads https://example.com
```

---

## 🦂 Scorpion

The **Scorpion** program analyzes image files and extracts **EXIF and metadata** information.
It is compatible with the same file extensions as Spider.

### Usage
```sh
./scorpion.py FILE1 [FILE2 ...]
```

### Example
```sh
python scorpion.py ./downloads/image1.jpg ./downloads/image2.png
```

### Output
Displays metadata such as creation date, camera model, and EXIF data.
```
Metadata for ./downloads/image1.jpg:
Make: Canon
Model: EOS 80D
DateTime: 2023:08:01 12:34:56
...
----------------------------------------
```

---

## 🎯 Purpose
This project is designed for **learning Python scripting**, **web scraping fundamentals**, and **image metadata analysis**, while respecting the rule of implementing all logic manually.

