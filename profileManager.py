#Attaching the ui to python code using this tutorial https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
import sys
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() #Calls the inherited classes __init__ method
        uic.loadUi('mainUI.ui', self) #Loads the .ui file

        self.profilesList = self.findChild(QtWidgets.QListWidget, 'profilesListWidget')
        self.profilesList.addItem('Test')
        self.profilesList.addItem('CoolerTest')
        
        self.show() #Shows the gui
app = QtWidgets.QApplication(sys.argv) #Creates an instance of QtWidgets.QApplication
window = Ui() #Creates an instance of our class
window.profilesList.addItem('Pickachu')
app.exec_()
