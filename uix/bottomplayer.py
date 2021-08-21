from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ObjectProperty, ListProperty
from kivy.lang.builder import Builder

Builder.load_string(
"""
<BottomPlayer>:
    app: app
    size_hint: None, None
    height: '60dp'
    width: '250dp'
    pos_hint: {'right':1}
    radius: '30dp', 0, 0, 0
    md_bg_color: app.primary
    padding: '10dp'
    spacing: '5dp'
    play_icn: play_icn
    FitImage:
        id: image
        radius: 20,
        source: app.c_image
        pos_hint: {'center_x':.5, 'center_y':.5}
        size_hint: None, None
        height: '30dp'
        width: '30dp'
    MDBoxLayout:
        orientation: 'vertical'
        adaptive_height: True
        pos_hint: {'center_y':.5}
        spacing: '5dp'
        MDLabel:
            text: root.app.c_track_name
            bold: True
            size_hint_y: None
            height: self.texture_size[1]
            shorten_from: 'right'
            shorten: True
        MDLabel:
            text: root.app.c_singer
            font_size: '12sp'
            size_hint_y: None
            height: self.texture_size[1]
            bold: True
            shorten_from: 'right'
            shorten: True
    AnimatedPlayButton:
        id: play_icn
        icon: 'play'
        pos_hint: {'center_y':.5}

<AnimatedPlayButton@IconBtn>:
    md_bg_color: app.primary
    length: 80
    font_size: '20sp'
    canvas.before:
        Color:
            rgba: app.secondary
        Line:
            ellipse: self.pos[0]-1, self.pos[1]-1, self.size[0] + 2, self.size[1] + 2, 0, 360
            width: 1.1
        Color: 
            rgba: [1, 1, 1, 1]
        Line:
            ellipse: self.pos[0]-1, self.pos[1]-1, self.size[0] + 2, self.size[1] + 2, 0, root.length
            width: 1.1
                

"""
)

class BottomPlayer(MDCard):
    track_name = StringProperty('Tell me why')
    singer = StringProperty('The Kid Laroi')
    time = StringProperty('3:86')
    image = StringProperty('default.jpg')
    active = BooleanProperty(defaultvalue=False)
    play_icn = ObjectProperty()
    pressed = ListProperty([0, 0])

    def on_touch_down(self, touch):
        if self.play_icn.collide_point(*touch.pos):
            self.play_icn.on_press()
            self.app.open_player()
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True

            return super(BottomPlayer, self).on_touch_down(touch)
        return super(BottomPlayer, self).on_touch_down(touch)

