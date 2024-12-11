from HTML_to_TXT import HTML_txt
import csv
import pandas

#HTML_txt('CasaPiaAndmestrukt.html')

weighted_positions= {'WB': 4,'CB_-_Technical' : 2 , 'ST_-Technical' : 11, 'FB' : 3,  'Mid_-_Attack' : 7, 'Winger' : 9,
                     'AM' : 8, 'CB_-_Defend' : 1 , 'GK' : 0 , 'Mid_-_Defend' : 5 , 'Mid_-_BBM' : 6  , 'ST_-_Target_Man' : 10}

def sorting(sõnastik):
    #kasutasin ülesande täitmiseks counting sorti, 
    võtmed = list(sõnastik.keys())
    keymax = max(võtmed)
    luger = [0] * (keymax + 1)
    for väärtused in võtmed:
        luger[väärtused] += 1
    for i in range(1 , keymax + 1):
        luger[i] += luger [i - 1]
    
    väljastaja = [0] * len(võtmed)

    for i in range(len(võtmed) - 1, -1 , -1):
        väljastaja[luger[võtmed[i]] - 1] = võtmed[i]
        luger[võtmed[i]] -= 1

    return väljastaja 


def mängijad_sõnastikku(massiiv):
    if len(massiiv) == 0:
        return([])
    if len(massiiv) == 1:
        return(massiiv)
    else:
        kogum = []
        mängijate_kogum = {}
        for players in massiiv:
            mängijate_kogum.update({players[2] : massiiv.index(players)})
            #print(mängijate_kogum)
        peaaegu = sorting(mängijate_kogum)
        peaaegu.reverse()
        values = list(mängijate_kogum.keys())
        for i in peaaegu:
            indeks = values.index(i)
            player = massiiv[indeks]
            kogum.append(player)
        return kogum
    


def vahetus(mängijate_nimekiri):
    for player in mängijate_nimekiri:
        player[0] = weighted_positions[player[0]]
    return mängijate_nimekiri

def createlists():
    return([[] for i in range(12)])
def minu_sorteering(mängijate_nimekiri):
    
    listid = createlists()


    for elements in mängijate_nimekiri:   
        position = elements[0]
        get_position = weighted_positions[position]
        listid[get_position].extend([elements])
    return listid
        
        

def Skoor(Mängijad):
    mängijate_fail = HTML_txt(Mängijad)
    tulemused = Mängijad.removesuffix('.html')
    
    players = open(tulemused + '.txt', 'r', encoding = 'utf - 8')
    stats = open('Attributes.txt', 'r')
    
    
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
                                parim_pos = [keymax, mängija_andmed[0], s.get(keymax) ,mängija_andmed[2], mängija_andmed[3]]
                                lõpp.append(parim_pos)
                                
                
                                

                mängija = []
                i = 0
    

    peaaegu = minu_sorteering(lõpp)
    massiiv = []
    for l in peaaegu:
        
        massiiv.append(mängijad_sõnastikku(l))

    väljundfail = open(tulemused + '_väljund.txt', 'w', encoding='utf - 8')
    
    for d in massiiv:
        if not d:
            None
        else:
            positsioonid = d[0]
            positsioonid = positsioonid[0]
            väljundfail.write('\n' + positsioonid + '\n' )
            for t in d:
            
                väljundfail.writelines(str(t) + '\n')
    #väljunffaili kirjutamine


Skoor('CasaPiaAndmestrukt.html')