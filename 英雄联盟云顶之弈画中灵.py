import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import random
heroes = ["夜幽","天将","灵魂莲华","幽魂","山海绘卷","青花瓷","天龙之子","吉星","永恒之森","剪纸仙灵","墨之影","武仙子","法师","擎天卫","斗士","决斗大师","尊者","神谕者","死神","圣贤","狙神","迅捷射手","护卫"]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.label1 = QLabel("", self)
        self.label2 = QLabel("", self)
        font = QFont()
        font.setPointSize(16)
        self.label1.setFont(font)
        self.label2.setFont(font)
        button = QPushButton("随机选择", self)
        button.setFont(font)
        button.setFixedHeight(50)
        button.clicked.connect(self.show_random_hero_and_item)
        main_layout = QVBoxLayout()
        label_layout1 = QHBoxLayout()
        label_layout1.addWidget(self.label1)
        label_layout1.setAlignment(self.label1, Qt.AlignCenter)
        label_layout2 = QHBoxLayout()
        label_layout2.addWidget(self.label2)
        label_layout2.setAlignment(self.label2, Qt.AlignCenter)
        main_layout.addLayout(label_layout1)
        main_layout.addLayout(label_layout2)
        main_layout.addWidget(button)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setWindowTitle("英雄联盟云顶之弈画中灵")
    def show_random_hero_and_item(self):
        hero = random.choice(heroes)
        if hero == "夜幽":
            item = '拳套'
        elif hero == "天将":
            item = '负极斗篷'
        elif hero == "灵魂莲华":
            item = '无用大棒'
        elif hero == "幽魂":
            item = '暴风大剑'
        elif hero == "山海绘卷":
            item = '女神之泪'
        elif hero == "青花瓷":
            item = '反曲之弓'
        elif hero == "永恒之森":
            item = '巨人腰带'
        elif hero == "剪纸仙灵":
            item = '锁子甲'
        else:
            item = ''
        self.label1.setText(hero)
        self.label2.setText(item)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())