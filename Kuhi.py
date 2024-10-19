#Defineerime Stacki klassina
class Stack:
    def __init__(self):
        self.kuhi = []
        
    #Et stackiobjekti printides ei prinditaks objecti asukohta
    def __repr__(self):
        return f"{self.kuhi}"
    
    #Stacki pikkuse leidmine
    def len(self):
        return len(self.kuhi)
    
    #stackile uue elemendi lisamine
    def push(self, uus):
        self.kuhi.append(uus)
    
    #Stackist elemendi lisamine.
    #FIFO ja LIFO vahetamiseks tuleb vahetada rida 20 ja 21 vahel
    def pop(self):
        self.kuhi.pop(0)
        #self.kuhi.pop(-1)
        
    #Stacki pealmise elemendi printimiseks
    def peek(self):
        return(self.kuhi[-1])
    
#Testimise kood
stack = Stack()
stack.push(1)
stack.push(3)
stack.push(5)
stack.push(7)
stack.push(9)
stack.push(11)
stack.push(13)
stack.pop()
stack.pop()
stack.pop()
print(stack.peek())
print(stack.len())
print(stack)
