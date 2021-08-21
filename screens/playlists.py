from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, DictProperty, StringProperty

Builder.load_string(
"""
<PlaylistsScreen>:
    MDBoxLayout:
        orientation: 'vertical'
        TopBarMenu:
            nav: root.nav
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: playlist_lbl.height + 20
            MDLabel:
                id: playlist_lbl
                text: 'Playlist'
                size_hint_y: None
                height: self.texture_size[1]
                bold: True
                padding: '10dp', '10dp'
        MDBoxLayout:
            ScrollView:
                id: playlists_scrl
                do_scroll_x: False
                do_scroll_y: True
                bar_width: 0
                MDGridLayout:  
                    id: playlist_grid
                    adaptive_height: True 
                    spacing: '5dp'
                    padding: '10dp', 0
                    cols: 1
                    PlaylistsCard:
                        image: 'data/cover/Abu Dhabi.jpg'
                        name: 'My Locals'
                    PlaylistsCard:
                        image: 'data/cover/Drake - Toosie Slide.jpg'
                        name: 'Dance'
                    PlaylistsCard:
                        image: 'data/cover/Bird Set Free.jpg'
                        name: 'Study Musics'
                    PlaylistsCard:
                        image: 'data/cover/Toxic (feat Adekunle Gold) [Prod by Sess]  NetNaijacom.jpg'
                        name: 'Afro Dance'
                    PlaylistsCard:
                        image: 'data/cover/Yekpa.jpg'
                        name: '2021'
                    PlaylistsCard:
                        image: 'data/cover/Six Feet Under.jpg'
                        name: 'Sad and Slow'
                    PlaylistsCard:
                        image: 'data/cover/If the World Was Ending (Ft Julia Michaels).jpg'
                        name: 'Study Music'

    BottomPlayer:
    FAB:
        pos_hint: {'right':.95, 'y':.12}

<PlaylistsCard@PlaylistCard>:
    height: '200dp'
    font_size: '20sp'
            
"""
)

class PlaylistsScreen(Screen):
    nav = ObjectProperty()