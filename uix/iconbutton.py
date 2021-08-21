from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard

Builder.load_string(
"""
<IconBtn>:
    size_hint: None, None
    size: icn.font_size+self.padding[0], icn.font_size+self.padding[1]
    radius: '20dp'
    icon: ''
    md_bg_color: [0, 0, 0, 0]
    elevation: 0
    font_size: '20dp'
    padding: '5dp', '5dp'
    ripple_behavior: True
    md_bg_color_disabled: [0, 0, 0, 0]
    disabled: False
    pos_hint: {'center_y':.5}
    MDIcon:
        id: icn
        icon: root.icon
        halign: 'center'
        font_size: root.font_size
        md_bg_color_disabled: root.md_bg_color_disabled
        disabled: root.disabled

"""
)

class IconBtn(MDCard):
    def on_press(self):
        print("IconButton")