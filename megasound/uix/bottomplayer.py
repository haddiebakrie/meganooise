from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivy.lang.builder import Builder

Builder.load_string(
"""
<BottomPlayer>:
    size_hint: None, None
    height: '70dp'
    width: '250dp'
    pos_hint: {'right':1}
    radius: '35dp', 0, 0, 0
    md_bg_color: app.primary
    padding: '10dp'
    spacing: '5dp'
    FitImage:
        id: image
        radius: 20,
        source: root.image
        pos_hint: {'center_x':.5, 'center_y':.5}
        size_hint: None, None
        height: '40dp'
        width: '40dp'
    MDBoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        pos_hint: {'center_y':.5}
        spacing: '5dp'
        MDLabel:
            text: root.track_name
            bold: True
            size_hint_y: None
            height: self.texture_size[1]
        MDLabel:
            text: root.singer
            font_size: '12sp'
            size_hint_y: None
            height: self.texture_size[1]
            bold: True
    AnimatedPlayButton:
        icon: 'play'

<AnimatedPlayButton@MDIconButton>:
    md_bg_color: app.primary
    user_font_size: '15sp'
    length: 80
    size: 15, 15
    size_hint: None, None
    canvas.before:
        Color:
            rgba: app.secondary
        Ellipse:
            size: self.size[0] + 4, self.size[1] + 4
            pos: self.pos[0]-2, self.pos[1]-2
        Color: 
            rgba: [1, 1, 1, 1]
        Line:
            ellipse: self.pos[0]-2, self.pos[1]-2, self.size[0] + 4, self.size[1] + 4, 0, root.length
            width: 1.1
                

"""
)

class BottomPlayer(MDCard):
    track_name = StringProperty('Tell me why')
    singer = StringProperty('The Kid Laroi')
    time = StringProperty('3:86')
    image = StringProperty('default.jpg')
    active = BooleanProperty(defaultvalue=False)