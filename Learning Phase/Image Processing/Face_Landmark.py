import cv2
import mediapipe as mp

# Initialize the MediaPipe FaceMesh and Drawing utils
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

# Set up the drawing specifications for landmarks
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1, color=(0, 255, 0))

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(image_rgb)

        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        # Draw the face landmarks on the image
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp_drawing.draw_landmarks(
                    image=image_bgr,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=drawing_spec)

        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Face Mesh', cv2.flip(image_bgr, 1))
        
        if cv2.waitKey(5) & 0xFF == 27:
            break
            
    cap.release()
    cv2.destroyAllWindows()
