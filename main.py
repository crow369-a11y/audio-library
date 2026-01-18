# main.py

from io_handler import load_records
from reports import report_all_sorted, report_by_artist, report_by_year_range


def print_records(records, title):
    """Выводит список записей в виде таблицы."""
    if not records:
        print("Нет данных для отображения.")
        return

    print(f"\n=== {title} ===")
    print(f"{'Исполнитель':<20} {'Трек':<30} {'Альбом':<25} {'Год':<6} {'Длит.':<8} {'Просл.':<12}")
    print("-" * 95)
    for r in records:
        print(
            f"{r.artist:<20} {r.title:<30} {r.album:<25} {r.year:<6} {r.duration_sec:<8} {r.plays:<12}")


def main():
    records = load_records()
    if not records:
        print("Программа завершена из-за ошибки загрузки данных.")
        return

    while True:
        print("\n=== Медиатека ===")
        print("1. Все треки (исполнитель ↑, год ↓, прослушивания ↓)")
        print("2. Треки конкретного исполнителя")
        print("3. Треки по диапазону лет")
        print("4. Выход")

        choice = input("Выберите пункт (1–4): ").strip()

        if choice not in ("1", "2", "3", "4"):
            print("Некорректный выбор. Пожалуйста, введите 1, 2, 3 или 4.")
            continue  # возвращаемся в начало цикла

        if choice == "1":
            result = report_all_sorted(records)
            print_records(result, "Все аудиозаписи")

        elif choice == "2":
            artist = input("Введите имя исполнителя: ").strip()
            result = report_by_artist(records, artist)
            if result is None:
                print("Исполнитель не найден.")
            else:
                print_records(result, f"Треки исполнителя: {artist}")

        elif choice == "3":
            try:
                start = int(input("Год начала: "))
                end = int(input("Год окончания: "))
                if start > end:
                    print("Год начала не может быть больше года окончания.")
                    continue
                result = report_by_year_range(records, start, end)
                if result is None:
                    print("Нет треков в указанном диапазоне.")
                else:
                    print_records(result, f"Треки с {start} по {end} год")
            except ValueError:
                print("Ошибка: введите корректные числа.")

        elif choice == "4":
            print("Наслаждайтесь музыкой!")
            break

        else:
            print("Некорректный выбор. Пожалуйста, введите 1, 2, 3 или 4.")


if __name__ == "__main__":
    main()
