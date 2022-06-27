# SVG : An SVG file is a graphics file that uses a two-dimensional graphic vector format 
# that defines images using an XML-based text format.
# As a standard format for showing vector graphics on the web, SVG files are developed.
# svg= converts links into image format

import pyqrcode



l="https://www.google.com/search?q=cricbuzz&oq=&aqs=chrome.0.35i39i362l8.239451348j0j7&sourceid=chrome&ie=UTF-8"

# url generates qrcode

url=pyqrcode.create(l)

#produce qr code from to image 

url.svg("mypaytm.svg",scale=10)