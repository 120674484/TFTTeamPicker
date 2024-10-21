from json import loads
def bonds_deal(text):
    data =loads(text)
    bonds = []
    number_max=[]
    for item in data['data']:
        if item['characterid'] and list(item['level'].keys())[-1]>'1':
            number_max.append(int(list(item['level'].keys())[-1]))
            bonds.append(item['name'])
    return bonds,number_max
def chesses_deal(text):
    data=loads(text)
    number_max_limit={}
    for item in data['data']:
        if int(item['price']) > 0:
            if item['races']:
                races = item['races'].split(',')
                for race in races:
                    try:
                        number_max_limit[race]+=1
                    except:
                        number_max_limit[race]=1
            if item['jobs']:
                jobs=item['jobs'].split(',')
                for job in jobs:
                    try:
                        number_max_limit[job]+=1
                    except:
                        number_max_limit[job]=1
    return number_max_limit
def code2_generate(text,bonds,number_max,number_max_limit):
    data=loads(text)
    equipIds = []
    formulas=[]
    isShows=[]
    names_prefix=[]
    names_suffix=[]
    for item in data['data']:
        equipIds.append(item['equipId'])
        formulas.append(item['formula'])
        isShows.append(item['isShow'])
        names_prefix.append(item['name'][:-2])
        names_suffix.append(item['name'][-2:])
    flag=False
    for a in range(len(names_suffix)):
        if names_suffix[a]=='纹章' and isShows[a]=='1':
            if formulas[a]:
                index=bonds.index(names_prefix[a])
                if number_max_limit[names_prefix[a]]<number_max[index]:
                    equipId1,equipId2=formulas[a].split(',')
                    index1=equipIds.index(equipId1)
                    index2=equipIds.index(equipId2)
                    name1=names_prefix[index1]+names_suffix[index1]
                    name2=names_prefix[index2]+names_suffix[index2]
                    if name1[0]=='金':
                        name1,name2=name2,name1
                    if flag:
                        code2+=f'\n\t\telif hero == "{names_prefix[a]}":item ="{name1} {name2}"'
                    else:
                        code2=f'\n\t\tif hero == "{names_prefix[a]}":item ="{name1} {name2}"'
                        flag=True
    return code2
if __name__ == '__main__':
    from multiprocessing import Pool
    from asyncio import run
    from aiohttp import ClientSession
    async def main():
        with Pool() as pool:
            async with ClientSession() as session:
                chesses_text = await fetch(session, 'https://game.gtimg.cn/images/lol/act/img/tft/js/chess.js')
                result= pool.apply_async(chesses_deal, (chesses_text,))
            async with ClientSession() as session:
                races_text = await fetch(session, 'https://game.gtimg.cn/images/lol/act/img/tft/js/race.js')
                result_first= pool.apply_async(bonds_deal, (races_text,))
            async with ClientSession() as session:
                jobs_text = await fetch(session, 'https://game.gtimg.cn/images/lol/act/img/tft/js/job.js')
                result_second= pool.apply_async(bonds_deal, (jobs_text,))
            async with ClientSession() as session:
                equip_text=await fetch(session, 'https://game.gtimg.cn/images/lol/act/img/tft/js/equip.js')
                races, races_number_max = result_first.get()
                jobs, jobs_number_max = result_second.get()
                bonds = races + jobs
                result_third= pool.apply_async(code2_generate, (equip_text,bonds,races_number_max+jobs_number_max,result.get()))
            code2 = result_third.get()
            version = input()
            code1=f'from random import choice\nfrom PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget\nfrom PySide6.QtGui import QFont\nfrom PySide6.QtCore import Qt\nheroes ={bonds}\nclass MainWindow(QMainWindow):\n\tdef __init__(self):\n\t\tsuper().__init__()\n\t\tself.init_ui()\n\tdef init_ui(self):\n\t\tself.label1 = QLabel("", self)\n\t\tself.label2 = QLabel("", self)\n\t\tfont = QFont()\n\t\tfont.setPointSize(16)\n\t\tself.label1.setFont(font)\n\t\tself.label2.setFont(font)\n\t\tbutton = QPushButton("随机选择", self)\n\t\tbutton.setFont(font)\n\t\tbutton.setFixedHeight(50)\n\t\tbutton.clicked.connect(self.show_random_hero_and_item)\n\t\tmain_layout = QVBoxLayout()\n\t\tlabel_layout1 = QHBoxLayout()\n\t\tlabel_layout1.addWidget(self.label1)\n\t\tlabel_layout1.setAlignment(self.label1, Qt.AlignCenter)\n\t\tlabel_layout2 = QHBoxLayout()\n\t\tlabel_layout2.addWidget(self.label2)\n\t\tlabel_layout2.setAlignment(self.label2, Qt.AlignCenter)\n\t\tmain_layout.addLayout(label_layout1)\n\t\tmain_layout.addLayout(label_layout2)\n\t\tmain_layout.addWidget(button)\n\t\tcentral_widget = QWidget()\n\t\tcentral_widget.setLayout(main_layout)\n\t\tself.setCentralWidget(central_widget)\n\t\tself.setWindowTitle("{version}")\n\tdef show_random_hero_and_item(self):\n\t\thero =choice(heroes)'
            code=code1+code2+f'\n\t\telse:item =""\n\t\tself.label1.setText(hero)\n\t\tself.label2.setText(item)\napp = QApplication()\nwindow = MainWindow()\nwindow.showMaximized()\napp.exec()'
            with open(f'{version}.py', 'w',encoding='utf-8') as f:
                f.write(code)
    async def fetch(session,url):
        async with session.get(url) as response:
            return await response.text()
    code=run(main())