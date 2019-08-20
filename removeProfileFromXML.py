import sys

# Assigns Profile Name Argument to Variable
profileName = ""
index = 0
for eachArg in sys.argv:
    if index == 0:
        index += 1
        continue
    profileName = profileName + eachArg
    index += 1

profileToRemove = "  <profile>" + profileName + "</profile>\n"
# Reads in profiles.xml
xml = open("/home/itsonlycole/.config/QB-ProfileManager/profiles.xml", "r")
message = xml.readlines()
# Resets index for for-loop
index = 0
for profile in message:
    if profile == profileToRemove:
        message.pop(index)
        break
    index += 1
xml.close()
# Writes changes to profiles.xml
xml = open("/home/itsonlycole/.config/QB-ProfileManager/profiles.xml", "w")
xml.writelines(message)
xml.close()
