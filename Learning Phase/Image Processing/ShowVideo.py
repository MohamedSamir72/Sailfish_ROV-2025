import cv2

# Open the video camera
cap = cv2.VideoCapture(0)

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error opening video file")

# Read and display frames from the video
while cap.isOpened():
    ret, frame = cap.read()  # Read a frame from the video

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
