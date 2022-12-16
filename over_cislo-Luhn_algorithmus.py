# Program kontroluje platnost čísla Luhnovým algoritmem podle Engeto Python lekce 8.: Pokročilější práce s funkcemi.

cislo = input("Prosím, zadejte číslo své karty: ")
print(len(cislo))
cifry = []
for cifra in cislo:
    cifry.append(int(cifra))
print(cifry)
len(cifry)
suda1 =[]
for i in range(len(cifry)-2,0,-2):
    suda1.append(2*(cifry[i]))
print('Dvojnásobek sudých čísel zprava: ')
print(suda1)

super_cifra = []
for i in suda1:
	if i > 9:
		super_cifra.append(int(i//10))
		super_cifra.append(int(i%10))
	if i < 9:
		super_cifra.append(int(i))
print('Super_cifra:')
print(super_cifra)
licha1 = []
for i in range(len(cifry)-1,0,-2):
    licha1.append(cifry[i])
print('Lichá čísla zprava: ')
print(licha1)
suda_licha= super_cifra + licha1
print('Lichá a sudá čísla: ')
print(suda_licha)
if ((sum(suda_licha))%10) == 0:
	print('Číslo vaší karty je platné.')
if ((sum(suda_licha))%10) != 0:
	print('Číslo vaší karty je neplatné, zkontrolujte prosím správné zadaní všech číslic.')
