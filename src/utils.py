from genpw import pronounceable_passwd
from random import randint


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines


def save_data(file_name, data):
    with open(file_name, "a+", encoding='utf-8') as file:
        file.write(f"\n{data}")


def generate_name(size=6, names_number=10):
    names = []
    for _ in range(names_number):
        name = pronounceable_passwd(size)

        if len(name) != size:
            continue
        names.append(name)
    return names
