#!/usr/bin/env python3
#Дебильный калькуляор

from colorama import Fore, Back, Style
from colorama import init
# use Colorama to make Termcolor work on Windows too
init()

print (Style.DIM)
print (Fore.BLACK)
print (Back.GREEN)

what = input ("Что будем делать(+,-) :")

print (Back.CYAN)

a = float (input ("Введи первое число : "))
b = float (input ("Введи второе число : "))

print (Back.RED)

if what == "+":
	c = a + b
elif what == "-":
	c = a - b	
else:
	print ("Неверная операция")

print ("Результат :" + str(c))

input ()
