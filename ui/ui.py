from kiwoom.kiwoom import *
from PyQt5.QtWidgets import QApplication
import sys

class UI_class():
    def __init__(self):
        print("ui클래스임")

        # sys.argv = ['파이썬파일경로', '추가할옵션', '추가할옵션']
        self.app = QApplication(sys.argv)

        self.kiwoom = Kiwoom()

        self.app.exec_() # 프로그램 종료 방지