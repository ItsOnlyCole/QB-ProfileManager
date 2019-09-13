#Attaching the ui to python code using this tutorial https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
import sys
from PyQt5 import QtWidgets, uic

profilesFile = "/home/itsonlycole/.config/QB-ProfileManager/profiles.xml"

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() #Calls the inherited classes __init__ method
        uic.loadUi('mainUI.ui', self) #Loads the .ui file

        self.profilesList = self.findChild(QtWidgets.QListWidget, 'profilesListWidget')
        
        self.show() #Shows the gui

    #def loadProfilesList(profiles):
        #self.profilesList.clear()
        #for profile in profiles:
            #self.profilesList.addItem(profile)

def createProfilesArray(file):
    profilesXML = open(file, "r")
    profilesText = profilesXML.readlines()
    profilesList = []
    #profilesLength = len(profilesText)
    for profile in profilesText:
        profilesList.append(profile)
    return profilesList

app = QtWidgets.QApplication(sys.argv) #Creates an instance of QtWidgets.QApplication
window = Ui() #Creates an instance of our class
profiles = createProfilesArray(profilesFile)
window.profilesList.clear()
for profile in profiles:
    window.profilesList.addItem(profile)
app.exec_()
