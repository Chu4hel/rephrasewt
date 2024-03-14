import csv
from config import MENU_FILE_PATH, REPLACE_PHRASES
from time import sleep

def replace_in_file(file_path, replace_dict):
    file_path += "\lang\menu.csv"
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";", quotechar='"')
        rows = list(reader)

    for row in rows:
        for i in range(len(row)):
            for key, value in replace_dict.items():
                row[i] = row[i].replace(key, value)

    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(rows)

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
    deb = check_and_add_config(MENU_FILE_PATH)
    if deb:
        replace_in_file(MENU_FILE_PATH, REPLACE_PHRASES)
        print("Фразы успешно заменены")
    else:
        print("Перезайдите в игру, для появления папки lang.")
    sleep(5)

if __name__ == "__main__":
    main()
