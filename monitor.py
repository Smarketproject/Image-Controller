import requests, time
import requests
import sys
from analyzer import analyze
import os
clear = lambda: os.system('clear')

SERVER_GET_URL = "https://homol.redes.unb.br/ptr022017B/carrinho/produto/"
SERVER_POST_URL = "https://homol.redes.unb.br/ptr022017B/validacao/"

def normalizelist(json_list):
	normalized_list = []
	for item in json_list:
		normalized_list.append(str(item['name']))
	return normalized_list

while True:

	name_file = str(raw_input("Insira o nome da imagem a ser analisada (coke.jpg): "))

	result = requests.get(SERVER_GET_URL).json()

	print(normalizelist(result))
	clear()
	if len(result) > 0:

		l = normalizelist(result)
		#clear()
		#print(l)
		image_match = analyze(name_file, l)

		requests.post(SERVER_POST_URL, data = {'validator': image_match})

		print("Carrinho do server: ")
		print(list(result))
		if image_match:
			print u'Ok. A imagem corresponde com o carrinho registrado !!!Carrinho Liberado!!!' 
			print u'-------------------------------------' 
			print u'!!!Carrinho Liberado!!!'
			print u'-------------------------------------'  
		else:
			print u'-------------------------------------' 
			print u'Sinto muito. A imagem nao corresponde com o carrinho registrado'
			print u'-------------------------------------' 

		#print (image_match)

	else:
		print u'-------------------------------------' 
		print u'Ops! O server retornou uma lista vazia'
		print u'-------------------------------------' 