import requests, time

SERVER_URL = "http://localhost:8000/product/showall/"

while True:

	result = requests.get(SERVER_URL).json()

	print(result)

	if len(result) > 0:
		print("Tem coisas")
	else:
		print("Ta vazio")


	time.sleep(2)