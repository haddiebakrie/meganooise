from kivy.lang.builder import Builder
from kivymd.uix.card import MDCardSwipe, MDCard
from kivy.properties import StringProperty, BooleanProperty, ObjectProperty, DictProperty, NumericProperty
from screens.musicplayer import MusicPlayerScreen

Builder.load_string(
"""
<MusicCard>:
    app: app
    ripple_behavior: True
    size_hint_y: None
    height: '50dp'
    md_bg_color: [0, 0, 0, 1]
    anchor: 'right'
    elevation: 0
    max_opened_x: '50dp'
    type_swipe: 'hand'
    # width: 5
    # size_hint_x: None
    MDCardSwipeLayerBox:        
        MDCard:
            md_bg_color: app.delete
            orientation: 'vertical'
            elevation: 0
            MDIcon:
                id: trash
                icon: 'delete-outline'
                halign: 'right'
                padding: '10dp', 0
                md_bg_color: [0, 0, 0, 0]
                md_bg_color_disabled: [0, 0, 0, 0]
    MDCardSwipeFrontBox:
        elevation: 0
        MDCard:
            padding: '5dp', '5dp'
            spacing: '5dp'
            md_bg_color: app.background
            elevation: 0
            ripple_behavior: True

            MDIcon:
                icon: 'drag-horizontal-variant'
                font_size: '15sp'
                size_hint_x: None
                width: self.texture_size[1]
            MDFloatLayout:
                id: fl
                size_hint: None, None
                width: '40dp'
                height: '40dp'
                pos_hint: {'center_y':.5}
                FitImage:
                    id: image
                    radius: 20,
                    source: root.image
                    pos_hint: {'center_x':.5, 'center_y':.5}
                    opacity: .5 if root.active == True else 1
                    size_hint_y: None
                    height: '40dp'
                IconBtn: 
                    icon: 'align-vertical-bottom' if root.active == True else ''
                    pos_hint: {'center_x':.5,  'center_y':.5}
                    size_hint: None, None
                    font_size: '20dp'
                    ripple_behavior: False
            MDBoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: root.track_name
                    bold: True
                    shorten: True
                    shorten_from: 'right'
                MDLabel:
                    text: root.singer
                    font_size: '12sp'
                    shorten: True
                    shorten_from: 'right'
            Label:
                text: root.time
                size_hint_x: None
                size: self.texture_size
                bold: True

<MusicCardPlaylist>:
    size_hint_y: None
    height: '50dp'
    md_bg_color: [0, 0, 0, 1]
    anchor: 'right'
    elevation: 0
    max_opened_x: '50dp'
    type_swipe: 'auto'
    MDCardSwipeLayerBox:        
    MDCardSwipeFrontBox:
        MDCard:
            ripple_behavior: True
            padding: '5dp', '5dp'
            spacing: '5dp'
            md_bg_color: app.background
            elevation: '1dp'
            IconBtn:
                icon: 'drag-horizontal-variant'
                font_size: '20dp'
                size_hint_x: None
                pos_hint: {'center_y':.5}
            MDFloatLayout:
                size_hint: None, None
                width: '40dp'
                height: '40dp'
                pos_hint: {'center_y':.5}
                FitImage:
                    id: image
                    radius: 20,
                    source: root.image
                    pos_hint: {'center_x':.5, 'center_y':.5}
                    opacity: .5 if root.active == True else 1
                    size_hint_y: None
                    height: '40dp'
                IconBtn: 
                    icon: 'align-vertical-bottom' if root.active == True else ''
                    pos_hint: {'center_x':.5,  'center_y':.5}
                    size_hint: None, None
                    font_size: '20dp'
                    ripple_behavior: False
            MDBoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: root.track_name
                    bold: True
                    shorten: True
                    shorten_from: 'right'
                MDLabel:
                    text: root.singer
                    font_size: '12sp'
                    shorten: True
                    shorten_from: 'right'
            Label:
                text: root.time
                size_hint_x: None
                size: self.texture_size
                bold: True  
            IconBtn:
                icon: 'close'
                font_size: '20dp'
                halign: 'center'
                size_hint_x: None
                md_bg_color: [0, 0, 0, 0]
                md_bg_color_disabled: [0, 0, 0, 0]
                pos_hint: {'center_y':.5}

<MusicCardNormal>:
    padding: '10dp', '5dp'
    spacing: '5dp'
    md_bg_color: app.background
    elevation: '1dp'
    ripple_behavior: True
    MDFloatLayout:
        size_hint: None, None
        width: '40dp'
        height: '40dp'
        pos_hint: {'center_y':.5}
        FitImage:
            id: image
            radius: 20,
            source: root.image
            pos_hint: {'center_x':.5, 'center_y':.5}
            opacity: .5 if root.active == True else 1
            size_hint_y: None
            height: '40dp'
        IconBtn: 
            icon: 'align-vertical-bottom' if root.active == True else ''
            pos_hint: {'center_x':.5,  'center_y':.5}
            size_hint: None, None
            font_size: '20dp'
            ripple_behavior: False
    MDBoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: root.track_name
            bold: True
            shorten: True
            shorten_from: 'right'
        MDLabel:
            text: root.singer
            font_size: '12sp'
            shorten: True
            shorten_from: 'right'
    Label:
        text: root.time
        size_hint_x: None
        size: self.texture_size
        bold: True  
"""
)

class MusicCard(MDCardSwipe):
    time = StringProperty()
    image = StringProperty()
    track_name = StringProperty()
    singer = StringProperty()
    path = StringProperty()
    length = NumericProperty()
    active = BooleanProperty(defaultvalue=False)
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if (touch.time_end - touch.time_start) > .5:
                self.open_card()
                return True
            self.load_music()
         
        return super().on_touch_up(touch)
    
    def load_music(self):
        self.dat = {'time':self.time, 'image':self.image, 'track_name':self.track_name, 'singer':self.singer, 'path':self.path, 'length':self.length,}
        music_player = MusicPlayerScreen(name='music-player')
        music_player.data = self.dat
        music_player.name = 'music-player'
        self.app.wm.transition.mode = 'push'
        self.app.wm.transition.direction = 'up'
        if self.app.wm.has_screen('music-player'):
            self.app.wm.remove_widget(self.app.wm.get_screen('music-player'))
            self.app.wm.add_widget(music_player)
            self.app.wm.current = 'music-player'
            return
        self.app.wm.add_widget(music_player)
        self.app.wm.current = 'music-player'        

class MusicCardPlaylist(MDCardSwipe):
    track_name = StringProperty('Tell me why')
    singer = StringProperty('The Kid Laroi')
    time = StringProperty('3:86')
    image = StringProperty('data/cover/def.png')
    active = BooleanProperty(defaultvalue=False)

class MusicCardNormal(MDCard):
    track_name = StringProperty('Tell me why')
    singer = StringProperty('The Kid Laroi')
    time = StringProperty('3:86')
    image = StringProperty('data/cover/def.png')
    active = BooleanProperty(defaultvalue=False)