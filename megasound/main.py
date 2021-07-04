import kivy
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import get_color_from_hex
from kivy.uix.screenmanager import ScreenManager, Screen

from uix.uix import *

class HomeScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass


Window.size = (320, 600)

class ToonPlay(MDApp):
    def build(self):
        self.title = 'Toon Play'
        self.theme_cls.primary_palette = 'Indigo'
        self.theme_cls.accent_palette = 'BlueGray'
        self.theme_cls.accent_hue = '100'
        self.background = get_color_from_hex('#170b24')
        self.primary = get_color_from_hex('#211263')
        self.delete = get_color_from_hex('#FF3B30')
        self.secondary = get_color_from_hex('#7f93aa')
        self.theme_cls.theme_style = 'Dark'
        screens = [
            HomeScreen(name='home')
        ]

        self.wm = WindowManager()
        for screen in screens:
            self.wm.add_widget(screen)

        return self.wm

if __name__ == '__main__':
    ToonPlay().run()
    