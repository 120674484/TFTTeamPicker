import sys,random
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
heroes =['破败军团', '黑夜使者', '小恶魔', '丧尸', '圣光卫士', '黎明使者', '龙族', '铁甲卫士', '复生亡魂', '光明哨兵','刺客', '游侠', '斗士', '征服者', '复苏者', '神谕者', '骑士', '法师', '神盾战士', '秘术师', '重骑兵','强袭炮手']
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
        self.setWindowTitle("英雄联盟云顶之弈英雄之黎明")
    def show_random_hero_and_item(self):
        hero = random.choice(heroes)
        if hero == "神盾战士":
            item = '暴风大剑 金铲铲'
        elif hero == "法师":
            item = '无用大棒 金铲铲'
        elif hero == "复苏者":
            item = '女神之泪 金铲铲'
        elif hero == "圣光卫士":
            item = '负极斗篷 金铲铲'
        elif hero == "黎明使者":
            item = '巨人腰带 金铲铲'
        elif hero == "刺客":
            item = '拳套 金铲铲'
        elif hero == "小恶魔":
            item = '反曲之弓 金铲铲'
        elif hero == '斗士':
            item = '巨人腰带 金锅锅'
        elif hero == '光明哨兵':
            item = '锁子甲 金锅锅'
        elif hero == '破败军团':
            item = '暴风大剑 金锅锅'
        elif hero == '复生亡魂':
            item = '负极斗篷 金锅锅'
        elif hero == '黑夜使者':
            item = '女神之泪 金锅锅'
        elif hero == '丧尸':
            item = '拳套 金锅锅'
        elif hero == '征服者':
            item = '反曲之弓 金锅锅'
        else:
            item = ''
        self.label1.setText(hero)
        self.label2.setText(item)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())