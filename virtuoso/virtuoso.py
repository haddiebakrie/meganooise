import os
from kivy.core.audio import SoundLoader
from kivy.app import App
import mutagen
from mutagen.mp3 import MP3
from mutagen import File
from mutagen.easyid3 import EasyID3

class Virtuoso:
    _all_music = []
    def __init__(self, path_to_music):
        for path, name, files in os.walk(path_to_music):
            for file in files:
                full_path = os.path.join(path, file)
                self._all_music.append(full_path)

        meta = File(self._all_music[0], easy=True)
        print(meta.tags)

class G(App):
    def build(self):
        return

hakeem = Virtuoso('data/musics')

G().run()