import sys
import os
import jdk
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui import Ui_MainWindow
from PySide6.QtGui import QIcon

def java_install(ver, add_path=False):
    try:
        jdk.install(ver)
        path = os.path.expanduser("~") + "\\.jdk"
        java_path = os.path.join(path, os.listdir(path)[0])
        if add_path:
            os.system(f'chcp 65001 & setx JAVA_HOME {java_path} & setx "Path" "%Path%;%JAVA_HOME%\\bin" /m')
        return 0
    except Exception as e:
        return e

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.install_java)
        self.ui.comboBox.addItems(["6", "8", "11", "17", "21"])
    
    def install_java(self):
        ver = self.ui.comboBox.currentText()
        add_path = True
        error = java_install(ver, add_path)
        if error == 0:
            QMessageBox.information(self, "Success", "Installation Complete.", QMessageBox.Yes)
        else:
            QMessageBox.critical(self, "Error", "Unable to install.\n{error}", QMessageBox.Yes)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    icon = QIcon("icon.ico")
    w.setWindowIcon(icon)
    w.show()
    app.exec()
