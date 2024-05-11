import csv

from NameSearch.search_csv_files import find_target_in_csv
from config import MENU_FILE_PATH, REPLACE_PHRASES, REPLACE_ENCYCLOPEDIA
from time import sleep


def replace_in_file(file_path, replace_dict):
    count_z = 0
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";", quotechar='"')
        rows = list(reader)

    for row in rows:
        for i in range(len(row)):
            for key, value in replace_dict.items():
                if key in row[i]:
                    row[i] = row[i].replace(key, value)
                    count_z += 1

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(rows)

    return count_z


def check_and_add_config(config_file):
    config_file += "\config.blk"
    # Строка для поиска
    target_string = "\n\ndebug{\n  testLocalization:b=yes\n}"
    # Переменная для хранения флага найденной строки
    found_target = False
    # Читаем содержимое файла
    with open(config_file, "r") as file:
        for line in file:
            if line.strip() == "testLocalization:b=yes":
                found_target = True
                break
    if found_target:
        print("Строка testLocalization присутствует в config.blk.")
        return True
    else:
        print("Строка testLocalization не найдена в config.blk.")
        with open(config_file, "a") as file:
            file.write(target_string)
        return False


def main():
    # file_path = MENU_FILE_PATH+"\lang"
    # find_target_in_csv(file_path, "Во время боя нажмите F1")
    # return
    deb = check_and_add_config(MENU_FILE_PATH)
    if deb:
        while True:
            menu = input(
                "\nМеню\n"
                "Напишите число и нажмите Enter\n"
                "1. Замена фраз в menu.csv (Пример: 'В бой', 'Попадание')\n"
                "2. Замена фраз в encyclopedia_tips.csv (Подсказки)\n"
                "0. Завершить программу\n"
                "Ожидание ввода: "
            )
            print("\n")
            if menu.isdigit():
                menu = int(menu)
            if menu == 1:
                count_z = replace_in_file(MENU_FILE_PATH + "\\lang\\menu.csv", REPLACE_PHRASES)
                print(f"Заменено {count_z} фраз")
            elif menu == 2:
                count_z = replace_in_file(MENU_FILE_PATH + "\\lang\\encyclopedia_tips.csv", REPLACE_ENCYCLOPEDIA)
                print(f"Заменено {count_z} фраз")
            elif menu == 0:
                print("Завершение программы...")
                sleep(3)
                exit(0)
            sleep(2)
    else:
        print("Перезайдите в игру, для появления папки lang.")
    sleep(5)


if __name__ == "__main__":
    main()
