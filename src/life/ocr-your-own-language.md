# [OCR translate letters to your own language](http://harikrish.wordpress.com/2011/04/07/ubuntu-linux-command-line-tool-to-convert-pdf-to-image-and-from-image-to-pdf/)


1. Scan it into pdf (jpg, or png should also be OK) using a scanner/camera.

2. [optional] convert pdf into images on Ubuntu using convert command. For example,
```
convert -quality 100  -density 300x300 DOC101012-10102012095258.pdf DOC101012-10102012095258.jpg
```
This will split pages into images. Use higher density when needed.

3. Go to http://www.free-ocr.com/ and extract the text from image.

4. Copy the text and paste it at Google translation.
