from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal
import sys
#import os
import pyautogui
import pytesseract
from PIL import Image


class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.text_window = None  # Placeholder for the secondary window

    def init_ui(self):
        self.setWindowTitle("Transparent Window")
        self.setGeometry(100, 100, 300, 200)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Create the button to open the text window and take screenshot
        self.button = QPushButton("+", self)
        self.button.resize(self.width(), 30)  # Set the height to be 30px and width to window width
        self.button.clicked.connect(self.handle_button_click)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: 1px solid black;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: lightblue;
            }
            QPushButton:pressed {
                background-color: darkblue;
                color: white;
            }
        """)

        # Add event filter to handle cursor dynamically
        self.button.installEventFilter(self)

        self.update_button_position()  # Ensure button starts in the bottom-right corner

    def eventFilter(self, source, event):
        """Handle hover events for the button."""
        if source == self.button:
            if event.type() == event.Enter:  # Cursor enters the button
                self.button.setCursor(Qt.PointingHandCursor)
            elif event.type() == event.Leave:  # Cursor leaves the button
                self.button.unsetCursor()
        return super().eventFilter(source, event)

    def update_button_position(self):
        """Ensure the button stretches across the bottom of the window."""
        window_width = self.width()
        button_height = 30  # Fixed button height
        self.button.resize(window_width, button_height)  # Resize button to window width and fixed height
        self.button.move(0, self.height() - button_height)  # Move the button to the bottom of the window

    def handle_button_click(self):
        """Handle the button click to either open the text window or take a screenshot."""
        # Check if the text window is already open
        if self.text_window is None:  # If the text window doesn't exist, create it
            self.open_text_window()
        else:  # If the text window is open, take the screenshot
            self.take_screenshot()

    def open_text_window(self):
        """Open or create the secondary text window and set its text."""
        if self.text_window is None:  # Create the text window only if it doesn't exist
            self.text_window = TextWindow()  # Create the text window
            self.text_window.closed.connect(self.on_text_window_closed)  # Connect to the closed signal

        self.text_window.setGeometry(self.geometry())  # Set the second window's size to match the main window
        self.text_window.show()
        self.update_text_window_position()

    def on_text_window_closed(self):
        """Reset the text window reference when it is closed."""
        self.text_window = None

    def update_text_window_position(self):
        """Align the secondary window to the right of the main window or left if close to screen edge."""
        if self.text_window:
            main_geometry = self.geometry()
            screen_geometry = QApplication.desktop().screenGeometry()

            # Check if there is enough space on the right side
            x = main_geometry.x() + main_geometry.width() + 10  # Position to the right of the main window
            y = main_geometry.y()

            # If the text window would be off the screen, place it on the left
            if x + self.text_window.width() > screen_geometry.right():
                x = main_geometry.x() - self.text_window.width() - 10  # Position to the left of the main window

            # Ensure the window stays within the vertical bounds of the screen
            if y + self.text_window.height() > screen_geometry.bottom():
                y = screen_geometry.bottom() - self.text_window.height() - 10

            self.text_window.move(x, y)

    def resizeEvent(self, event):
        """Reposition the button when the window is resized."""
        self.update_button_position()
        self.update_text_window_position()
        super().resizeEvent(event)

    def moveEvent(self, event):
        """Reposition the secondary window when the main window moves."""
        self.update_text_window_position()
        super().moveEvent(event)

    def paintEvent(self, event):
        """Draw a transparent background."""
        self.setStyleSheet("background: rgba(255, 255, 255, 50);")

    def take_screenshot(self):
        """Capture the visible area inside the main window and save it as an image in the script directory."""
        main_geometry = self.geometry()
        button_height = self.button.height()  # Get the button's height to exclude from the screenshot

        # Capture the area inside the main window but exclude the bottom part where the button is located
        screenshot = pyautogui.screenshot(region=(main_geometry.x(), main_geometry.y(), main_geometry.width(), main_geometry.height() - button_height))

        image = Image.frombytes("RGB", screenshot.size, screenshot.tobytes())

        # Use Tesseract OCR to extract text from the image
        extracted_text = pytesseract.image_to_string(image, lang='eng+rus')

        self.text_window.set_text(extracted_text)

        # # Get the current script's directory
        # script_directory = os.path.dirname(os.path.abspath(__file__))

        # # Define the file path for the screenshot
        # file_name = os.path.join(script_directory, "screenshot.png")

        # # Save the screenshot in the same directory as the script
        # screenshot.save(file_name)
        # print(f"Screenshot saved as {file_name}")


class TextWindow(QWidget):
    closed = pyqtSignal()  # Signal to notify when the window is closed

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Text Window")
        layout = QVBoxLayout(self)
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def set_text(self, text):
        """Set the given text into the text edit field."""
        self.text_edit.setText(text)

    def closeEvent(self, event):
        """Emit the closed signal when the window is closed."""
        self.closed.emit()  # Emit the closed signal
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TransparentWindow()
    main_window.show()
    sys.exit(app.exec_())
