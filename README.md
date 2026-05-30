# QR Code Generator using Python

A simple Python project that generates a QR code for a given URL using the `qrcode` and `Pillow` libraries.

## Features

* Generate QR codes from any text or URL
* Custom QR code color
* High error correction level
* Save QR code as a PNG image

## Requirements

Install the required libraries:

```bash
pip install qrcode[pil]
```

or

```bash
pip install qrcode pillow
```
## Usage

1. Replace `'Website URL'` with your desired URL or text.

Example:

```python
qr.add_data('https://github.com')
```

2. Run the script:

```bash
python qr_generator.py
```

3. The generated QR code will be saved as:

```text
qr.png
```

## Output

The program generates a QR code image similar to:

```text
project-folder/
│
├── qr_generator.py
└── qr.png
```

## Configuration Options

| Parameter        | Description            |
| ---------------- | ---------------------- |
| version          | Controls QR code size  |
| error_correction | Error correction level |
| box_size         | Size of each QR box    |
| border           | Border thickness       |
| fill_color       | QR code color          |
| back_color       | Background color       |

### Error Correction Levels

```python
qrcode.constants.ERROR_CORRECT_L  # 7%
qrcode.constants.ERROR_CORRECT_M  # 15%
qrcode.constants.ERROR_CORRECT_Q  # 25%
qrcode.constants.ERROR_CORRECT_H  # 30%
```

## Example Output

* Blue QR code
* White background
* PNG format

## Future Enhancements

* Add logo inside QR code
* Generate QR codes from user input
* Create colored and gradient QR codes
* Build a GUI using Tkinter
* Develop a web version using Flask or Django

## Author

Addwin Alanolikkal
