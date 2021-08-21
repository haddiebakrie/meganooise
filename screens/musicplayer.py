from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, DictProperty, StringProperty, NumericProperty, BooleanProperty, OptionProperty
from kivymd.uix.slider import MDSlider
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from random import randint


Builder.load_string(
"""
#:import get_color_from_hex kivymd.theming.get_color_from_hex

<MusicPlayerScreen>:
    app: app
    slider: slider
    FitImage:
        id: cover
        source: root.data['image']
        size_hint_y: None
        height: root.height - play_card.height
        pos_hint: {'top':1}
        opacity: .6
    FitImage:
        source: 'shadow2.png'
        size_hint_y: None
        height: cover.height
        pos_hint: {'top':1}
    MDBoxLayout:
        orientation: 'vertical'
        spacing: '10dp'
        MDBoxLayout:
            padding: '10dp'
            adaptive_height: True
            IconBtn:
                icon: 'chevron-down'
                md_bg_color: app.secondary
                on_release:
                    app.switch_screen('home')
        MDBoxLayout:
            orientation: 'vertical'
            spacing: '5dp'
            MDLabel:
                text: root.data['track_name']
                font_size: '28sp'
                bold: True
                size_hint_y: None
                height: self.texture_size[1]
                bold: True
                padding: '15dp', 0
                halign: 'center'

            MDLabel:
                text: root.data['singer']
                size_hint_y: None
                height: self.texture_size[1]
                padding: '15dp', 0
                font_size: '20sp'
                halign: 'center'
                opacity: .8
        MDBoxLayout:
            height: '90dp'
            size_hint_y: None
            MDFloatLayout:
                size_hint_y: None
                height: '80dp'
                MDBoxLayout:
                    pos_hint: {'center_y':.5, 'center_x':.5}
                    padding: '27dp', 0
                    MDBoxLayout:
                        md_bg_color: get_color_from_hex('#7f93aaf0')
                        radius: '10dp'    
                MDBoxLayout:
                    size_hint_y: None
                    padding: '21dp', 0
                    height: '75dp'
                    pos_hint: {'y':0, 'center_x':.5}
                    MDBoxLayout:
                        radius: '10dp'
                        md_bg_color: get_color_from_hex('#7f93aaf9')
                MDBoxLayout:
                    height: '70dp'
                    padding: '15dp', 0
                    size_hint_y: None
                    pos_hint: {'y':0, 'center_x':.5}
                    MDBoxLayout:
                        radius: '10dp'
                        md_bg_color: app.background
                        padding: 0, '10dp'
                        MusicCardNormal:
                            image: root.data['image']
                            track_name: root.data['track_name']
                            singer: root.data['singer']
                            time: root.data['time']

        MDBoxLayout: 
            id: play_card
            md_bg_color: [0, 0, 0, 1]
            height: '160dp'
            size_hint_y: None
            MDBoxLayout:
                radius: '20dp', '20dp', 0, 0
                md_bg_color: app.background
                orientation: 'vertical'
                MDFloatLayout:
                    size_hint_y: None
                    height: play_icon.height
                    MDBoxLayout:
                        padding: '20dp', 0
                        pos_hint: {'center_y':.5, 'center_x':.5}
                        IconBtn:
                            icon: 'skip-previous'
                            font_size: '40dp'
                            on_release:
                                root.prev_music()
                        Widget:
                        IconBtn:
                            id: play_icon
                            icon: 'pause' if root.is_playing == True else 'play'
                            font_size: '55dp'
                            on_press:
                                root.play()
                        Widget:
                        IconBtn:
                            icon: 'skip-next'
                            font_size: '40dp'
                            on_release:
                                root.next_music()
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: '20dp', 0
                    MDSlider:
                        id: slider
                        color: [1, 1, 1, 1]
                        max: float(str(int(root.data['length']/60)) + '.' + str(int(root.data['length'] % 60)))
                        padding: 0, 0
                        height: '20dp'
                        size_hint_y: None
                        hint: False
                        show_off: False
                    MDBoxLayout:
                        adaptive_height: True
                        MDLabel:
                            text: '{0}:{1}'.format(str(slider.value)[0], str(slider.value)[2:4])
                            # text: str(slider.max)
                            size_hint_y: None
                            height: self.texture_size[1]
                            font_size: '12sp'
                        MDLabel:
                            text: str(root.data['time'])
                            halign: 'right'
                            size_hint_y: None
                            height: self.texture_size[1]
                            font_size: '12sp'
                    MDBoxLayout:
                        MDIconButton:
                            icon: 'shuffle'
                            on_release:
                                app.toggle_shuffle()
                        Widget:
                        MDIconButton:
                            icon: 'playlist-plus'
                        Widget:
                        MDIconButton:
                            icon: 'alarm-snooze'
                        Widget:
                        MDIconButton:
                            icon: 'format-list-bulleted'
                            
"""
)

class MusicPlayerScreen(Screen):
    data = DictProperty(defaultvalue={'time':'', 'image':'', 'track_name':'', 'singer':'', 'path':'', 'length':0}) 
    is_playing = BooleanProperty(defaultvalue=False)
    repeat = OptionProperty('none', options=['all', 'one', 'none'])
    app = ObjectProperty()

    def on_enter(self):
        if not self.app.has_audio:
            self.app.load_audio(self.data['path'])
            self.play()
            self.app.c_track_name = self.data['track_name']
            self.app.c_image = self.data['image']
            self.app.c_singer = self.data['singer']
            
    def play(self):
        if self.is_playing:
            self.app.sound.stop()
            self.is_playing = False
        else:
            self.app.sound.play()
            self.is_playing = True
            self.seek = Clock.schedule_interval(lambda x:self.update_slider(), 1)

    def update_slider(self):
        if self.slider.value == self.slider.max: 
            self.is_done()
            return
        self.slider.value = self.get_sound_pos()

    def get_sound_pos(self):
        sound_pos = self.app.sound.get_pos() 
        if len(str(int(sound_pos % 60))) != 1:
            sound_pos = float(str(int(sound_pos/60)) + '.' + str(int(sound_pos % 60)))
        else:
            sound_pos = float(str(int(sound_pos/60)) + '.' + '0{0}'.format(str(int(sound_pos % 60))))

        return sound_pos


    def on_touch_up(self, touch):
        if self.slider.collide_point(*touch.pos):
            # self.app.sound.play()
            m, sec = str(self.slider.value).split('.')
            print(m, sec[0:2], self.slider.value)
            mins = int(m)*60
            secs = float(sec[0:2])
            self.app.sound.seek(mins+secs)
            self.update_slider()
        super().on_touch_up(touch)

    def next_music(self):
        if self.app.shuffle:
            index = self.shuffle()
            self.data = self.app.all_data[index]
            self.app.load_audio(self.data['path'])
            self.is_playing = False
            self.play()
            return
        index = self.app.all_data.index(self.data)
        self.data = self.app.all_data[index+1]
        self.app.load_audio(self.data['path'])
        self.is_playing = False
        self.play()

    def prev_music(self):
        index = self.app.all_data.index(self.data)
        self.data = self.app.all_data[index-1]
        self.app.load_audio(self.data['path'])
        self.is_playing = False
        self.play()
    
    def is_done(self):
        self.app.sound.seek(0.0)
        self.slider.value = 0.0
        self.is_playing = False
        if self.repeat == 'none':
            self.next_music()

    def shuffle(self):
        index = randint(0, len(self.app.all_data))
        return index
