from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, BooleanProperty
from kivy.clock import Clock
from functools import partial

Builder.load_string(
"""
<PlaylistCard>:
    size_hint_y: None
    height: '100dp'
    width: '100dp'
    elevation: 0
    md_bg_color: [0, 0, 0, 0]
    radius: '10dp', 
    font_size: '15sp'
    MDFloatLayout:
        FitImage:
            radius: root.radius
            source: root.image
            pos_hint: {'center_x':.5, 'center_y':.5}
            opacity: .8

        MDCheckbox:
            pos_hint: {'right':.95, 'top':.9}
            size_hint: None, None
            size: '20dp', '20dp'
            selected_color: [1, 1, 1, 1]
            disabled: True if root.selection == False else False
            opacity: 0 if root.selection == False else 1
            checkbox_icon_down: 'checkbox-marked-circle'
            checkbox_icon_normal: 'checkbox-blank-circle-outline'
        MDLabel:
            text: root.name
            pos_hint: {'top':.2, 'x':.04}
            size_hint_y: None
            height: self.texture_size[1]
            # padding: '5dp', 0
            bold: True
            font_size: root.font_size
"""
)

class PlaylistCard(MDCard):
    name = StringProperty("Solo Musics")
    image = StringProperty('default.jpg')
    selection = BooleanProperty(defaultvalue=False)

    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if (touch.time_end - touch.time_start) > .5:
                self.selection = True
         
        return super().on_touch_up(touch)
