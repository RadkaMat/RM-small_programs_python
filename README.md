# RM-Python-small-programs #
Některé programy jsou z knihy o pythonu: Automate the Boring Stuff with Python Programming od: Al Sweigart

1. ## Hadej číslo ##
- uživatel se snaží uhodnout číslo od 0 do 20, program mu radí a počítá pokusy.

2. ## Vytvoření postavy ##
- (podle hry wow) uživatel si vybere frakci a rasu, za kterou chce hrát.

3. ## Ověř číslo - alfa verze ##
- ověří platnost uživatelovi platební karty o 16-ti cifrách na základě Luhnova algoritmu

4. ## Ověř číslo - Luhnův algoritmus ##
- ověří platnost uživatelova čísla bez omezení počtu cifer na základě Luhnova algoritmu



Nápady na zlepšení programů:

  1. u hádání čísla přidat možnost: uživatel omylem hádá stejné číslo 2x,
  řešení: přidat list už hádaných čísel a porovnávat nové hádané číslo s tímto listem
  
  2. u vytvoření postavy na začátek přogramu přidat výčet všech frakcí a ras
  
  3. k ověření čísla přidat i jméno vydavatele karty
  řešení: Mastercard začíná na cifry 51-55 a Visa začíná na cifru 4
  
  4. k ověření čísla ještě to číslo uložit do .csv
  řešení: knihovna csv s funkcí with open()
