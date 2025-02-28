from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFrame
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class LoginUI(QWidget):
    def __init__(self):
        super().__init__()

        # Cấu hình cửa sổ
        self.setWindowTitle("Login - GoFinance")
        self.setGeometry(100, 100, 900, 500)
        self.setStyleSheet("background-color: #f4f4f4; border-radius: 10px;")

        # Layout chính
        main_layout = QHBoxLayout(self)

        # --- Left Frame (GoFinance Info) ---
        left_frame = QFrame(self)
        left_frame.setStyleSheet("""
            background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #0066FF, stop:1 #003399); 
            border-top-left-radius: 20px; 
            border-bottom-left-radius: 20px;
        """)
        left_layout = QVBoxLayout(left_frame)

        title = QLabel("GoFinance", self)
        title.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        title.setStyleSheet("color: white;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("The most popular peer to peer lending at SEA", self)
        subtitle.setFont(QFont("Arial", 12))
        subtitle.setStyleSheet("color: white;")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        read_more_btn = QPushButton("Read More", self)
        read_more_btn.setStyleSheet("""
            background-color: white; 
            color: #0066FF; 
            border-radius: 15px; 
            padding: 8px;
        """)

        left_layout.addWidget(title)
        left_layout.addWidget(subtitle)
        left_layout.addWidget(read_more_btn)
        left_layout.addStretch()  # Đẩy nút xuống dưới

        # --- Right Frame (Login Form) ---
        right_frame = QFrame(self)
        right_frame.setStyleSheet("""
            background: white; 
            border-top-right-radius: 20px; 
            border-bottom-right-radius: 20px;
        """)
        right_layout = QVBoxLayout(right_frame)

        hello_label = QLabel("Hello Again!", self)
        hello_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        hello_label.setStyleSheet("color: #333;")
        hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        welcome_label = QLabel("Welcome Back", self)
        welcome_label.setFont(QFont("Arial", 12))
        welcome_label.setStyleSheet("color: gray;")
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        email_input = QLineEdit(self)
        email_input.setPlaceholderText("Email Address")
        email_input.setStyleSheet("""
            border: 1px solid lightgray; 
            border-radius: 20px; 
            padding: 10px;
        """)

        password_input = QLineEdit(self)
        password_input.setPlaceholderText("Password")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_input.setStyleSheet("""
            border: 1px solid lightgray; 
            border-radius: 20px; 
            padding: 10px;
        """)

        login_button = QPushButton("Login", self)
        login_button.setStyleSheet("""
            background-color: #0066FF; 
            color: white; 
            border-radius: 20px; 
            padding: 10px;
        """)

        forgot_label = QLabel("Forgot Password", self)
        forgot_label.setFont(QFont("Arial", 10))
        forgot_label.setStyleSheet("color: gray; text-decoration: underline; cursor: pointer;")
        forgot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        right_layout.addWidget(hello_label)
        right_layout.addWidget(welcome_label)
        right_layout.addWidget(email_input)
        right_layout.addWidget(password_input)
        right_layout.addWidget(login_button)
        right_layout.addWidget(forgot_label)

        # Thêm các khối vào giao diện chính
        main_layout.addWidget(left_frame, 1)
        main_layout.addWidget(right_frame, 1)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = LoginUI()
    window.show()
    sys.exit(app.exec())
