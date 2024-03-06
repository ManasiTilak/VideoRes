# Change Video Resolution with OpenCV in Python

This Python script demonstrates how to change the resolution of a video using OpenCV. It allows you to load a video file, set the desired resolution, and create a new video file with the specified resolution.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library installed

## Usage

1. Clone or download this repository.
2. Replace `'path/to/video.mp4'` in the code with the actual path to your input video file.
3. Adjust the desired resolution by changing the values of `new_width` and `new_height` in the code.
4. Run the script using the following command:python VideoRes.py
5. The script will process the input video and create a new video file named `output_video.mp4` with the specified resolution in the same directory.

## Code Explanation

1. The script starts by importing the required OpenCV library.
2. The input video is loaded using `cv2.VideoCapture`.
3. The current video dimensions are retrieved using `cap.get(cv2.CAP_PROP_FRAME_WIDTH)` and `cap.get(cv2.CAP_PROP_FRAME_HEIGHT)`.
4. The desired resolution for the output video is set by defining `new_width` and `new_height`.
5. A `VideoWriter` object is created with the desired resolution, codec (`mp4v`), and frame rate.
6. A loop iterates over each frame of the input video, resizing it using `cv2.resize` and writing it to the output video using `out.write`.
7. Finally, the resources are released by calling `cap.release()`, `out.release()`, and `cv2.destroyAllWindows()`.

## Dependencies

- OpenCV (cv2) library

Make sure you have OpenCV installed in your Python environment. You can install it using pip: pip install opencv-python