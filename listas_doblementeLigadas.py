# DOUBLY LINKED LIST

class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.prev = None


    def __str__(self) -> str:
        return str(self.value)

class DoublyLinkedList:
    
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

    def print_list(self):
        temp = self.head
        while temp is not None:
            x = temp.prev
            print(f'Valor: {temp.value}          Valor anterior: {x}')
            temp = temp.next
            

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.prev = None
            self.tail = new_node
        else:
            pre = self.head
            self.tail.next = new_node
            self.tail = new_node
            
            while pre.next is not self.tail:
                pre = pre.next 

            self.tail.prev = pre
        self.length += 1


    def pop(self):
        if self.head == self.tail:
            self.tail = None
            self.prev = None
            self.head = None
            return None 
        else:
            end = self.tail.prev
            self.tail = end
            self.tail.next = None          
        self.length -= 1
            

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.append()
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def popfirt(self):
        if self.length == 1:
            self.pop()
        else:
            self.head = self.head.next
            self.head.prev = None    
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
            temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp
            self.length += 1


    def set(self, index, value):
        if index == self.length:
            self.append(value)
        change_node = self.get(index)
        change_node.value = value
            
    
    def remove_index(self, index):
        if index == 0:
            self.popfirt()
        elif index == self.length-1:
            self.pop()
        elif index >= self.length:
            print("Posicion sin contenido")
        else:
            temp = conection = self.head
            for a in range(index-2):
                temp = temp.next
            for a in range(index+1):
                conection = conection.next
            temp.next = conection
            conection.prev = temp
            self.length -= 1          
            

my_boubly_linked_list = DoublyLinkedList(7)
my_boubly_linked_list.append(5)
my_boubly_linked_list.append(14)
my_boubly_linked_list.append(3)
my_boubly_linked_list.append(19)
my_boubly_linked_list.append(27)
my_boubly_linked_list.append(4)

print("Lista inicial (Append):")
my_boubly_linked_list.print_list()
print('\n')

my_boubly_linked_list.pop()
print(f'Pop(): {my_boubly_linked_list}')

my_boubly_linked_list.prepend(20)
print(f'Prepend(20): {my_boubly_linked_list}')

my_boubly_linked_list.popfirt()
print(f'Popfirst(): {my_boubly_linked_list}')

print(f'Get(1): {my_boubly_linked_list.get(1)}')

my_boubly_linked_list.insert(2, 40)
print(f'Insert(): {my_boubly_linked_list}')

my_boubly_linked_list.set(3, 41)
print(f'Set(): {my_boubly_linked_list}')

my_boubly_linked_list.remove_index(1)
print(f'Remove(): {my_boubly_linked_list}')

my_boubly_linked_list.popfirt()
print(f'Popfirst(): {my_boubly_linked_list}')

print('\nLista final:')
my_boubly_linked_list.print_list()
print('\n')

print('Head: ', my_boubly_linked_list.head.value)
print('Tail: ', my_boubly_linked_list.tail.value)
print('Length: ', my_boubly_linked_list.length)

