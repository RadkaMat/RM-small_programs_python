import pandas as pd

#1. vyber frakce a rasy
frakce = ['A', 'H']
alliance = ['Lide', 'Elfove','Trpaslici','Gnomove']
horde = ['Orkove','Nemrtvi','Taureni','Trolove']
tabulka_ras = [['Lide','Orkove'], ['Elfove', 'Nemrtvi'], ['Trpaslici', 'Taureni'], ['Gnomove', 'Trolove']]
df_tab_ras = pd.DataFrame(tabulka_ras, columns = ['Alliance', 'Horde'])
print(df_tab_ras)

print('\nVyber frakci, za kterou chces hrat.\n (napis A pro Alliance nebo H pro Hordu)')
hrac1_frac = input()

if hrac1_frac == 'A':
	print(f'Vitej u Alliance.\nVyber si jednu z ras Alliance:\n'+f'{alliance}')
	hrac1_rasa = input()
	if hrac1_rasa in alliance:
		print(hrac1_rasa)
elif hrac1_frac == 'H':
	print('Vitej v Horde.\nVyber si jednu z ras Hordy:\n'+f'{horde}')
	hrac1_rasa = input()
	if hrac1_rasa in horde:
		print(f'Vytvoril jsis postavu: Horda, {hrac1_rasa}')
else:
	print('To neni hratelna frakce.')
