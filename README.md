# OCR Word Position Detection

This project demonstrates how to detect the position of words in an image using Optical Character Recognition (OCR) with Python. The `pytesseract` library is used as a wrapper for Google's Tesseract-OCR Engine, and `opencv-python` is used for image processing.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system
- Tesseract-OCR installed on your system. You can download it from [here](https://github.com/UB-Mannheim/tesseract/wiki) for Window.

## Usage

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
4. Run python script:
    ```python
    python words_detection.py
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [pytesseract](https://github.com/madmaze/pytesseract)
- [OpenCV](https://opencv.org/)

