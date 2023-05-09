class HashTable:
    
    def __init__(self):
        self.table = []


    def hash(self, key):
        h=0
        i=1       
        for char in key:
            h+=ord(char)*i
            i+=1         
        return h % 11
    
    def add_hash(self, key, value):
        index = self.hash(key)
        if len(self.table)<index:
            for enter in range(len(self.table) ,index+1):
                self.table.insert(enter, None)

        if self.table[index] == None:
            self.table[index] = []
        self.table[index].append([key, value])
    
    def get_hash(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for i in range(len(self.table[index])):
                if self.table[index][i][0] == key:
                    return self.table[index][i][1]
        return None
    
    def print_hash(self):
        for k, v in enumerate(self.table):
            print(k, " :  ", v)

ht = HashTable()


ht.add_hash("mario", 10)
ht.add_hash("mauricio", 9)
ht.add_hash("rafael", 8)
ht.add_hash("gael", 7)
ht.add_hash("julian", 6)
ht.add_hash("fernanda", 5)
ht.add_hash("samantha", 4)

ht.add_hash("oiram", 30)
ht.add_hash("oiciruam", 29)
ht.add_hash("leafar", 28)
ht.add_hash("leag", 27)
ht.add_hash("nailuj", 26)
ht.add_hash("adnanref", 25)
ht.add_hash("ahtnamas", 24)


print("\n")

print(ht.get_hash('leag'))

print("\n")

ht.print_hash()



#my_hash = (my_hash + ord(letter) * 13) % len(7)