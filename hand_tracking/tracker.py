import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1):
        self.hands = mp.solutions.hands.Hands(max_num_hands=max_hands)
        self.mp_draw = mp.solutions.drawing_utils

    def get_landmarks(self, frame):
        """Returns hand landmarks normalized [0,1]."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb_frame)
        landmarks_list = []

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                landmarks = handLms.landmark
                landmarks_list.append(landmarks)

        return landmarks_list, frame
