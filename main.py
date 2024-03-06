import cv2

# Load the video
cap = cv2.VideoCapture('path/to/video.mp4')

# Get the current video dimensions
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Set the desired resolution (width, height)
new_width = 640
new_height = 480

# Get the video codec and FPS
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object
out = cv2.VideoWriter('output_video.mp4', fourcc, fps, (new_width, new_height))

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        break

    # Resize the frame
    resized_frame = cv2.resize(frame, (new_width, new_height))

    # Write the resized frame to the output video
    out.write(resized_frame)

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()