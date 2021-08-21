from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.uix.behaviors import ButtonBehavior


Builder.load_string(
"""
<FAB>:
    size_hint: None, None
    size: '50dp', '50dp'
    radius: '50dp'
    md_bg_color: app.primary
    ripple_behavior: True
    IconBtn:
        icon: root.icon
        size: '50dp', '50dp'
        ripple_behavior: False

<IconButton>:
    size_hint_y: None
    height: '50dp'
    radius: '25dp'
    md_bg_color: app.primary
    ripple_behavior: True
    orientation: 'vertical'
    MDBoxLayout:
        adaptive_width: True
        pos_hint: {'center_x': .5}
        spacing: '5dp'
        IconBtn:
            icon: root.icon
        Label:
            text: root.text
            width: self.texture_size[0]
            size_hint_x: None
            bold: True

<ButtonBottom>:
    size_hint_y: None
    height: '50dp'
    radius: '25dp', '25dp', 0, 0
    md_bg_color: app.primary
    ripple_behavior: True
    orientation: 'vertical'
    MDLabel:
        text: root.text
        bold: True
        halign: 'center'
"""
)

class FAB(MDCard, ButtonBehavior):
    icon = StringProperty('plus')
    def on_release(self):
        print('HI')

class IconButton(MDCard, ButtonBehavior):
    icon = StringProperty('plus')
    text = StringProperty('Action text')
    def on_release(self):
        print('HI')

class ButtonBottom(MDCard, ButtonBehavior):
    text = StringProperty('Save')
    def on_release(self):
        print('HI')