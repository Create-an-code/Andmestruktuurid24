#Ternary Search jagab SORTEERITUD massiivi kolmeks võrdseks osaks ning kontrollib nende jagamisepunkte. 
#Kui esimene jagamisepunkt on suurem kui otsitav element, jääb otsitav element esimesse kolmandikku. 
#Kui teine jagamisepunkt on väiksem kui otsitav element, jääb otsitav element kolmandasse kolmandikku.
#Kui otsitav element on jagamisepunktide vahel, jääb otsitav element keskmise kolmandikku.
#Kui otsitav element on jagamisepunktidega võrdne, tagastatakse selle indeks.
#Seejärel korratakse protsessi, kuni otsitav element on leitud või massiiv on läbi kontrollitud.

#Ternary Search ajakomplekssus on O(log3(n)), kuna massiiv jagatakse kolmeks võrdseks osaks.
#Binary Search ajakomplekssus on O(log2(n)), kuna massiiv jagatakse kaheks võrdseks osaks.

def tersearch(otsitav, massiiv, vasak=0, parem=None):
    if parem is None: #Kui parem on määramata, siis määrame selle
        parem = len(massiiv) - 1
    if parem >= vasak: #Kui parem on suurem või võrdne vasakuga, siis jätkame
        kolmandik = vasak + (parem - vasak) // 3
        kolmandik2 = parem - (parem - vasak) // 3


    if massiiv[kolmandik] == otsitav: #Kui otsitav element on esimeses kolmandikus, tagastame selle indeksi
        return kolmandik
    if massiiv[kolmandik2] == otsitav: #Kui otsitav element on kolmandas kolmandikus, tagastame selle indeksi
        return kolmandik2


    if otsitav < massiiv[kolmandik]: #Kui otsitav element on esimese kolmandiku ja jagamispunkti vahel, siis jätkame esimese kolmandikuga
        return tersearch(vasak, kolmandik-1, otsitav, massiiv)
    elif otsitav > massiiv[kolmandik2]: #Kui otsitav element on kolmanda kolmandiku ja jagamispunkti vahel, siis jätkame kolmanda kolmandikuga
         return tersearch(kolmandik2+1, parem, otsitav, massiiv)

    if otsitav > massiiv[kolmandik] and otsitav < massiiv[kolmandik2]: #Kui otsitav element on jagamispunktide vahel, siis jätkame keskmise kolmandikuga
        return tersearch(kolmandik+1, kolmandik2-1, otsitav, massiiv)
    
    #Kui elementi ei leita, tagastame -1
    return -1