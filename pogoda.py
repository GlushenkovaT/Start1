from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from colorama import init
from colorama import Fore , Back ,Style
init()

owm = OWM('2fc91aabb72c9b1f371ba4445fad8aaa')
mgr = owm.weather_manager()

place = input ("В каком городе/стране?:")
print (Back.RED)

observation = mgr.weather_at_place('Kyiv,UA')
w = observation.weather
temp = w.temperature('celsius') ['temp']


print (" В городе" + place + "сейчс" + w.detailed_status)
print (Back.BLUE)
print ("Температура сейчас в районе" + str(temp))
print (Back.YELLOW)

if temp < 10:
	print ("Сейчас норм")
elif temp <20:
	print ("Сейчас холодно оденься теплее")
else:
	print ("Температура норм одевай что угодно")

