import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(500,500,500,500)
   b.move(50,20)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())

def main():
    """
    Initilize gui
    maybe put greeting
    """

    exit = False

    while not exit:
        # in here put the main code that will repeat as long as the user wants
        ...
        """
        return and closing logic statements
        
        if user_input = "return":
            continue
        
        elif user_input = "exit":
            exit = True
        
        """

    """
    maybe add final goodbye
    """

if __name__ == '__main__':
    window()
    main()