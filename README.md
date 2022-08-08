# ASCII art converter


Simple script to convert an image to an ANSI representation of it

Prerequisites
-
You need to have python installed and then run the following command:

```bash
pip install -r requirements.txt
```

Usage
-
```
python3 art.py [-i] [-w] [-f]

- i     the path to the image
- w     the width of the ascii image
- f     whether or not the foreground of the characters is set (default is set to False)
```

Example
-
```bash
python3 art.py -i wave.jpg -w 100
```
Converts the image
![Wave](wave.jpg)

to the ASCII representation
![Wave_ascii](ascii_wave.jpg)
