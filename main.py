import cv2
from hand_tracking.tracker import HandTracker
from gestures.recognizer import GestureRecognizer
from mouse_control.controller import MouseController

def main():
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    recognizer = GestureRecognizer()
    controller = MouseController()

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        landmarks_list, frame = tracker.get_landmarks(frame)

        if landmarks_list:
            landmarks = landmarks_list[0]  # only one hand
            gesture, coords = recognizer.detect_gesture(landmarks, w, h)
            controller.perform_action(gesture, coords)

        cv2.imshow("Hand Gesture Mouse", frame)
        if cv2.waitKey(1) == 27:  # ESC to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
