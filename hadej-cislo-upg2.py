# Toto je jednoduchý program na hru, ve kterém uživatel jako hráč se pokouší uhádnout náhodně vygenerované číslo.

import random

def string_na_int(slovo):
    try:
        int(slovo)
        return True
    except ValueError:
        return False

hadej = random.randint(1, 20)
print('Zahrajeme si hru. \nMyslím si číslo od 1 do 20. \nZkus to číslo uhádnout. \nMáš jen 5 pokusů, které ti budu počítat.')
nespravna_cisla = []
for pocet_pokusu in range(1, 7):
    tip = input()
    
    if pocet_pokusu == 6:
        print('Vyčerpal jsi všechny své pokusy. Bohužel jsi mé číslo neuhádl.')
    
    elif string_na_int(tip):
        tip = int(tip)
        
        if tip in nespravna_cisla:
            print('Toto číslo už jsi hádal. Hádej dál.')
            
        elif tip > hadej:
            print('To je moc velké číslo, uber. Hádej znovu.')
            nespravna_cisla.append(tip)
            continue
            
        elif tip < hadej:
            print('To je moc malé číslo, přidej. Hádej znovu.')
            nespravna_cisla.append(tip)
            continue
            
        else:
            print('Uhádl/a jsi na ' + str(pocet_pokusu) + '. pokus!')
            break
            
    else:
        print('To není číslo. Hádej znovu.')
        continue
