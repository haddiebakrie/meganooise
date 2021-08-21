from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_string(
"""
<TopBarMenu>:
    size_hint_y: None
    height: '50dp' 
    spacing: '50dp'
    padding: '20dp', '5dp', 0, 0
    IconBtn:   
        icon: 'sort-variant'
        md_bg_color: app.secondary
        pos_hint: {'center_y':.5}
        on_release: 
            root.nav.resize_screen()
            
    
    SearchFieldHalf:

<TopBarBack>:
    padding: '10dp', '5dp', 0, 0
    size_hint_y: None
    height: '50dp' 
    spacing: '50dp'
    MDIconButton:   
        icon: 'chevron-left'
        md_bg_color: app.secondary
        padding: 0    
    SearchFieldHalf:

<TopBarSelected>:
    padding: '10dp', '5dp', 0, 0
    size_hint_y: None
    height: '50dp' 
    spacing: '10dp'
    selected: '0'
    MDIconButton:   
        icon: 'chevron-left'
        md_bg_color: app.secondary
        padding: 0
    
    MDLabel: 
        text: "{0} selected item".format(root.selected)
        halign: 'center'
        bold: True
    
    MDCheckbox:
        size_hint: None, None
        size: '40dp', '40dp'
        group: 'selection'
        selected_color: [1, 1, 1, 1]
"""
)


class TopBarMenu(MDBoxLayout):
    pass


class TopBarBack(MDBoxLayout):
    pass

class TopBarSelected(MDBoxLayout):
    pass