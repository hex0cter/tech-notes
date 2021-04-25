
# [Image to text (OCR) for Swedish](http://code.google.com/p/tesseract-ocr/)

[**tesseract-ocr**](http://code.google.com/p/tesseract-ocr/) is a software package (from google) that can extract text from pictures. It supports multiple languages. Below is how it works with Swedish.

Download the latest tarball from:

http://code.google.com/p/tesseract-ocr/downloads/list

Follow the README to install it. (Don't forget to run sudo ldconfig at the end)

Another package leptonica is also needed. You should download and install the latest version from the link below before installing tesseract:

http://www.leptonica.org/download.html

You need to copy the Swedish training data from

http://code.google.com/p/tesseract-ocr/downloads/list

and copy the file swe.traineddata into /usr/loca/share/tessdata.

After everything is installed, run
```
tesseract test.jpg out -l swe
```
The text will be extracted and written into out.txt.
