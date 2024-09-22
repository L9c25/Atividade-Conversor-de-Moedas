import requests



moedas = ['BRL', 'EUR', 'USD', 'ARS', 'GBP', 'CAD', 'CHF', 'JPY', 'AUD', 'CNY']

req = requests.get(f"https://economia.awesomeapi.com.br/json/last/BRL-EUR,BRL-USD,BRL-ARS,BRL-GBP,BRL-CAD,BRL-CHF,BRL-JPY,BRL-AUD,BRL-CNY")

cotacoes = []

for moeda in moedas:
	if moeda != 'BRL':
		cotacao = (req.json()[('BRL' + moeda)]['bid'])
		cotacao = round(float(cotacao), 2)
		cotacoes.append(cotacao)

	
print(cotacoes)