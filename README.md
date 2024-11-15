# rephrasewt
Программа на Python, которая упростит замену фраз на кастомные в WT

# Программа для замены фраз в файле CSV

Это простая программа на Python, которая меняет некоторые фразы в текстовом файле формата CSV.

## Установка Python

1. **Скачать Python:**
   - Перейдите на [официальный сайт Python](https://www.python.org/).
   - Нажмите на кнопку "Downloads".
   - Выберите версию Python для вашей операционной системы (Windows, macOS, Linux) и скачайте установщик.

2. **Установка Python:**
   - Запустите скачанный установщик.
   - Убедитесь, что установлен флажок "Add Python to PATH".<details><summary>Картинка где ставить галочку</summary>![alt text](https://github.com/Chu4hel/rephrasewt/assets/106600877/78f68a40-ea4c-4c61-8f6d-3e2ce5c58af4)</details>
   - Нажмите "Install Now" и следуйте инструкциям установщика.
   - После установки откройте терминал (Command Prompt в Windows, Terminal в macOS и Linux) и выполните команду `python --version` для проверки установки.
(Для windows - сочетание клавиш CTRL + R . Затем нужно ввести в открывшееся окно "cmd"

## Клонирование репозитория

1. **Склонируйте репозиторий:**
   - Нажмите на кнопку "Clone or download" вверху этой страницы.
   - Скопируйте URL репозитория.
   - Откройте терминал и выполните команду `git clone <URL>` (вставьте скопированный URL).

   Или просто [скачайте ZIP архив](https://github.com/Chu4hel/rephrasewt/archive/refs/heads/main.zip) и распакуйте его.

## Создание файла конфигурации

1. **Откройте текстовый редактор:**
   - Например, Notepad на Windows, TextEdit на macOS, или любой другой редактор по вашему выбору.

2. **Создайте файл `config.py`:**
   - В репозитории найдите файл `config.py` и скопируйте его в ту же директорию.

3. **Настройте пути и фразы:**
   - Откройте файл `config.py` в редакторе и измените пути к файлам и фразы для замены по вашему усмотрению.
   - Сохраните изменения.

Пример содержимого файла `config.py`:
   ```python
   # config.py

   # Путь к папке игры
   MENU_FILE_PATH = "C:\Games\WarThunder" #Измените на свой

   # Фразы для замены
   REPLACE_PHRASES = {
       "В бой": "В боль",
       "уничтожен": "анигилирован", # После последнего элемента должна стоять запятая
       # Добавьте остальные фразы по аналогии
       # Регистр имеет значение!
   }
```

## Запуск программы

1. **Откройте терминал:**

   - **В Windows:** нажмите `Win + R`, введите `cmd`, нажмите Enter.
   - **В macOS:** откройте Launchpad -> Другие -> Терминал.
   - **В Linux:** откройте любой терминал по вашему выбору.

2. **Перейдите в директорию с программой:**

   - Используйте команду `cd путь_к_папке`, чтобы перейти в директорию, где находится склонированный репозиторий.

3. **Запустите скрипт:**
    
   - Выполните команду `python main.py`.
      - Если в config.blk добавлена нужная строка, то программа прочтет `menu.csv`, заменит фразы согласно настройкам в `config.py` и сохранит изменения в `menu.csv`.
      - Иначе программа сама добавит в config.blk нужную строку.
         - После этого вам нужно перезайти в игру и заново запустить скрипт.

4. **Проверьте результат:**

   - Откройте файл `menu.csv` в текстовом редакторе и убедитесь, что фразы были заменены.
   - Или просто зайдите в игру и наслаждайтесь.

    
## ВАЖНО!
После каждого обновления (микропатча) возможно названия бронетехники/ивентов/наград сломаются. <br>
В этом случае вам необходимо удалить папку lang в файлах игры, затем перезайти в War Thunder и заново запустить скрипт.
   
