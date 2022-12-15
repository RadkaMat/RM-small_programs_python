# program na hadání čísla podle knihy: Automate boting stuff with python
# moje rozšířeni: 1. upozorní uživatele, když opakuje dříve zadané číslo 2. zda je uzivateluv tip v hádanémm rozmezí 3. aby nespravná čísla se v seznamu neopakovala
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
