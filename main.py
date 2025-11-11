import re
import requests

TIME_PATTERN = re.compile(r'\b(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b')


def get_time(text):
    """Возвращает список всех корректных времен в тексте"""
    return re.findall(TIME_PATTERN, text)


def check_time(time_str):
    """Проверяет, является ли строка корректным временем"""
    return bool(re.fullmatch(TIME_PATTERN, time_str))


def search_in_file(file_path):
    """Поиск времени в загруженном файле"""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return get_time(content)


def search_in_url(url):
    """Поиск времени на веб-странице"""
    response = requests.get(url)
    if response.status_code == 200:
        return get_time(response.text)
    else:
        print("Ошибка загрузки страницы:", response.status_code)
        return []


def main():
    print("Выберите режим работы:")
    print("1 — Проверить введённое время")
    print("2 — Найти корректное время в файле")
    print("3 — Найти корректное время на веб-странице")

    choice = input("Введите номер режима: ")

    if choice == "1":
        time_str = input("Введите время (в формате ЧЧ:ММ:СС): ")
        if check_time(time_str):
            print("Время корректно!")
        else:
            print("Время некорректно.")

    elif choice == "2":
        file_path = input("Введите путь к файлу: ")
        times = search_in_file(file_path)
        print("Найденные значения времени:", ", ".join(times))

    elif choice == "3":
        url = input("Введите URL страницы: ")
        times = search_in_url(url)
        print("Найденные значения времени:", ", ".join(times))

    else:
        print("Неверный выбор режима!")


if __name__ == "__main__":
    main()
