#Attaching the ui to python code using this tutorial https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
import sys
from os.path import expanduser, exists
from os import mkdir
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() #Calls the inherited classes __init__ method
        uic.loadUi('mainUI.ui', self) #Loads the .ui file
        self.profilesList = self.findChild(QtWidgets.QListWidget, 'profilesListWidget')
        self.show() #Shows the gui

def generateProfilesXML(file):
    xml = open(file, "w")
    xmlMessage = ""
    xmlMessage.append("<profiles>\n")
    xmlMessage.append("  <profile>Default</profile>\n")
    xmlMessage.append("</profiles>")
    xml.writelines(xmlMessage)
    xml.close()

def defineProfilesLocation():
    user = expanduser('~')
    dir = user + "/.config/QB-ProfileManager"
    file = user + "/.config/QB-ProfileManager/profiles.xml"
    if exists(dir)=="false":
        mkdir(dir)
        print("QB-ProfileManager Folder made")
    if exists(file)=="false":
        generateProfilesXML(file)
        print("profiles.xml made")
    return file

def createProfilesList(file):
    profilesXML = open(file, "r")
    profilesText = profilesXML.readlines()
    profilesList = []
    profilesTextLength = len(profilesText)
    profilesTextLength -= 1
    profilesText.pop(0)
    profilesText.pop(profilesTextLength-1)
    for profile in profilesText:
        profilesList.append(profile[11:-11])
    return profilesList

app = QtWidgets.QApplication(sys.argv) #Creates an instance of QtWidgets.QApplication
window = Ui() #Creates an instance of our class
profilesFile=defineProfilesLocation()
profiles = createProfilesList(profilesFile)
window.profilesList.clear()
for profile in profiles:
    window.profilesList.addItem(profile)
app.exec_()
