# Image Processing Server with Flask

This repository contains a Flask-based web application designed for basic image processing operations. Users can upload an image and select a variety of transformations to apply, including resizing, rotating, and converting images to grayscale. The processed images can be previewed and downloaded through a user-friendly web interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.9 or higher installed on your machine.
- PIL (Python Imaging Library) installed, we're using `Pillow` in this project, a modern fork of PIL.
- Flask and Flasgger for the web server and Swagger UI documentation.

## Installation

Follow these steps to get your development env running:
1. Clone the repository to your local machine:
   ```
   git clone https://github.com/jay-singhvi/PyFlask-RPC-ImgProcessor.git
   ```
2. Navigate to the cloned repository directory:
   ```
   cd PyFlask-RPC-ImgProcessor
   ```
3. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```
   Note: This project assumes you have a `requirements.txt` file listing all the necessary packages.

## Usage

To run the Flask application, execute the following command from the root directory of the project:

```
python IP_Flask_Server.py
```

Navigate to `http://127.0.0.1:5000/ipMain` in your web browser to access the web application.

### How to Use the Web Application

1. **Upload an Image**: Select an image file from your computer to upload.
2. **Choose Operations**: Select the image operations you wish to apply (e.g., resize, rotate, convert to grayscale).
3. **Submit**: Submit the form to process the image.
4. **View and Download**: View the processed images and download them if desired.

## Contributing

Contributions to this project are welcome! Here are a few ways you can help:

- Report bugs.
- Add new features or extend existing ones.
- Improve documentation.

To contribute, please fork the repository, make your changes, and submit a pull request.

## Acknowledgments

- Thanks to the Flask team for the excellent micro web framework.
- The Pillow project for making Python image processing work a breeze.
