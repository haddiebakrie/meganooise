from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from uix.musiccard import MusicCard

Builder.load_string(
"""
<MusicScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        TopBarMenu:
            nav: root.nav
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: playlist_lbl.height + playlist_scrl.height + 30
            MDLabel:
                id: playlist_lbl
                text: 'Playlist'
                size_hint_y: None
                height: self.texture_size[1]
                bold: True
                padding: '10dp', 0
            MDBoxLayout:
                adaptive_height: True
                padding: '10dp', '10dp', 0, '10dp'
                ScrollView:
                    id: playlist_scrl
                    do_scroll_x: True
                    do_scroll_y: False
                    size_hint_y: None
                    bar_width: 0
                    MDGridLayout:  
                        id: playlist_grid
                        adaptive_width: True 
                        spacing: '5dp'
                        rows: 1
                        SizedPlaylistCard:
                            image: 'data/cover/Abu Dhabi.jpg'
                            name: 'My Locals'
                        SizedPlaylistCard:
                            image: 'data/cover/Drake - Toosie Slide.jpg'
                            name: 'Dance'
                        SizedPlaylistCard:
                            image: 'data/cover/Bird Set Free.jpg'
                            name: 'Study Musics'
                        SizedPlaylistCard:
                            image: 'data/cover/Toxic (feat Adekunle Gold) [Prod by Sess]  NetNaijacom.jpg'
                            name: 'Afro Dance'
                        SizedPlaylistCard:
                            image: 'data/cover/Yekpa.jpg'
                            name: '2021'
                        SizedPlaylistCard:
                            image: 'data/cover/Six Feet Under.jpg'
                            name: 'Sad and Slow'
                        SizedPlaylistCard:
                            image: 'data/cover/If the World Was Ending (Ft Julia Michaels).jpg'
                            name: 'Study Music'
        MDBoxLayout:
            orientation: 'vertical'
            height: '50dp'
            size_hint_y: None
            MDBoxLayout:
                padding: '10dp', 0
                MDLabel:
                    text: 'Music'
                    bold: True
                IconBtn:
                    icon: 'filter-variant'
        MDBoxLayout:
            padding: '5dp', 0, 0, '10dp'
            RecycleView:
                id: music_scrl
                do_scroll_x: False
                do_scroll_y: True
                bar_width: 0
                viewclass: 'MusicCard'
                RecycleBoxLayout:  
                    id: music_grid
                    default_size_hint_y: None
                    height: self.minimum_height
                    spacing: '5dp'
                    orientation: 'vertical'
                    size_hint_y: None       
                    default_size: self.width, None             
                    
    BottomPlayer:

<SizedPlaylistCard@PlaylistCard>:                    
    size_hint: None, None
    radius: 10, 
    font_size: '12sp'
"""
)

class MusicScreen(Screen):
    nav = ObjectProperty()
    music_grid = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)