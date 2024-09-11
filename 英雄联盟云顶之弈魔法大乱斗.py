import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
import random
heroes = ["命运之子", "龙族", "魔神使者", "花仙子", "冰霜", "小蜜蜂", "次元术士", "炎魔","咖啡甜心", "诅咒女巫", "时间学派", "堡垒卫士", "强袭枪手", "猎手", "术师","法师", "魔战士", "复苏者", "学者", "换形师", "重装战士", "狂暴战士"]
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
        self.setWindowTitle("英雄联盟云顶之弈魔法大乱斗")
    def show_random_hero_and_item(self):
        hero = random.choice(heroes)
        if hero == "魔神使者":
            item = '巨人腰带'
        elif hero == "花仙子":
            item = '女神之泪'
        elif hero == "冰霜":
            item = '锁子甲'
        elif hero == "小蜜蜂":
            item = '拳套'
        elif hero == "次元术士":
            item = '无用大棒'
        elif hero == "炎魔":
            item = '反曲之弓'
        elif hero == "咖啡甜心":
            item = '暴风大剑'
        elif hero == "诅咒女巫":
            item = '负极斗篷'
        else:
            item = ''
        self.label1.setText(hero)
        self.label2.setText(item)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())