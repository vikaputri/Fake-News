import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from sklearn.externals import joblib

class MyGrid(Widget):
    title = ObjectProperty(None)
    author = ObjectProperty(None)
    isi = ObjectProperty(None)

    def btn(self):
        a = self.title.text
        b = self.author.text
        c = self.isi.text

        gabung = a+b+c
        filename = './pipeline.sav'
        loaded_model = joblib.load(filename)
        pred = loaded_model.predict([gabung])
        if (pred == [1]) :
           result = 'Real'
        elif (pred == [0]):
            result = 'Fake'
        else:
            result = 'Nothing'

        self.title.text = ""
        self.author.text = ""
        self.isi.text = ""
        self.hasil.text = result

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
