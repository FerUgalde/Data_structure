# LISTAS LIGADAS


class Node:
    

    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self) -> str:
        return str(self.value)
    

class linkedlist: 


    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    
    def __len__(self):
        return self.length
    

    def __str__(self) -> str:
        String = '['
        temp = self.head
        for i in range(len(self)):
            String += str(temp)
            if i is not len(self)-1:
                String += str(', ')
            temp = temp.next
        String += "]"
        return String
    
    '''def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next'''


    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def pop(self):
        if self.head == self.tail:
            self.tail = None
            self.head = None
            return None 
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next  
            self.tail = temp
            self.tail.next = None    
        self.length -= 1


    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def popfirst(self):
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
        self.length -=1


    def get(self, index):
        temp = self.head
        if index >= self.length:
            print("Valor no permitido")
        else:
            for a in range(index):
                temp = temp.next
            return temp
    

    def insert(self, index, value):
        if index > self.length:
            print("Tu posicion supera el tamanio de la lista")
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp = self.head
            for a in range(index-1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1


    def set(self, index, value):
        if index == self.length:
            self.append(value)
        change_node = self.get(index)
        change_node.value = value


    def remove(self, value):
        temp = self.head
        for a in range(self.length):
            if temp.value == value:
                self.remove_index(a)
            temp = temp.next
    

    def remove_index(self, index):
        if index == 0:
            self.popfirst()
        elif index == self.length-1:
            self.pop()
        elif index >= self.length:
            print("Posicion sin contenido")
        else:
            temp = self.head
            for a in range(index-1):
                temp = temp.next
            conection = temp
            for a in range(2):
                conection = conection.next
            temp.next = conection
            self.length -= 1

            
my_linked_list = linkedlist(4)
my_linked_list.append(10)
my_linked_list.append(6)
my_linked_list.append(2)
my_linked_list.append(8)
my_linked_list.append(5)
my_linked_list.append(2)
my_linked_list.append(15)

print(f'Lista inicial: {my_linked_list} \n')

my_linked_list.pop()
print(f"pop:  {my_linked_list}\n")

my_linked_list.prepend(20) 
print(f"prepend:  {my_linked_list}\n")

my_linked_list.popfirst()
print(f"popfirst:  {my_linked_list}\n")

print(f"get(3): {my_linked_list.get(3)}")

my_linked_list.insert(4 , 30)
print(f"\ninsert:  {my_linked_list}\n")

my_linked_list.set(1, 30)
print(f"set:  {my_linked_list}\n")

my_linked_list.remove_index(4)
print(f"remove_index:  {my_linked_list}\n")

my_linked_list.remove(2)
print(f"remove:  {my_linked_list}\n")

try:
    print("head", my_linked_list.head.value)
    print("tail", my_linked_list.tail.value)
    print("length", my_linked_list.length)
except AttributeError:
    print("No hay valores en el nodo")
