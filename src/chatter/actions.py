from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
import requests
import json


'''

class ActionWeather(Action):
	def name(self):
		return 'action_weather'
		
	def run(self, dispatcher, tracker, domain):
		from apixu.client import ApixuClient
		api_key = 'db6af0e0da0d45f3b03155500182009' #your apixu key
		client = ApixuClient(api_key)
		
		loc = tracker.get_slot('location')
		current = client.getCurrentWeather(q=loc)
		
		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)
						
		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]


Table 
 - customer
 - position
 - quantity
 '''


class FetchNRisky(Action):
	def name(self):
		return 'fetch_n_risky'

	def run(self, dispatcher, tracker, domain):

		request = {'table':'table_name','position':'quantity','customer':'customer_name','quantity':1}


		table = tracker.get_slot('Table')
		position= tracker.get_slot('position')
		quantity = tracker.get_slot('quantity')
		customer = tracker.get_slot('customer')

		PARAMS = {'table':table,'position':position,'customer':quantity,'quantity':customer} 
		URL = 'http://192.168.1.1:3000/contracts'
		# requests.get()
		
		# query_response = requests.
		r = requests.get(url = URL, params = PARAMS) 
		data = r.json()

		response = """Ok, got it! Here are the customers {} """.format(data['customers'])

		dispatcher.utter_message(response)
		return [SlotSet('Table',table),SlotSet('position',position),SlotSet('quantity',quantity),SlotSet('customer_name',customer_name)]

class FetchRiskScore(Action):
	def name(self):
		return 'fetch_risk_scores'

	def run(self, dispatcher, tracker, domain):

		request = {'table':'table_name','position':'quantity','customer':'customer_name','quantity':1}


		table = tracker.get_slot('Table')
		position= tracker.get_slot('position')
		quantity = tracker.get_slot('quantity')
		customer = tracker.get_slot('customer')


		# requests.get()
		
		# query_response = requests.
		response = """Ok, got it!\n  request['table'] = {} request['position'] = {} request['quantity'] = {} request['customer'] ={}""".format(table, position, quantity, customer)

		dispatcher.utter_message(response)
		return [SlotSet('Table',table),SlotSet('position',position),SlotSet('quantity',quantity),SlotSet('customer_name',customer)]