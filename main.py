import sys
from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QMessageBox








class MyCalc(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyCalc, self).__init__()

        self.setWindowTitle("My Calculator")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(350, 150, 340, 490)
        
        self.setMinimumSize(340, 490)
        self.setMaximumSize(340, 490)
        
       
        self.initUI()





    def initUI(self):

        # Create Result PlainTextEdit
        self.resultText = QtWidgets.QTextEdit(self)
        self.resultText.setGeometry(20, 20, 300, 90)
        # self.resultText.setDisabled(True)
        self.resultText.setReadOnly(True)
        self.resultText.setStyleSheet("background-color: white;")
        self.resultText.setFont(QFont("Times", 20))
        
        
        
        self.buttons = self.createButtons()
       


        



    
    def clearResultText(self):
        self.resultText.setText("")

    def btn_Clicked(self):
        self.resultText.insertPlainText(self.sender().text())
        # print(self.resultText.toPlainText())
    
    
    def calculate(self):
        msg = QMessageBox()
        msg.setWindowTitle('Calculator')
        msg.setIcon(QMessageBox.Information)                
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        
        text = self.resultText.toPlainText()
        try:
            r = eval(text)
        except TypeError:
            msg.setText("Hesaplanamadı !")
            x = msg.exec_()
            return 0
        except SyntaxError:
            msg.setText("Hesaplanamadı !")
            x = msg.exec_()
            return 0
        except ZeroDivisionError:
            msg.setText("Hiç bir sayı '0' a bölünmez !")
            x = msg.exec_()
            return 0
        # print(text)
        # print("-"*30)
        # print(r)
        msg.setText(f"Sonuç : {r}")
        x = msg.exec_()
        
    

        
      
        

    def createButtons(self):
        buttons = {}
        
        # number buttons size
        NB_SIZE = (55+5, 55+5)
        # number buttons function
        NB_FUNC = self.btn_Clicked
        # number buttons border-radius value
        NB_BD_RD = 30
        
        BTNS = {
            "0": ([35,410, 125+5,  NB_SIZE[1]-4], "red", 28, NB_FUNC),
            ".": ([180,410, NB_SIZE[0]-4, NB_SIZE[1]-4],"red", 28, NB_FUNC),    
            
            "(": ([105,130, *NB_SIZE], "yellow", NB_BD_RD, NB_FUNC),
            ")": ([175,130, *NB_SIZE], "yellow", NB_BD_RD, NB_FUNC),
            "/": ([245,130, *NB_SIZE], "yellow", NB_BD_RD, NB_FUNC),
            "*": ([245,200, *NB_SIZE], "yellow", NB_BD_RD, NB_FUNC),
            "-": ([245,270, *NB_SIZE], "yellow", NB_BD_RD, NB_FUNC),
            "+": ([245,340, *NB_SIZE], "yellow", NB_BD_RD, NB_FUNC),
            
            "C": ([35,130, *NB_SIZE], "darkgreen", NB_BD_RD, self.clearResultText),
            "=": ([245,410, *NB_SIZE], "darkgreen", NB_BD_RD, self.calculate),         
            }
        
        # Create Buttons
        for bText, val in BTNS.items():      
            btn = QtWidgets.QPushButton(self)
            btn.setText(bText)
            btn.setFont(QFont("Times", 20))
            btn.setGeometry(*val[0])
            btn.setStyleSheet(f"color: white; background-color: black; border: 2 solid {val[1]}; border-radius: {val[2]}px;")
            btn.clicked.connect(val[-1])
            
            # Return Buttons data add button
            buttons[bText] = btn    
        
        
        # Number button to Creatting
        x = 35
        y = 340
        for i in range(1, 10):
            btn = QtWidgets.QPushButton(self)
            btn.setText(str(i))
            btn.setFont(QFont("Times", 20))
            btn.setStyleSheet(f"color: white; background-color: black; border: 2 solid red; border-radius: {NB_BD_RD}px;")
            btn.clicked.connect(NB_FUNC)

            # set Geometry
            btn.setGeometry(x,y, *NB_SIZE)
            x += 70
            if i%3==0:
                x = 35
                y -= 70
            # Return Buttons data add button
            buttons[str(i)] = btn
            
            
        # btnC = QtWidgets.QPushButton(self)
        # btnC.setText()
        # btnC.setFont(QFont("Times", 20))
        # btnC.setStyleSheet("color: white; background-color: black; border: 2 solid darkgreen;")
        # btnC.clicked.connect(self.clearResultText)
        # btnC.setGeometry()
        
        return buttons  
            






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myWin = MyCalc()
    
    myWin.show()
    sys.exit(app.exec())

