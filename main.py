# encoding: utf-8
import kivy
kivy.require('1.8.0')
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.clock import Clock, mainthread
# hacer post y get a la api
from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp

class Acceso(App):
	@mainthread
	def reqError(self,req, Ret):
		print(u'Error en la conexión al servidor')
		print(Ret)
		content=Label(text=u'Error en la conexión al servidor')
		popup = Popup(
			title='Mensaje', 
			content=content,
			size_hint=(1,1.0/3.0),
		)
		popup.open()
		
	@mainthread
	def reqFail(self,req, Ret):
		print(u'Error al realizar la petición')
		print(Ret)
		content=Label(text=u'Error al realizar la petición')
		popup = Popup(
			title='Mensaje', 
			content=content,
			size_hint=(1,1.0/3.0),
		)
		popup.open()
		
	@mainthread
	def tokenListo(self,ins):
		print(u'+++ +++')
		req_body = '{"TKN":"ECHO"}'
		
		headers = {
			'Content-Type':'application/json'
		}
		
		print(self.baseurl +'/api/echo')
		print(u'Body:',req_body)
		req = UrlRequest(
			url = self.baseurl +'/api/echo', 
			on_success = self.envioCred,
			on_error = self.reqError, # comment for avoid crash
			on_failure = self.reqFail, 
			decode = True,
			req_body = req_body,
			verify = False,
			req_headers = headers
		)
	@mainthread
	def envioCred(self,req,Ret):
		print(u'+++ +++')
		print(u'Ret: ',Ret,req)
		if Ret['R'] == 200:
			content=Label(text=u'Done')
			popup = Popup(
				title='Alerta', 
				content=content,
				size_hint=(1,1.0/3.0)
			)
			popup.open()
			
	def salir(self,ins):
		App.get_running_app().stop()
			
		
	def build(self,**kw):
		self.baseurl = 'https://144.202.34.148'
		self.tknn = ''
		S = dp(10)
		
		layout = BoxLayout(
			orientation='vertical',
			padding = [S,S,S,S]
		)
		
		btnok = Button(
			text='Access',
			font_size='20sp'
		)
		btnexit = Button(
			text='Exit',
			font_size='20sp'
		)
		
		##########################
		control = BoxLayout(orientation='horizontal')
		control.add_widget(btnok)
		control.add_widget(btnexit)
		##########################
		layout.add_widget(Widget())
		layout.add_widget(control)
		layout.add_widget(Widget())
		
		btnok.bind(on_press=self.tokenListo)
		btnexit.bind(on_press=self.salir)
		
		
		return layout

if __name__ == '__main__':
	M = Acceso()
	M.run()
