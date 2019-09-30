#Attaching the ui to python code using this tutorial https://nitratine.net/blog/post/how-to-import-a-pyqt5-ui-file-in-a-python-gui/
import sys
from os.path import expanduser, exists
from os import mkdir, rmdir, remove
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() #Calls the inherited classes __init__ method
        uic.loadUi('mainUI.ui', self) #Loads the .ui file
        self.profilesList = self.findChild(QtWidgets.QListWidget, 'profilesListWidget')
        self.removeProfileButton = self.findChild(QtWidgets.QPushButton, 'removeProfileButton')
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

def loadProfiles():
    profilesFile=defineProfilesLocation()
    profiles = createProfilesList(profilesFile)
    window.profilesList.clear()
    for profile in profiles:
        window.profilesList.addItem(profile)

def removeProfile(profile):
    #Checks if default Profile and if so, cancel and display popup stating that default can't be deleted. (maybe add an option to do fresh default profile instead.
    user = expanduser('~')
    profileDir = user + "/.config/qutebrowser-" + profile
    profileShortcut = user + "/.local/share/applications/qutebrowser-" + profile + ".desktop"
    rmdir(profileDir)
    remove(profileShortcut)
    removeProfileFromXML(profile)
    loadProfiles()
    #create Popup stating profile is deleted
    ###END-OF-Function###

def removeProfileFromXML(profile):
    profileToRemove = "  <profile>" + profile + "</profile>\n"
    user = expanduser('~')
    xmlFile = user + ".config/QB-ProfileManager/profiles.xml"
    xml = open(xmlFile, "r")
    profilesList = xml.readlines()
    index = 0
    for profile in profilesList:
        if profile == profileToRemove:
            profilesList.pop(index)
            break
        index += 1
    xml.close()
    xml = open(xmlFile, "w")
    xml.writeLines(profilesList)
    xml.close()

app = QtWidgets.QApplication(sys.argv) #Creates an instance of QtWidgets.QApplication
window = Ui() #Creates an instance of our class
loadProfiles()
app.exec_()
removeProfile("TestProfile")
