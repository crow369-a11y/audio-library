# io_handler.py
def load_records(filename="audio_library.csv"):
    """
    Читает файл audio_library.csv вручную через split(';').
    Возвращает список объектов AudioRecord.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка открытия файла: {e}")
        return []

    if not lines:
        print("Файл пуст.")
        return []

    records = []
    for line_num, line in enumerate(lines[1:], start=2):
        line = line.strip()
        if not line:
            continue

        parts = line.split(';')
        if len(parts) != 6:
            print(
                f"Предупреждение: строка {line_num} пропущена (ожидается 6 полей, получено {len(parts)})")
            continue

        # Убираем лишние пробелы вокруг каждого поля
        artist, title, album, year, duration_sec, plays = [
            p.strip() for p in parts]

        try:
            from models import AudioRecord
            record = AudioRecord(artist, title, album,
                                 year, duration_sec, plays)
            records.append(record)
        except Exception as e:
            print(f"Ошибка в строке {line_num}: {e}")
            continue

    return records
