# models

class AudioRecord:
    """
    Представляет одну аудиозапись.
    Поля: artist, title, album, year, duration_sec, plays.
    """

    def __init__(self, artist, title, album, year, duration_sec, plays):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = int(year)
        self.duration_sec = int(duration_sec)
        self.plays = int(plays)
