list = [1,2,200,300,5500,34000]

def bin_otsing(massiiv, väärtus):
    
    algus  = 0 #paneme kirja massiivi piirid
    lõpp = len(massiiv)
    
    while algus < lõpp: #jooksutame otsingukoodi, kuni otsitava massiivi piirid põrkuvad
        keskmine_element = (lõpp + algus) // 2 #jagame massiivi pooleks
    
        if massiiv[keskmine_element] == väärtus: #kui keskmine element on otsitav, siis tagastame väärtuse
            return((str('Number asub indeksil ' + str(keskmine_element))))
        
        
        if massiiv[keskmine_element] < väärtus: #poolitame listi, kui number on suurem kui keskmine,
            algus = keskmine_element + 1  		#siis uueks alguseks saab praegune keskmine 
        elif massiiv[keskmine_element] > väärtus: #poolitame listi, kui number on väiksem kui keskmine,
            lõpp  = keskmine_element		    #siis uueks lõpuks saab praegune keskmine 
        
        
        
    if väärtus != keskmine_element:   			#võrdleme keskmist ja otsitavat, kui 11. rea if statement
        return('Elemendi asukohta ei leitud')	#ei ole tagastanud väärtust ning programmi lõpetanud.


print(bin_otsing(list,-1))
        
    