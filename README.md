# Video Black Frame Checker v1.0.1

## Overview

The Video Black Frame Checker is a simple yet powerful tool for detecting full black frames in video files. This Python application uses OpenCV to process videos and identifies moments where black frames appear. The user-friendly interface allows drag-and-drop functionality for quick processing.

## Features

- **Drag and Drop Support**: Easily add video files by dragging them into the application.
- **Real-time Progress Tracking**: Displays frame count and processing status.
- **Accurate Timestamps**: Lists timecodes where black frames are detected.
- **Multi-threaded Processing**: Keeps the UI responsive during video analysis.

## Installation

### Prerequisites

Ensure you have Python 3 installed. Then, install the required packages:

```bash
pip install -r requirements.txt
```

### Dependencies

- OpenCV
- NumPy
- TkinterDnD2

## Usage

Run the script:

```bash
python script.py
```

1. Drag and drop a video file into the application window.
2. The app will process the video and display timestamps for detected black frames.

## File Structure

```
|-- main.py
|-- icon.ico
|-- requirements.txt
|-- README.md
```


## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Author

Developed by [Imaan](https://github.com/1maan).