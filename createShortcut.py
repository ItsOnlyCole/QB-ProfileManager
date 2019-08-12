import sys
import os

profileName = ""
# shortcutLocation = '~/.local/share/applications/qutebrowser-'
# ###Add a way to use the current user instead of setting a primary user only
shortcutLocation = '/home/itsonlycole/.local/share/applications/qutebrowser-'
index = 0

for eachArg in sys.argv:
    if index == 0:
        index += 1
        continue
    profileName = profileName + eachArg
    index += 1

shortcutLocation += profileName + ".desktop"

if os.path.exists(shortcutLocation):
    os.remove(shortcutLocation)

shortcut = open(shortcutLocation, "w")

shortcut.write("[Desktop Entry]\n")
shortcut.write("Name=Qutebrowser-"+profileName+"\n")
shortcut.write("Comment=QuteBrowser profile for "+profileName+"\n")
shortcut.write("Exec=qutebrowser -B .config/qutebrowser-"+profileName+"\n")
# shortcut.write("Icon=ICONLOCATION")
shortcut.write("Terminal=false\n")
shortcut.write("Type=Application\n")
shortcut.write("Categories=Network;")
