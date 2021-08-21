from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, DictProperty, StringProperty

Builder.load_string(
"""
<PlaylistScreen>:
    FitImage:
        source: root.cover
        size_hint_y: None
        height: root.height / 2
        pos_hint: {'top':1}
        opacity: .6
    MDBoxLayout:
        orientation: 'vertical'
        TopBarBack:
        MDBoxLayout:
            orientation: 'vertical'
            padding: 0, '50dp', 0, 0
            MDIconButton:
                icon: 'camera-plus'
                pos_hint: {'center_x':.5}
                user_font_size: '30dp'
                opacity: 0
                disabled: True
            MDBoxLayout:
                spacing: '5dp'
                padding: '5dp'
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '5dp'
                    MDLabel:
                        text: root.name
                        font_size: '28sp'
                        bold: True
                        size_hint_y: None
                        height: self.texture_size[1]
                        bold: True
                        padding: '15dp', 0

                    MDLabel:
                        text: '{0} tracks'.format(root.song_count)
                        size_hint_y: None
                        height: self.texture_size[1]
                        padding: '15dp', 0
                        # bold: True
                        font_size: '15sp'

                MDIconButton:
                    icon: 'pencil'
                    opacity: 0
                    disabled: True
                    md_bg_color: app.secondary
                IconBtn:
                    font_size: '20dp'
                    icon: 'dots-vertical'
                    md_bg_color: app.secondary

            MDFloatLayout:
                size_hint_y: None
                height: root.height/2 + dp(70)
                MDBoxLayout:
                    radius: '40dp', 0, 0, 0
                    md_bg_color: app.secondary
                MDBoxLayout:
                    radius: '40dp', 0, 0, 0
                    size_hint_y: None
                    md_bg_color: app.background
                    height: root.height/2 + dp(40)
                    padding: '10dp', '15dp', '5dp', 0
                    MDBoxLayout:
                        ScrollView:
                            id: music_scrl
                            do_scroll_x: False
                            do_scroll_y: True
                            bar_width: 0
                            MDGridLayout:  
                                id: playlist_grid
                                adaptive_height: True 
                                spacing: '5dp'
                                cols: 1
                                MusicCard:
                                    active: True
                                MusicCard:
                                MusicCard:
                                MusicCard:
                                MusicCard:
                                MusicCard:
                                MusicCard:
                                MusicCard:
                                MusicCard:
                                MusicCard:

"""
)

class PlaylistScreen(Screen):
    playlist = DictProperty() 
    cover = StringProperty('default.jpg')
    name = StringProperty('My Songs')
    song_count = StringProperty('23')