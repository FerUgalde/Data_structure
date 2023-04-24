class HashTable:

    def __init__(self):
        self.table = []


    def get_hash(self, key):
        h=0
        i=1
        j=len(key)
        
        for char in key:
            h+=ord(char)*i      #+j
            i+=1 
        
        """i=0
        for char in key[::-1]:
            h+=ord(char)*i
            i-=1"""
        
        return h % 11
    
    def add_hash(self, key):
        index = self.get_hash(key)

        if len(self.table)<index:
            for enter in range(len(self.table) ,index+1):
                self.table.insert(enter, None)

        if self.table[index] == None:
            self.table[index] = key
    
    #21 29

ht = HashTable()


ht.add_hash("mario")
ht.add_hash("mauricio")
ht.add_hash("rafael")
ht.add_hash("gael")
ht.add_hash("julian")
ht.add_hash("fernanda")
ht.add_hash("samantha")

print(ht.table)

print(ht.get_hash("mario"))
print(ht.get_hash("mauricio"))
print(ht.get_hash("rafael"))
print(ht.get_hash("gael"))
print(ht.get_hash("julian"))
print(ht.get_hash("fernanda"))
print(ht.get_hash("samantha"))

"""print("\n")
print(get_hash("oiram"))
print(get_hash("oiciruam"))
print(get_hash("leafar"))
print(get_hash("leag"))
print(get_hash("nailuj"))
print(get_hash("adnanref"))
print(get_hash("ahtnamas"))
"""

#my_hash = (my_hash + ord(letter) * 13) % len(7)