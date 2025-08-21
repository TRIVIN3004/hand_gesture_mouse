import pyautogui

class MouseController:
    def __init__(self):
        self.screen_w, self.screen_h = pyautogui.size()

    def perform_action(self, gesture, coords):
        """Maps gestures to mouse actions."""
        x, y = coords
        screen_x, screen_y = int(x * self.screen_w), int(y * self.screen_h)

        if gesture == "move":
            pyautogui.moveTo(screen_x, screen_y)

        elif gesture == "left_click":
            pyautogui.click()

        elif gesture == "right_click":
            pyautogui.click(button="right")

        elif gesture == "scroll_up":
            pyautogui.scroll(100)   # Scroll up

        elif gesture == "scroll_down":
            pyautogui.scroll(-100)  # Scroll down
