from modules.song import Song
from typing import Iterator, List, Dict
import csv, json, random

class Playlist:
    def __init__(self, name: str, songs: List[Song]):
        self.__name = name
        if not isinstance(songs, list):
            raise TypeError("songs doit être une liste d'objets Song.")
        self.__songs = {song.title: song for song in songs}

    
    @classmethod
    def from_csv(cls, name: str, csv_path: str):
        songs = []
        with open(csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for ligne in reader:
              try:
                  song = Song.from_obj(ligne)
                  songs.append(song)
              except ValueError as e : 
                  print(f"Erreur lors de la création de la chanson:{e}")
        return cls(name, songs)

    
    @classmethod
    def from_json(cls, name: str, json_path: str):
        songs = []
        with open(json_path, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for song_data in data:
              try:
                  song = Song.from_obj(song_data)
                  songs.append(song)
              except ValueError as e : 
                  print(f"Erreur lors de la création de la chanson:{e}")
        return cls(name, songs)
    
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name
        
    @property
    def songs(self) -> Dict[str, Song]:
        return self.__songs
    @songs.setter
    def songs(self, songs: List[Song]):
        self.__songs = {song.title: song for song in songs}

    def __iter__(self):
        return iter(self.__songs.values())
    
    def __add__(self,song):
        if isinstance(song, Song):
            self.__songs[song.title] = song
            return self
        else:
            raise TypeError (f"Impossible d'ajouter une chanson de type {type(song)}.")
        
    def __sub__(self, song_title: str):
        if song_title in self.__songs:
            del self.__songs[song_title]
            return Playlist(self.__name, list(self.__songs.values()))
        else:
            print(f"La chanson avec le titre '{song_title} n'est pas dans la playslist")
        return self
    
    def play_all(self, rdm_mode = False):
        mode = "aléatoire" if rdm_mode else "standard"
        print(f"Lecture de {self.__name} ({len(self.__songs)} chansons en mode {mode})")
        songs_list = list(self.__songs.values())
        if rdm_mode:
            random.shuffle(songs_list)
        for song in songs_list:
            song.play()