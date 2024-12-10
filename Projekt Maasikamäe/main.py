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


    mängija = []
    i = 0
    lõpp = []
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
                mängija_tulemuse_list = []
                mängija = mängija[:len(mängija)-2]
                mängija_andmed = mängija[:4]
                mängija_atribuudid = mängija[4:]
                s = {}
                
                for element in atribuudid_listis:
                    tulemus = []
                    
                    for pikkus in range(len(mängija_atribuudid)):
                        
                        a = (mängija_atribuudid[pikkus] * element[pikkus])
                        tulemus.append(a)
                        if pikkus == 46:
                            positsioon = element[-1]
                            tulemus = sum(tulemus)
                            skoorid = positsioon, tulemus
                            s.update({skoorid})
                            if len(s) == 11:
                                keymax = max(s, key = lambda x: s[x])
                                parim_pos = [keymax, mängija_andmed[0], s.get(keymax) ,mängija_andmed[2]]
                                lõpp.append(parim_pos)
                                #print(lõpp)
                #print(lõpp)
                                

                                #mängija_tulemuse_list.append()
                                #print(mängija_tulemuse_list)
                #print(mängija_tulemuse_list)            

                #for atribuut in mängija_atribuudid:



                mängija = []
                i = 0
    sorteeritud = sorted(lõpp, key=lambda x: x[0])
    
    def sorteeri(lst):
        x = [item[0] for item in lst]
        x = list(set(x))
        return x
        
        #lõpp
    print(sorteeri(lõpp))
    #for lement in lõpp:
        
         
Skoor('CasaPiaAndmestrukt.txt', 'Attributes.txt')