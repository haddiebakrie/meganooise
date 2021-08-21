import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition, CardTransition
from kivy.utils import platform
import os
from mutagen import File
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image
from io import BytesIO
from kivy.core.image import Image as CoreImage
from kivymd.utils.fitimage import FitImage
from kivy.core.audio import SoundLoader

from uix.uix import *
from screens.screen import *
from kivy.properties import StringProperty

# if platform == 'android':
#     from android.storage import primary_external_storage_path
#     from android import loadingscreen
#     loadingscreen.hide_loading_screen()
#     from android.permissions import request_permissions, Permission
#     request_permissions([Permission.WRITE_EXTERNAL_STORAGE])
#     from jnius import autoclass

class HomeScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

if platform != 'android':
    Window.size = (320, 600)

class ToonPlay(MDApp):
    c_singer = StringProperty('Oliver Rodrigo')
    c_image = StringProperty('default.jpg')
    c_track_name = StringProperty("Driver's License")
    def build(self):
        self.title = 'Toon Play'
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'BlueGray'
        self.theme_cls.accent_hue = '100'
        self.background = get_color_from_hex('#170b24')
        self.primary = get_color_from_hex('#241263')
        self.delete = get_color_from_hex('#FF3B30')
        self.secondary = get_color_from_hex('#7f93aa50')
        self.theme_cls.theme_style = 'Dark'
        self.sound = SoundLoader()
        self.has_audio = False
        self.shuffle = False
        self.song_list = {}
        screens = [
            HomeScreen(name='home'),
            MusicPlayerScreen(name='player')
        ]

        self.wm = WindowManager(transition=CardTransition(mode='push', direction='up'))
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
    
    def switch_screen(self, screen):
        # print(self.wm.screens)
        self.wm.transition.mode = 'pop'
        self.wm.transition.direction = 'down'
        self.wm.current = screen

    def on_start(self):
        if platform == 'android':
            # mediastore = autoclass('android.provider.MediaStore$Audio$Media')
            # md = mediastore()
            self.get_songs()
        self.song_list = self.get_songs_wn()
        self.all_data = []
        for song in self.song_list:
            data = {'time':'', 'image':'', 'track_name':'', 'singer':'', 'path':'', 'length':''}
            meta = File(song, easy=True)
            music_card = MusicCard()
            try:
                tag = ID3(song)
                raw_length = MP3(song).info.length
                # length = length[:4].replace('.', ':')
                if len(str(int(raw_length % 60))) == 1:
                    length = str(int(raw_length / 60)) + ':' + '0{0}'.format(str(int(raw_length % 60)))
                else:
                    length = str(int(raw_length / 60)) + ':' + '{0}'.format(str(int(raw_length % 60)))
                # :
                data['track_name'] = meta.tags['title'][0] if 'title' in meta.tags else 'Unknown'
                
                data['singer'] = meta.tags['artist'][0] if 'artist' in meta.tags else 'Unknown'
                data['time'] = length
                data['length'] = raw_length
                data['path'] = song
                if tag.getall('APIC:'):
                    apic = tag.get('APIC:').data
                    image = Image.open(BytesIO(apic))
                    idc = hash(meta.tags['title'][0])
                    image.save('data/cover/{0}.jpg'.format(meta.tags['title'][0].replace('.','').replace('|','')))
                    image = self.get_im(apic, 'jpg')
                    data['image'] = 'data/cover/{0}.jpg'.format(meta.tags['title'][0].replace('.','').replace('|',''))
                else:
                    data['image'] = 'data/cover/def.png'
                self.all_data.append(data)

                # print(len(data))
                # music_card.data = data
            except Exception as e:
                pass
        self.wm.screens[0].ids['scrn_manager'].screens[0].ids['music_scrl'].data = self.all_data

    def get_im(self, image_byt, ext):
        buf = BytesIO(image_byt)
        core = CoreImage(buf, ext=ext)
        return core.texture
        

    def get_songs_wn(self):
        song_list = {}
        song_dir = 'C:/Users/Haddy/Music/'
        for path, dirnames, filenames in os.walk(song_dir):
            # for path in paths:
            for filename in filenames:
                if filename.endswith('.mp3'):
                    full_path = os.path.join(path, filename)
                    song_list[full_path] = ''

        return song_list

    def get_songs(self):
        song_list = []
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Cursor = autoclass('android.database.Cursor')

        contentResolver = PythonActivity.mActivity
        uri = autoclass('android.provider.MediaStore$Audio$Media').EXTERNAL_CONTENT_URI

        cursor = contentResolver.getContentResolver().query(uri, None, None, None, None)

        if cursor is not None and cursor.moveToFirst():
            while cursor.moveToNext():
                title = cursor.getString(cursor.getColumnIndex('MediaStore.Audio.Media.TITLE'))  # retrieve songs title
                # path = cursor.getString(cursor.getColumnIndex('MediaStore.Audio.Media._data'))  # retrieve songs path

                song_list.append(title)

        cursor.close()

    def load_audio(self, path):
        if self.has_audio:
            self.sound.stop()
            self.has_audio = False
        self.sound = SoundLoader.load(path)
        self.has_audio = True

    def toggle_shuffle(self):
        if self.shuffle == True:
            self.shuffle = False
            return
        self.shuffle = True

    def open_player(self):
        self.wm.current = 'music-player'

if __name__ == '__main__':
    ToonPlay().run()