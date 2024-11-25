from modules.instruments import Guitar, Piano, Drum, Instrument
from modules.song import Song
from modules.playlist import Playlist
from modules.utils import print_section_separator

import json

# 2.1.3. Fonction à compléter après avoir compléter le code de modules/instruments.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testInstruments():
  print_section_separator("Tests partie 2.1")

# TODO: Instancier un objet de la classe Instrument.
  try: 
     instrument = Instrument("fabriquant-inconnu")

  except TypeError :
     print("Impossible d'instancier un Instrument.")
   
# TODO: Instancier une Guitar du "fabricant-g", l'afficher, et appeler sa méthode play().
  guitare = Guitar("fabricant-g") 
  print(guitare)
  print(guitare.play())

# TODO: Instancier un Piano du "fabricant-p", l'afficher, et appeler sa méthode play().
  piano = Piano("fabricant-p")
  print(piano)
  print(piano.play())

  # TODO: Instancier un Drum du "fabricant-b", l'afficher, et appeler sa méthode play().
  drum = Drum("fabricant-b")
  print(drum)
  print(drum.play())


# 2.2.6. Fonction à compléter après avoir compléter le code de modules/song.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testSong():
  print_section_separator("Tests partie 2.2")

  # TODO: Instancier une Song appelée "Title", de l'artiste "Artist",
  #       sortie en 2024 et qui se joue avec une batterie du fabriquant "brand".
  #       Afficher l'instance créée.
  chanson_1 = Song('Title', 'Artist', 2024, 'Drum', 'brand')
  print(chanson_1)

  # TODO: Instancier une Song à partir d'un dictionnaire/objet vide (i.e. {}).
  #       Afficher l'instance créée.
  dictionnaire_vide = {}
  try:
    chanson_2 = Song.from_obj(dictionnaire_vide)
    print(chanson_2)
  except ValueError as e :
    print(f'ValueError, message: {e}')

  # TODO: Instancier une Song à partir de la 1ère chanson du fichier "data/songs.json"
  #       Afficher l'instance créée.
  data_1 = json.load(open("part2/data/songs.json"))[0]
  song_1 = Song.from_obj(data_1)
  print(song_1)


# 2.3.6. Fonction à compléter après avoir compléter le code de modules/playlist.py.
#        Les instructions détaillées sont dans le fichier README.md.
def testPlaylist():
  print_section_separator("Tests partie 2.3")

  # TODO: Instancier une Playlist nommée "Playlist-csv" depuis le fichier CSV data/songs.csv.
  playlist_csv = Playlist.from_csv(name = 'Playlist-cvs', csv_path = "/Users/mimiisuki/Desktop/projet-2-mimiisuki-main/part2/data/songs.csv")
  

  # TODO: Instancier une Playlist nommée "Playlist-json" depuis le fichier JSON data/songs.json.
  playlist_json = Playlist.from_json(name = 'Playlist-json', json_path = "/Users/mimiisuki/Desktop/projet-2-mimiisuki-main/part2/data/songs.json")
  
  # TODO:Ajouter un dictionnaire/objet vide (i.e. {}) à la playlist "Playlist-json".
  try:
    playlist_json += {}
  except TypeError as e :
    print(f'TypeError, message: {e}')
  
  # TODO: Ajouter les chansons de la playlist "Playlist-json" à la playlist "Playlist-csv".
  for song in  playlist_json:
    playlist_csv.__add__(song)

  # TODO: Retirer la chanson intitulée "We Will Rock You" de la playlist "Playlist-csv".
  playlist_csv.__sub__(song_title = 'We Will Rock You')

  # TODO: Jouer toutes les chansons de la playlist "Playlist-json" en mode normal.
  playlist_json.play_all(rdm_mode = False)

  #TODO: Jouer toutes les chansons de la playlist "Playlist-csv" en mode aléatoire.
  playlist_csv.play_all(rdm_mode = True)


if __name__ == "__main__":
  testInstruments()
  testSong()
  testPlaylist()