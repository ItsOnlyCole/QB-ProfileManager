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

# Reads in profiles.xml
xml = open("/home/itsonlycole/.config/QB-ProfileManager/profiles.xml", "r")
message = xml.readlines()
# Removes closing tag parent and adds new child
length = len(message)
message.pop(length-1)
message.append("  <profile>"+profileName+"</profile>\n")
# print(message)
message.append("</profiles>")
xml.close()
# Writes changes to profiles.xml
xml = open("/home/itsonlycole/.config/QB-ProfileManager/profiles.xml", "w")
xml.writelines(message)
xml.close()
