from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/pramata_chatter')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-439564283745-440045126227-439969372628-9df0739b808eebb6e648a01212ffa342', #app verification token
							'xoxb-439564283745-440163421698-0rEDIyLgCp0Yd03rhExV7SLK', # bot verification token
							'sMZgQ9mQLtdnaesCeKm4hvRZ', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))