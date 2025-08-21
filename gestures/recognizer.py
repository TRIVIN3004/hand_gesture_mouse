class GestureRecognizer:
    def __init__(self):
        self.prev_y = None  # For scroll detection

    def detect_gesture(self, landmarks, frame_w, frame_h):
        """Detects gestures based on landmarks."""
        index_tip = landmarks[8]
        thumb_tip = landmarks[4]
        middle_tip = landmarks[12]

        # Convert normalized [0,1] → pixel coords
        index_x, index_y = int(index_tip.x * frame_w), int(index_tip.y * frame_h)
        thumb_x, thumb_y = int(thumb_tip.x * frame_w), int(thumb_tip.y * frame_h)
        middle_x, middle_y = int(middle_tip.x * frame_w), int(middle_tip.y * frame_h)

        gesture = "move"

        # Left click (thumb + index close)
        if abs(index_x - thumb_x) < 20 and abs(index_y - thumb_y) < 20:
            gesture = "left_click"

        # Right click (thumb + middle close)
        elif abs(middle_x - thumb_x) < 20 and abs(middle_y - thumb_y) < 20:
            gesture = "right_click"

        # Scroll detection (index & middle fingers together moving up/down)
        elif abs(index_x - middle_x) < 40:  
            if self.prev_y is not None:
                if index_y - self.prev_y > 15:   # Moved down
                    gesture = "scroll_down"
                elif self.prev_y - index_y > 15: # Moved up
                    gesture = "scroll_up"
            self.prev_y = index_y

        else:
            self.prev_y = None  # Reset if not in scroll mode

        return gesture, (index_tip.x, index_tip.y)
