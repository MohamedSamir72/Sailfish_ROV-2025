import cv2
import time

# Open a video file or capture device. 0 is the default camera
cap = cv2.VideoCapture(0)

# Check if the video capture is opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Variable initialization
fps = 0
frame_count = 0
start_time = time.time()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        break

    # Display the frame
    cv2.imshow('Frame', frame)

    # Calculate FPS
    frame_count += 1
    if frame_count >= 30:  # Calculate FPS every 30 frames
        end_time = time.time()
        fps = frame_count / (end_time - start_time)
        start_time = end_time
        frame_count = 0
        print(f"FPS: {fps:.2f}")

    # Press Q on keyboard to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
