#E-shop. Když si něco přidáš do košíku, evidují se dané položky, počet kusů a sčítá se celková cena. U nedostupného zboží uvidíte: „Zboží není skladem“, u nenabízeného zboží: „Zboží nyní není v prodeji“. Nakonec zkontroluješ celý košík a ujistíš se, že máš všechno.
import pandas as pd

nazev_zbozi = ['trvanlivé mléko','vepřová pečeně', 'banán žlutý', 'jogurt bílý', 'chléb konzumní', 'jablka červená', 'pomeranč']
jednotka_zbo = ['1 litr','1 kilo', '1 kilo', '150 gramů','500 gramů', '1 kilo', '1 kilo']
cena_zbo =[29.90,99.90,29.90,9.90,29.90,29.90,39.90]
pocet_na_sklade =[12,3,15,20,6,20,20]
tabulka_zbo = pd.DataFrame(list(zip(nazev_zbozi, jednotka_zbo, cena_zbo, pocet_na_sklade)),columns=['Název zboží','Jednotka', 'Cena','Zbývá'])
print(f"{'' :=<42}"+'\n'+f"{'Vítejte v našem e-shopu s potravinami' :=^42}"+'\n'+f"{'' :=<42}")
print(tabulka_zbo)
