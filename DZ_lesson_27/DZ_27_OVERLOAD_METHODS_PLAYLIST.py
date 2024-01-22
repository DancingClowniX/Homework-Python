class Track:
    def __init__(self, name: str, min: int, sec: int):
        self.name = name
        self.min = min
        self.sec = sec
    def __add__(self, other_track):#сложение треков
        if isinstance(other_track, Track):
            new_track_sec = self.sec + other_track.sec
            new_track_min = self.min + other_track.min
            if new_track_sec >= 60:
                sec = new_track_sec % 60
                add_min = new_track_sec // 60
                new_track_min = self.min + other_track.min + add_min
                new_track_sec = sec
            else:
                new_track_sec = self.sec + other_track.sec
                new_track_min = self.min + other_track.min
            return Track(f"Mashup", new_track_min, new_track_sec)
    def __sub__(self, other_track):
        if isinstance(other_track, Track):
            new_track_sec = self.sec - other_track.sec
            new_track_min = self.min - other_track.min
            if self.min > other_track.min:
                if self.sec < other_track.sec:
                    new_track_sec = 60-(other_track.sec-self.sec)
                    new_track_min = self.min-other_track.min-1
                elif self.sec > other_track.sec:
                    new_track_sec = self.sec-other_track.sec
                elif self.sec == other_track.sec:
                    new_track_sec = 0
                return Track(f"Mashup_minus", new_track_min, new_track_sec)
            else:
                if self.sec > other_track.sec:
                    new_track_sec = self.sec - other_track.sec
                    new_track_min = other_track.min - self.min
                elif self.sec < other_track.sec:
                    new_track_sec = other_track.sec - self.sec
                    new_track_min = other_track.min - self.min
                elif self.sec == other_track.sec:
                    new_track_sec = 0
                return Track(f"Mashup_minus", new_track_min, new_track_sec)

track_music1 = Track("Блёклый самурай",2,45)
track_music2 = Track("Лавандовый чай",1,34)
track_music3 = track_music1+track_music2
print(track_music3.name,track_music3.min,track_music3.sec)
track_music4 = track_music1-track_music2
print(track_music4.name,track_music4.min,track_music4.sec)