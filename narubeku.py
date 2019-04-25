#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import webbrowser
from PyQt5.QtWidgets import *  #(QWidget, QPushButton, QLabel, QFrame, QApplication, QLineEdit,QHBoxLayout)
from PyQt5.QtGui import *


class Warikan(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        # トグルボタンの作成
        personb = QPushButton('人数', self)
        personb.setCheckable(True)
        personb.move(35, 30)

        pQ = QLineEdit(self)
        pQ.move(40, 10)
        # クリックされたらsetColor関数の呼び出し
        personb.clicked[bool].connect(self.setColor)

        moneyb = QPushButton('合計金額', self)
        moneyb.setCheckable(True)
        moneyb.move(35, 90)

        mQ = QLineEdit(self)
        mQ.move(40, 60)

        moneyb.clicked[bool].connect(self.setColor)

        resultb = QPushButton('結果発表', self)
        resultb.setCheckable(True)
        resultb.move(35, 160)

        rQ = QLineEdit(self)
        rQ.move(40, 130)
        resultb.clicked[bool].connect(self.wari)


        ##self.square = QFrame(self)
        ##self.square.setGeometry(150, 20, 100, 100)
        ##self.square.setStyleSheet("QWidget { background-color: %s }" %  
        ##    self.col.name())



        # qleに文字が入力されたら、onChanged関数の呼び出し
       ## qle.textChanged[str].connect(self.onChanged)



        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('割り勘で世界の不平等を無くす')
        self.show()


               
    def wari(self,pressed):
        num=(input())
        person=(input())
        sum=num//person
        print(sum)


    def setColor(self, pressed):

        # 押されたボタンをsource変数に代入
        source = self.sender()      

        # ボタンがクリックされたら、色を設定
        if pressed:
            val = 255
        else: val = 0

        # Redボタンが押されたら、色に赤を混ぜる
        if source.text() == "人数":
            print('そのボタンは未実装です')
            #self.col.setRed(val)    
        # Greenボタンが押されたら、色に緑を混ぜる            
        elif source.text() == "金額":
            print('そのボタンも未実装です')
            #self.col.setGreen(val)   
        # Blueボタンが押されたら、色に青を混ぜる
        else: 
            url='https://keisan.casio.jp/exec/system/1244792650'
            webbrowser.open(url)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Warikan()
    sys.exit(app.exec_())