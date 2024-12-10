class BinNode():
    def __init__(self,data):
        self.data = data
        self.vasak = None
        self.parem = None

    def __str__(self):
        return self.data
    
    def prindiPuu(self):
        if self.vasak:
            self.vasak.prindiPuu()
        print(self.data)
        if self.parem:
            self.parem.prindiPuu()
    
    def sisesta(self, data):
        if self.data:
            if data < self.data:
                if self.vasak is None:
                    self.vasak = BinNode(data)
                else:
                    self.vasak.sisesta(data)
            elif data > self.data:
                if self.parem is None:
                  self.parem = BinNode(data)
                else:
                  self.parem.sisesta(data)
        else:
            self.data = data
    
root = BinNode(99)
root.sisesta(420)
root.sisesta(69)
root.sisesta(33)
root.sisesta(666)
root.sisesta(1337)

root.prindiPuu()


        
    
