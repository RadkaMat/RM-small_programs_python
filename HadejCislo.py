import random
hadej = random.randint(1, 20)
print('Myslím si číslo od 1 do 20')
print('Hádej to číslo.')
for i in range(1,100):
	tip = int(input())
	if tip > hadej:
		print('To je moc velké číslo, uber.')
		print('Hádej znovu.')
		continue
	if tip < hadej:
		print('To je moc malé číslo, přidej.')
		print('Hádej znovu.')
		continue
	if tip == hadej:
		print('Uhádl jsi na ' + str(i) + '. pokus!')
		break
