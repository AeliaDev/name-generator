from random import randint


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def save_data(file_name, data):
    with open(file_name, "a+", encoding='utf-8') as file:
        file.write(f"\n{data}")


def handle_lines(lines, language):
    syllabus = {}
    if language == "fr":
        syllabus['consonants'] = lines[0].strip().split(',')
        syllabus['vowels'] = lines[1].strip().split(',')

    elif language == "en":
        syllabus['syllables'] = lines[0].strip().split(',')
    return syllabus


def generate_name(syllabus, name_length, language):
    name = ""
    for _ in range(name_length):
        if language == "fr":
            name += syllabus['consonants'][
              randint(0, len(syllabus['consonants']) - 1)
            ] + syllabus['vowels'][
              randint(0, len(syllabus['vowels']) - 1)
            ]
        elif language == "en":
            name += syllabus['syllables'][
              randint(0, len(syllabus['syllables']) - 1)
            ]
    return name
