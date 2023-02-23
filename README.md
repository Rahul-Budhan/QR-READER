### QR Code Reader
This program reads QR codes from images using the zbarlight module in Python.

### QR Code Generator
This program generates QR codes from images using the qrcode module in Python.

### Usage
To use the program, run python qr_reader.py <image_path> in the terminal.

Replace <image_path> with the path to the image containing the QR code you want to read or where you want to generate.

The program will attempt to read the QR code from the image and display the decoded message on the screen.

### Dependencies
This program requires Python 3.6 or later to be installed on your system.

### The following additional third-party libraries are required:

+ Pillow for reading images
+ zbarlight for decoding QR codes
+ You can install these libraries using pip. For example:

```
pip install Pillow
pip install zbarlight
```
