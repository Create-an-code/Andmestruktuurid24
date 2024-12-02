class Topeltrasi:
    def __init__(self, suurus: int):
        self.tabeli_suurus = suurus
        self.tabel = [-1] * suurus
        self.votmete_arv = 0
        
    def __esimene(self, arv: int):
        #print("esimene", str(arv % self.tabeli_suurus))
        return arv % self.tabeli_suurus
    
    def __teine(self, arv: int):
        #print("teine",str((arv * (arv-1)) % self.tabeli_suurus))
        return (arv * (arv-1)) % self.tabeli_suurus

    def lisa(self, arv: int):
        if arv == -1 or arv ==  -2:
            print('-1 ja -2 ei saa tabelisse sisestada')
            return
        if self.on_tais():
            print('Tabel on täis')
            return
        otsing, samm = self.__esimene(arv), self.__teine(arv)
        while self.tabel[otsing] != -1:
            if -2 == self.tabel[otsing]:
                break
            otsing = (otsing + samm) % self.tabeli_suurus
        self.tabel[otsing] = arv
        self.votmete_arv += 1
    
    def kustuta(self, arv: int):
        if not self.otsi(arv):
            return
        otsing, samm = self.__esimene(arv), self.__teine(arv)
        while self.tabel[otsing] != -1:
            if arv == self.tabel[otsing]:
                self.tabel[otsing] = -2
                self.votmete_arv -= 1
                return
            else:
                otsing = (otsing + samm) % self.tabeli_suurus
        return
    
    def otsi(self, arv: int):
        otsing, samm, algnePos, esimeneIteratsioon = self.__esimene(arv), self.__teine(arv), self.__esimene(arv), True
        while True:
            if self.tabel[otsing] == -1:
                break
            elif self.tabel[otsing] == arv:
                return True
            elif otsing == algnePos and not esimeneIteratsioon:
                return False
            else:
                otsing = (otsing + samm) % self.tabeli_suurus
            esimeneIteratsioon = False
        return False

    def on_tais(self):
        return self.votmete_arv == self.tabeli_suurus

    def __str__(self):
        return str(self.tabel)

#Topelt räsimise algoritm aitab vähendada klastrite teket, mis tekivad ühekordsel räsimisel.

#Ruumikomplekssus: O(tabeli suurus)
#Ajakomplekssus-
#Sisestus: O(n)
#Otsing: O(n)
#Kustutamine: O(n)

#Topelt räsimine on eriti efektiivne kui on vaja hajutada andmeid ja suurendada turvalisust. Näiteks andmebaasides, kus hoitakse kasutajate paroole.






#Katsetus
rasi = Topeltrasi(15)

sisestused = [7,11,223,2,4]
for sisend in sisestused:
    rasi.lisa(sisend)

print(rasi)

otsingud = [7,11,223,2,4,69]
for otsing in otsingud:
    print(rasi.otsi(otsing))

kustutused = [13,19,223,1024,11]
for kustutus in kustutused:
    rasi.kustuta(kustutus)

print(rasi)

