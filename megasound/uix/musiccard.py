from kivy.lang.builder import Builder
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty, BooleanProperty

Builder.load_string(
"""
<MusicCard>:
    size_hint_y: None
    height: '50dp'
    md_bg_color: [0, 0, 0, 1]
    anchor: 'right'
    elevation: 0
    max_opened_x: '50dp'
    MDCardSwipeLayerBox:        
        MDCard:
            md_bg_color: [1, 0, 0, 1]
            orientation: 'vertical'
            MDIcon:
                id: trash
                icon: 'delete-outline'
                halign: 'right'
                padding: '10dp', 0
                md_bg_color: [0, 0, 0, 0]
                md_bg_color_disabled: [0, 0, 0, 0]
    MDCardSwipeFrontBox:
        MDCard:
            padding: '5dp', '5dp'
            spacing: '5dp'
            md_bg_color: app.background
            elevation: '1dp'
            MDIcon:
                icon: 'equal'
                font_size: '15sp'
                size_hint_x: None
                width: self.texture_size[1]
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
                MDIcon: 
                    icon: 'align-vertical-bottom' if root.active == True else ''
                    pos_hint: {'center_x':.5,  'center_y':.5}
                    size_hint: None, None
                    size: self.texture_size
            MDBoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: root.track_name
                    bold: True
                MDLabel:
                    text: root.singer
                    font_size: '12sp'
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
            padding: '5dp', '5dp'
            spacing: '5dp'
            md_bg_color: app.background
            elevation: '1dp'
            MDIcon:
                icon: 'equal'
                font_size: '15sp'
                size_hint_x: None
                width: self.texture_size[1]
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
                MDIcon: 
                    icon: 'align-vertical-bottom' if root.active == True else ''
                    pos_hint: {'center_x':.5,  'center_y':.5}
                    size_hint: None, None
                    size: self.texture_size
            MDBoxLayout:
                orientation: 'vertical'
                MDLabel:
                    text: root.track_name
                    bold: True
                MDLabel:
                    text: root.singer
                    font_size: '12sp'
            Label:
                text: root.time
                size_hint_x: None
                size: self.texture_size
                bold: True  
            MDIconButton:
                icon: 'close'
                user_font_size: '18sp'
                halign: 'center'
                size_hint_x: None
                size: ('20dp', '20dp')
                md_bg_color: [0, 0, 0, 0]
                md_bg_color_disabled: [0, 0, 0, 0]


"""
)

class MusicCard(MDCardSwipe):
    track_name = StringProperty('Tell me why')
    singer = StringProperty('The Kid Laroi')
    time = StringProperty('3:86')
    image = StringProperty('default.jpg')
    active = BooleanProperty(defaultvalue=False)

class MusicCardPlaylist(MDCardSwipe):
    track_name = StringProperty('Tell me why')
    singer = StringProperty('The Kid Laroi')
    time = StringProperty('3:86')
    image = StringProperty('default.jpg')
    active = BooleanProperty(defaultvalue=False)