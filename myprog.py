name = input ("Введи свое имя :")
print ("Привет" + name)

m = float (input ("Введи свой вес: "))
h = float (input ("Введи свой рост в см :"))
h = h/100
index_mass = float (m/(h*h))

if float(index_mass) < 16:
	print ("Индек массы тела равен:","%.2f" % index_mass, "кг/м2", " и у Вас дефицит массы тела")
elif float(index_mass) >= 16 and float(index_mass)<=18.5 :
	print ("Индек массы тела равен:","%.2f" % index_mass, "кг/м2", "и у Вас недостаточная масса тела")
elif float (index_mass) >=18.5 and float (index_mass) <=24 :
	print ("Индек массы тела равен:","%.2f" % index_mass, "кг/м2", "и у Вас нормальная масса тела")
elif float (index_mass) >=25 and float (index_mass) <=30 :
	print ("Индек массы тела равен:","%.2f" % index_mass, "кг/м2", "и у Вас избыточная масса тела,пора начать работать над собой")
elif float (index_mass) >=30 and float (index_mass) <=35 :
	print ("Индек массы тела равен:","%.2f" % index_mass, "кг/м2", "и у Вас ожирение 1ст,края")
elif float (index_mass) >=35 and float (index_mass) <=40 :
	print ("Индек массы тела равен:","%.2f" % index_mass, "кг/м2", "и у Вас ожирение 2ст, ну,как-бы жесть")
elif float (index_mass) >=40 :
	print ("Индек массы тела равен:","%.2f" % index_mass, "кг/м2", "приехали,все,ожирение 3ст,лучше не двигайтесь вообще,иначе перелом костей и все дела...")




