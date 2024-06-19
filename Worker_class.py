import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess

class Worker(QThread):
    update_text = pyqtSignal(str)
    update_error =pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        # command를 실행합니다. universal_newlines=True는 text=True와 동일합니다(Python 3.7 이하 호환을 위해 사용)
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        
        # 프로세스의 표준 출력을 실시간으로 읽고 전송합니다.
        while True:
            output = process.stdout.readline()
            if output:
                self.update_text.emit(output.strip())
            else:
                break

        # 에러 발생 시 표준 에러 출력을 읽습니다.
        if process.stderr is not None:
            stderr = process.stderr.read()
            if stderr:
                self.update_error.emit(stderr.strip())

        # 프로세스 종료 대기
        process.wait()
        
        # 프로세스의 종료 코드를 확인하여 에러 여부를 판단합니다.
        if process.returncode != 0:
            self.update_error.emit(f"Command failed with return code {process.returncode}")

        # 프로세스의 출력을 실시간으로 읽습니다.
        # while True:
        #     line = process.stdout.readline()
        #     if not line:
        #         break
        #     self.update_text.emit(line)
        # process.stdout.close()
        # process.wait()



# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi()

#     def setupUi(self):
#         self.setGeometry(300, 300, 600, 400)
#         self.setWindowTitle('실시간 명령어 실행 결과')

#         self.textBrowser = QTextBrowser(self)
#         layout = QVBoxLayout()
#         layout.addWidget(self.textBrowser)

#         centralWidget = QWidget(self)
#         centralWidget.setLayout(layout)
#         self.setCentralWidget(centralWidget)

#         # 명령어 실행
#         self.runCommand()

#     def runCommand(self):
#         command = 'your_command_here'  # 실행하고 싶은 명령어
#         self.worker = Worker(command.split())  # command를 리스트 형태로 변환
#         self.worker.update_text.connect(self.appendText)
#         self.worker.start()

#     def appendText(self, text):
#         self.textBrowser.append(text)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     ex.show()
#     sys.exit(app.exec_())
