from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder

Builder.load_string(
"""
<SearchFieldHalf>:
    size_hint_y: None
    height: '35dp'
    md_bg_color: app.secondary
    radius: '20dp', 0, 0, '20dp'
    elevation: 0
    padding: '10dp', 0, '5dp', 0
    MDIcon:
        icon: 'magnify'
        font_size: '20sp'
        halign: 'center'
        size_hint_x: None
        size: ('20dp', '20dp')
    TextInput:
        height: '40dp'
        size_hint_y: None
        background_color: [0, 0, 0, 0]
        cursor_color: [1, 1, 1, 1]
        multiline: False
        font_size: '20dp'
        foreground_color: [1, 1, 1, 1]
        pos_hint: {'center_y':.5}

<SearchField>:
    size_hint_y: None
    height: '40dp'
    md_bg_color: app.secondary
    radius: '20dp', '20dp', '20dp', '20dp'
    elevation: 0
    padding: '10dp', 0, '10dp', 0
    MDIcon:
        icon: 'magnify'
        font_size: '20sp'
        halign: 'center'
        size_hint_x: None
        size: ('20dp', '20dp')
    TextInput:
        id: txt_input
        height: '40dp'
        size_hint_y: None
        background_color: [0, 0, 0, 0]
        cursor_color: [1, 1, 1, 1]
        multiline: False
        foreground_color: [1, 1, 1, 1]
        pos_hint: {'center_y':.5}
    IconBtn:
        icon: 'close'
        disabled: True if txt_input.text == '' else False
        on_release: 
            txt_input.text = ''
            txt_input.focus = True
"""
)

class SearchFieldHalf(MDCard):
    pass

class SearchField(MDCard):
    pass