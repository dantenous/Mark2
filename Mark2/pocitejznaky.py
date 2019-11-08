with open('rozsypeny-caj.txt', mode='r') as soubor:
    nac = soubor.read()

with open('katakana.txt', mode='r') as katana:
    kat = katana.read()

with open('hiragana.txt', mode='r') as hiragana:
    hir = hiragana.read()



def uloz_znak_hira(znak):
    with open('hiragana-vypis.txt', mode='a', encoding='utf-8') as hiragana1:
        hiragana1.write(znak)

def uloz_znak_kata(znak):
    with open('katana-vypis.txt', mode='a') as katana1:
        katana1.write(znak)

kate = kat.rstrip()
nacti = nac.rstrip()
hira = hir.rstrip()

i = 0
pocet_katana = 0
pocet_hiragana = 0

i=0
celkem = len(nacti)
while i < celkem:
    for i in range(celkem):
        if nacti[i] in kate and nacti[i] != '\n':
            pocet_katana += 1
            uloz_znak_kata(nacti[i])
            print(nacti[i])
        if nacti[i] in hira and nacti[i] != '\n':
            pocet_hiragana += 1
            uloz_znak_hira(nacti[i])
            print(nacti[i])
    i+=1
        
print("Pocet hiragana je: ", pocet_hiragana, "Pocet katana je: ", pocet_katana)
