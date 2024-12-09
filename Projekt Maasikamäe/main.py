from HTML_to_TXT import HTML_txt
import csv
import pandas

HTML_txt('CasaPiaAndmestrukt.html')



def Skoor(Mängijad, Atribuudid):
    tulemused = Mängijad.removesuffix('txt')
    players = open(Mängijad, 'r', encoding = 'utf - 8')
    stats = open(Atribuudid, 'r')
    skoor = open(tulemused, 'w+', encoding = 'iso-8859-1')

    atribuudid_listis = []
    for rida in stats:
        
        try:
            rida = rida.removesuffix('\n')
        except:
            None
        rida = rida.split(',')
        atribuudid_listis_üksikult = []
        for element in rida:
            
            try:
                element = int(element)
                atribuudid_listis_üksikult.append(element)
            except:
                atribuudid_listis_üksikult.append(element)
        
        atribuudid_listis.append(atribuudid_listis_üksikult)
        print(atribuudid_listis)



    mängija = []
    i = 0

    for line in players:
        if i < 53:  #Kuna ühe mängija kohta on alati 52 rida ja 2 tühja rida, siis saan selle
                    #defineerimsega võtta ühe mängija atribuudid ja need listi salvestada

            line = line.rstrip('\n')
            try:
                line = int(line)
            except:
                None
            mängija.append(line)
            #Lisan rea listi, aga proovin võimlausel strignid teha int-ideks, kuna pean nendega pärast arvutusi tegema
            i = i + 1













            if i == 53:
                mängija = mängija[:len(mängija)-2]
                mängija_andmed = mängija[:4]
                mängija_atribuudid = mängija[4:]

                
                    
                #for atribuut in mängija_atribuudid:



                mängija = []
                i = 0

    

Skoor('CasaPiaAndmestrukt.txt', 'Attributes.txt')