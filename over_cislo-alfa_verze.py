# Program kontroluje platnost čísla Luhnovým algoritmem podle Engeto Python lekce 8.: Pokročilější práce s funkcemi.
# Nedokončená alfa verze.

cislo = input("Prosím, zadejte své číslo karty: ")
print(len(cislo))
cifry = []
for cifra in cislo:
    cifry.append(int(cifra))
print(cifry)
suda1 =[]
for i in range(14,0,-2):
    suda1.append(2*(cifry[i]))
print('Dvojnásobek sudých čísel zprava: ')
print(suda1)
super_cifra = int(str(suda1[0])+str(suda1[1])+str(suda1[2])+str(suda1[3])+str(suda1[4])+str(suda1[5])+str(suda1[6]))
print(super_cifra)
licha1 = []
for i in range(15,0,-2):
    licha1.append(cifry[i])
print('Lichá čísla zprava: ')
print(licha1)
suda_licha= suda1 + licha1
print('Lichá a sudá čísla: ')
print(suda_licha)
if ((sum(suda_licha))%10) == 0:
	print('Číslo vaší karty je platné.')
if ((sum(suda_licha))%10) != 0:
	print('Číslo vaší karty je neplatné, zkontrolujte prosím správné zadaní všech číslic.')
