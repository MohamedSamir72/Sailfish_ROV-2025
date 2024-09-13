from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

from gui import *
    
import math

# Handle all screens (HD or 4k)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

class MainWindow(Ui_MainWindow, QMainWindow):
    label = ""
    history = {}
    history_text = "Operations:\n"
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.last_result = None

        self.ui.simple_bt.clicked.connect(self.s_page)
        self.ui.advanced_bt.clicked.connect(self.a_page)
        self.ui.history_bt.clicked.connect(self.h_page)

        for i in range(10):
            button = getattr(self.ui, f"button{i}")
            button.setCursor(Qt.PointingHandCursor)
            
            button_2 = getattr(self.ui, f"button{i}_2")
            button_2.setCursor(Qt.PointingHandCursor)


        self.ui.button_plus.setCursor(Qt.PointingHandCursor)
        self.ui.button_plus_2.setCursor(Qt.PointingHandCursor)
        self.ui.button_minus.setCursor(Qt.PointingHandCursor)
        self.ui.button_minus_2.setCursor(Qt.PointingHandCursor)
        self.ui.button_multi.setCursor(Qt.PointingHandCursor)
        self.ui.button_multi_2.setCursor(Qt.PointingHandCursor)
        self.ui.button_division.setCursor(Qt.PointingHandCursor)
        self.ui.button_division_2.setCursor(Qt.PointingHandCursor)
        self.ui.button_clear.setCursor(Qt.PointingHandCursor)
        self.ui.button_clear_2.setCursor(Qt.PointingHandCursor)    
        self.ui.ac_bt.setCursor(Qt.PointingHandCursor)
        self.ui.ac_bt_2.setCursor(Qt.PointingHandCursor)
        self.ui.button_equal.setCursor(Qt.PointingHandCursor)
        self.ui.button_equal_2.setCursor(Qt.PointingHandCursor)
        self.ui.ans_bt.setCursor(Qt.PointingHandCursor)
        self.ui.ans_bt_2.setCursor(Qt.PointingHandCursor)



        for i in range(10):
            clicking = getattr(self.ui, f"button{i}")
            clicking.clicked.connect(getattr(self, f"click_bt{i}"))

            clicking = getattr(self.ui, f"button{i}_2")
            clicking.clicked.connect(getattr(self, f"click_bt{i}"))

        self.ui.button_plus.clicked.connect(self.click_add)
        self.ui.button_plus_2.clicked.connect(self.click_add)
        self.ui.button_minus.clicked.connect(self.click_sub)
        self.ui.button_minus_2.clicked.connect(self.click_sub)
        self.ui.button_multi.clicked.connect(self.click_multi)
        self.ui.button_multi_2.clicked.connect(self.click_multi)
        self.ui.button_division.clicked.connect(self.click_div)
        self.ui.button_division_2.clicked.connect(self.click_div)
        self.ui.button_clear.clicked.connect(self.click_clear)    
        self.ui.button_clear_2.clicked.connect(self.click_clear)    
        self.ui.ac_bt.clicked.connect(self.click_clear_all)    
        self.ui.ac_bt_2.clicked.connect(self.click_clear_all)    
        self.ui.button_equal.clicked.connect(self.click_equal)
        self.ui.button_equal_2.clicked.connect(self.click_equal)
        self.ui.ans_bt.clicked.connect(self.click_ans)
        self.ui.ans_bt_2.clicked.connect(self.click_ans)
        
        self.ui.root_bt.clicked.connect(self.click_root)
        self.ui.exp_bt.clicked.connect(self.click_exp)
        self.ui.factorial_bt.clicked.connect(self.click_fact)
        self.ui.left_pr_bt.clicked.connect(self.click_open_paren)
        self.ui.right_pr_bt.clicked.connect(self.click_close_paren)
        self.ui.sin_bt.clicked.connect(self.click_sin)
        self.ui.cos_bt.clicked.connect(self.click_cos)
        self.ui.tan_bt.clicked.connect(self.click_tan)

    def s_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.simple_page)

    def a_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.advanced_page)

    def h_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.history_page)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_0:
            self.click_bt0()
        elif key == Qt.Key_1:
            self.click_bt1()
        elif key == Qt.Key_2:
            self.click_bt2()
        elif key == Qt.Key_3:
            self.click_bt3()
        elif key == Qt.Key_4:
            self.click_bt4()
        elif key == Qt.Key_5:
            self.click_bt5()
        elif key == Qt.Key_6:
            self.click_bt6()
        elif key == Qt.Key_7:
            self.click_bt7()
        elif key == Qt.Key_8:
            self.click_bt8()
        elif key == Qt.Key_9:
            self.click_bt9()
        elif key == Qt.Key_Plus:
            self.click_add()
        elif key == Qt.Key_Minus:
            self.click_sub()
        elif key == Qt.Key_Asterisk:
            self.click_multi()
        elif key == Qt.Key_Slash:
            self.click_div()
        elif key == Qt.Key_Backspace:
            self.click_clear()
        elif key == Qt.Key_Return or key == Qt.Key_Enter:
            self.click_equal()
        elif key == Qt.Key_Escape:
            self.click_clear_all()

    # Show buttons in label
    def click_bt0(self):
        MainWindow.label+='0'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt1(self):
        MainWindow.label+='1'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt2(self):
        MainWindow.label+='2'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt3(self):
        MainWindow.label+='3'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt4(self):
        MainWindow.label+='4'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt5(self):
        MainWindow.label+='5'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt6(self):
        MainWindow.label+='6'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt7(self):
        MainWindow.label+='7'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt8(self):
        MainWindow.label+='8'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_bt9(self):
        MainWindow.label+='9'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_add(self):
        MainWindow.label+='+'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_sub(self):
        MainWindow.label+='-'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_multi(self):
        MainWindow.label+='*'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_div(self):
        MainWindow.label+='/'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_clear(self):
        MainWindow.label = MainWindow.label[:-1]
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_clear_all(self):
        MainWindow.label = ""
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_open_paren(self):
        MainWindow.label += '('
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_close_paren(self):
        MainWindow.label += ')'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_exp(self):
        MainWindow.label += '**'
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_root(self):
        MainWindow.label += '√('
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_sin(self):
        MainWindow.label += 'sin('
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_cos(self):
        MainWindow.label += 'cos('
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_tan(self):
        MainWindow.label += 'tan('
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_fact(self):
        MainWindow.label += 'factorial('
        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

    def click_ans(self):
        # Append the last result to the label if it's available
        if self.last_result:
            MainWindow.label += self.last_result
            self.ui.screen.setText(MainWindow.label)
            self.ui.screen_2.setText(MainWindow.label)



    def click_equal(self):
        req = MainWindow.label
        # Replace custom operators with their Python equivalents
        req = req.replace('√', 'math.sqrt')
        req = req.replace('sin', 'math.sin')
        req = req.replace('cos', 'math.cos')
        req = req.replace('tan', 'math.tan')
        req = req.replace('factorial', 'math.factorial')

        try:
            MainWindow.label = str(eval(req))
            self.last_result = MainWindow.label
        except:
            print("Syntax Error")
        
        # Show old methods
        MainWindow.history.update({req: MainWindow.label})

        # Show calculation method in dictionary at history screen
        last_key = list(MainWindow.history)[-1]
        MainWindow.history_text += f"{str(last_key)} = {MainWindow.history[last_key]}\n"

        self.ui.history.setText(MainWindow.history_text)

        self.ui.screen.setText(MainWindow.label)
        self.ui.screen_2.setText(MainWindow.label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MainWindow()
    player.show()
    sys.exit(app.exec())

