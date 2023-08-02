# Aelia - Welpike (https://github.com/AeliaDev/name-generator)

from utils import *

# Ascii art generated with : https://patorjk.com/software/taag
print(" _   _                                                        _             \n"
      "| \ | |                                                      | |            \n"
      "|  \| | __ _ _ __ ___   ___    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ \n"
      "| . ` |/ _` | '_ ` _ \ / _ \  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|\n"
      "| |\  | (_| | | | | | |  __/ | (_| |  __/ | | |  __/ | | (_| | || (_) | |   \n"
      "|_| \_|\__,_|_| |_| |_|\___|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   \n"
      "                              __/ |                                         \n"
      "                             |___/                 v2.0.0   by Aelia (Welpike)")


err = ""
name_length = 0
name_number = 0

while name_length <= 0:
    try:
        name_length = int(input("Enter the number of syllables for the name : "))
    except ValueError:
        err = "The number of syllables must be an integer."
    else:
        if name_length <= 0:
            err = "The number of syllables must be positive."
    print(err)

while name_number <= 0:
    try:
        name_number = int(input("Enter the number of names that you want : "))
    except ValueError:
        err = "The number of names must be an integer."
    else:
        if name_number <= 0:
            err = "The number of syllables must be positive."
    print(err)


names = generate_name(name_length, name_number)

for name in names:
    print(name)
    save_data("data/generated.txt", name)

print("Names saved")
