from kivy.lang.builder import Builder
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.properties import ObjectProperty, StringProperty
from kivy.animation import Animation
from kivymd.uix.card import MDCard
from kivy.clock import Clock

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
    height: '50dp'
    spacing: '20dp'
    md_bg_color: [0, 0, 0, 0]
    elevation: 0
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
            Clock.schedule_once(self.remove_hint, .2)
        
    def remove_hint(self, dt):
        self.bg.size_hint=(1, 1)

class NavListItem(MDCard):
    icon = StringProperty('android')
    text = StringProperty('Android')
