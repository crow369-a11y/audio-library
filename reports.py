# reports.py

from quicksort import quicksort


def report_all_sorted(records):
    """Отчёт 1: все записи, сортировка: исполнитель ↑, год выпуска ↓, прослушивания ↓"""
    def compare(a, b):
        if a.artist != b.artist:
            return a.artist < b.artist
        if a.year != b.year:
            return a.year > b.year
        return a.plays > b.plays

    sorted_records = records[:]  # копия, чтобы не менять оригинал
    quicksort(sorted_records, compare)
    return sorted_records


def report_by_artist(records, artist_name):
    """Отчёт 2: треки конкретного исполнителя, сортировка: альбом ↓, название ↑"""
    filtered = [r for r in records if r.artist.lower() == artist_name.lower()]
    if not filtered:
        return None

    def compare(a, b):
        if a.album != b.album:
            return a.album > b.album
        return a.title < b.title

    quicksort(filtered, compare)
    return filtered


def report_by_year_range(records, start_year, end_year):
    """Отчёт 3: треки в диапазоне лет, сортировка: год выпуска ↓, исполнитель ↑"""
    filtered = [r for r in records if start_year <= r.year <= end_year]
    if not filtered:
        return None

    def compare(a, b):
        if a.year != b.year:
            return a.year > b.year
        return a.artist < b.artist

    quicksort(filtered, compare)
    return filtered
