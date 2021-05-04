from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import kivy.uix.label
import kivy.uix.widget

import os
from mostsim import find_images

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

    def selected(self, filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                           size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, filename):
        try:
            self.ids.image.source = filename[0]
        except:
            pass

        img_path1, img_path2 = find_images(filename[0])
        self.dismiss_popup()

        try:
            self.ids.image1.source = img_path1
        except:
            pass

        try:
            self.ids.image2.source = img_path2
        except:
            pass


class Main_Interface(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    Main_Interface().run()