class Jar:
    def __init__(self, capacity=12):
        
        self._capacity=capacity
        self._size=0
        self._cookie=u"\U0001F36A"
        if capacity<0:
            raise ValueError
        
        
    def __str__(self):
        return(self._cookie*self._size)
        
    def deposit(self, n):
        self._size+=n
        if self._capacity<self._size:
            raise ValueError
        
    def withdraw(self, n):
        
        self._size-=n
        if self._size<=0:
            raise ValueError
        
        

    @property
    def capacity(self):
        return self._capacity
        
    @property
    def size(self):
        return self._size
def main():
    
    jar=Jar()
    jar.deposit(7)
    jar.withdraw(1)
    jar.deposit(3)

    print(jar)

    
    
    
if __name__ == "__main__":
    main()