# main.py

from notes_manager import NotesManager

def print_menu():
    print("-------------------------")
    print("1. Создать новую заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Сохранить заметки в файл")
    print("5. Загрузить заметки из файла")
    print("6. Вывести заметку по ID")
    print("7. Вывести все заметки")
    print("8. Выйти")
    print("-------------------------")

def main():
    notes_manager = NotesManager()


if __name__ == "__main__":
    main()