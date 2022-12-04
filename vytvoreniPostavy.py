#1. vyber frakce a rasy
frakce = ['A', 'H']
alliance = ['Lide', 'Elfove','Trpaslici','Gnomove']
horde = ['Orkove','Nemrtvi','Taureni','Trolove']

print('Vyber frakci, za kterou chces hrat.\n (napis A pro Alliance nebo H pro Hordu)')
hrac1_frac = input()
if hrac1_frac == 'A':
	print(f'Vitej u Alliance.\nVyber si jednu z ras Alliance:\n'+f'{alliance}')
elif hrac1_frac == 'H':
	print('Vitej v Horde.\nVyber si jednu z ras Hordy:\n'+f'{horde}'+'')
else:
	print('To neni hratelna frakce.')
