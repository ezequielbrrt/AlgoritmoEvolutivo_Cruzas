#! /bin/python
# -*- coding: utf-8 -*-

import numpy as  np

def cruza_uniforme():
	pass

def cruza_Un_punto(padre,madre):
	t = len(padre)
	i = int(np.random.randint(t,size=1))
	while i == 0:
		i = int(np.random.randint(t,size=1))
	hijo1 = padre[0:i]
	hijo2 = madre[0:i]
	hijo1 = hijo1 + madre[i:t] 
	hijo2 = hijo2 + padre[i:t]
	return hijo1,hijo2
	
def cruza_Dos_puntos(padre,madre):
	tam_padre = len(padre)
	i = int(np.random.randint(tam_padre) +1) 
	j = int(np.random.randint(tam_padre) +1)
	while i >= j:
		i = int(np.random.randint(tam_padre))
		j = int(np.random.randint(tam_padre))
	hijo1 = padre[0:i]
	hijo2 = madre[0:i]
	hijo1 = hijo1 + madre[i:j] + padre[j:]
	hijo2 = hijo2 + padre[i:j] + madre[j:]
	return hijo1,hijo2


def main():
	x = "1111100000"
	y = "0000011111"
	print cruza_Un_punto(x,y)
	print cruza_Dos_puntos(x,y)


main()

