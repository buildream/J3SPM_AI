from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

class MyDialog(QDialog):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)

        self.setWindowTitle('Notice')

        # 레이아웃 생성
        layout = QVBoxLayout()

        # 레이블 생성 및 추가
        self.label= QLabel(label_text,self)
        layout.addWidget(self.label)

        # 닫기 버튼 생성 및 추가
        close_button = QPushButton('Close')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        # 레이아웃 설정
        self.setLayout(layout)
