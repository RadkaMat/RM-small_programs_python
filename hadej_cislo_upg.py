# program na hadani cisla podle knihy: Automate boting stuff with python, moje rozsireni: 1. upozorni uzivatele, ze opakuje drive zadane cislo, 2. zda je uzivateluv tip v hadanem rozmezi, 3. aby nespravna cisla se v seznamu neopakovala, 4. 
import random

def string_na_int(slovo):
	try:
		int(slovo)
		return True
	except ValueError:
		return False

hadej = random.randint(1, 20)
print('Zahrajeme si hru. \nMyslím si číslo od 1 do 20. \nZkus to číslo uhádnout. \nBudu ti počítat pokusy.')
nespravna_cisla = []
for i in range(1,20):
	tip = int(input())
	if bool(string_na_int(tip) == False):
		print('To není číslo. Hádej znovu.')
		continue
	else:
		if tip in nespravna_cisla:
			print('Toto číslo už jsi hádal.')
			print(nespravna_cisla)
		elif tip > hadej:
			print('To je moc velké číslo, uber.\nHádej znovu.')
			nespravna_cisla.append(tip)
			print(nespravna_cisla)
			continue
		elif tip < hadej:
			print('To je moc malé číslo, přidej.\nHádej znovu.')
			nespravna_cisla.append(tip)
			print(nespravna_cisla)
			continue
		else:
			print('Uhádl/a jsi na ' + str(i) + '. pokus!')
			print(nespravna_cisla)
			break
else:
	pass