from kivy.lang.builder import Builder
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.properties import ObjectProperty, StringProperty
from kivy.animation import Animation
from kivymd.uix.card import MDCard

Builder.load_string(
"""
<NavDrawer>:
    type: 'standard'
    md_bg_color: app.primary
    elevation: 0
    opening_transition: 'linear'
    closing_transition: 'linear'

<NavListItem>:
    size_hint_y: None
    height: '70dp'
    spacing: '20dp'
    md_bg_color: [0, 0, 0, 0]
    elevation: 0
    padding: '10dp'
    MDIcon:
        icon: root.icon
        size_hint_x: None
        width: self.texture_size[0]
    MDLabel:
        text: root.text
"""
)

class NavDrawer(MDNavigationDrawer):
    bg = ObjectProperty()
    cbg = ObjectProperty()

    def resize_screen(self):
        if self.state == 'close':
            bg_anim = Animation(padding = (0, 30, 0, 30), d=.2, t='linear')
            cbg_anim = Animation(radius = (20, 20, 20, 20), d=.2, t='linear')
            self.bg.size_hint = (None, None)
            bg_anim.start(self.bg)
            cbg_anim.start(self.cbg)
            self.set_state('open')
        else:
            bg_anim = Animation(padding = (0, 0, 0, 0), d=.2, t='linear')
            cbg_anim = Animation(radius = (0, 0, 0, 0), d=.2, t='linear')
            bg_anim.start(self.bg)
            cbg_anim.start(self.cbg)
            self.set_state('close')
            if not bg_anim.have_properties_to_animate:
                self.bg.size_hint = (1, 1)

class NavListItem(MDCard):
    icon = StringProperty('android')
    text = StringProperty('Android')
