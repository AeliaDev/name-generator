# Aelia - Welpike

from utils import (read_file, save_data, handle_lines, generate_name)

# Ascii art generated with : https://patorjk.com/software/taag
print(" _   _                                                        _             \n"
      "| \ | |                                                      | |            \n"
      "|  \| | __ _ _ __ ___   ___    __ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ \n"
      "| . ` |/ _` | '_ ` _ \ / _ \  / _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|\n"
      "| |\  | (_| | | | | | |  __/ | (_| |  __/ | | |  __/ | | (_| | || (_) | |   \n"
      "|_| \_|\__,_|_| |_| |_|\___|  \__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   \n"
      "                              __/ |                                         \n"
      "                             |___/                        by Aelia (Welpike)")

try:
    language = input("Enter the language of the syllables (en, fr) : ")
except:
    language = "en"

try:
    name_length = int(input("Enter the number of syllables for the name : "))
except:
    name_length = 3

name = generate_name(
    handle_lines(
        read_file(f"data/syllables_{language}.txt"),
        language
    ),
    name_length,
    language
)

print("\nGenerated : " + name + "\n")

save_data("data/generated.txt", f"{language} - {name} - {name_length}")

print("Saved")