#!/usr/bin/python
import random
f=open("fechas.csv","w")
for i in range(20):
	dia=random.randint(1, 31)
	mes=random.randint(1, 12)
	anio=random.randint(0, 14)
	if mes == 2:
		if dia>=28:
			dia=28
	if mes == 4:
		if dia==31:
			dia=30
	if mes == 6:
		if dia==31:
			dia=30
	if mes == 9:
		if dia==31:
			dia=30
	if mes == 11:
		if dia==31:
			dia=30
	fecha=str(dia)+"/"+str(mes)+"/"+str(anio)+";\r"
	print fecha
	f.write(fecha)
f.close()
