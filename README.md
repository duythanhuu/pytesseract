# OCR Word Position Detection

This project demonstrates how to detect the position of words in an image using Optical Character Recognition (OCR) with Python. The `pytesseract` library is used as a wrapper for Google's Tesseract-OCR Engine, and `opencv-python` is used for image processing.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system
- Tesseract-OCR installed on your system. You can download it from [here](https://github.com/UB-Mannheim/tesseract/wiki) for Window.

## Installation

To set up the project, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/duythanhuu/pytesseract.git
    cd pytesseract 
    ```

2. Install the required Python libraries:
    ```sh
    pip install pytesseract opencv-python
    ```

3. Configure the path to the Tesseract executable in the script:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

## Usage

To detect the positions of words in an image, follow these steps:

The script will display the image with bounding boxes drawn around each detected word and print the positions of the detected words in the console.


The displayed image will have green bounding boxes around each detected word.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [OpenCV](https://opencv.org/)

