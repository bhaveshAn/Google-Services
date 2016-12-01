from kivy.app import App 
from kivy.lang import Builder
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition


'''class GoogleScreen(Screen):
	pass
class ServiceScreen(Screen):
	pass

class QueryScreen(Screen):
        def goto(self,text):
                print('Hello %s has been inserted'%(text))
        def search_query(self,value):
                print('Its a %s query'%(value))'''

class ScreenManagement(ScreenManager):
	pass

'''class RootWidget(FloatLayout):
	pass'''
present=Builder.load_file("assets/kivy_files/googleservices.kv")


class GoogleServicesApp(App):
	"""docstring for GoogleServices"""
	'''def __init__(self, arg):
		super(GoogleServices, self).__init__(**args)
		self.arg = arg'''
	def build(self):
		return present

if __name__ == '__main__':
	GoogleServicesApp().run()

