# EXAMEN 1 IT'S A PALINDTOME?

class Node:
    
    def __init__(self, value):

        self.value = value
        self.next = None
        self.prev = None

    
    def __str__(self) -> str:
        return str(self.value)

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


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


evaluacion = input('Ingresa la secuencia a evaluar  ').lower()

pal = list(evaluacion)

is_palindrome = DoublyLinkedList()

for i in pal:
    is_palindrome.append(i)

print(is_palindrome)

h = is_palindrome.head
t = is_palindrome.tail
i = 1


while h.value == t.value:

    h = h.next
    t = t.prev
    i += 1
    if i == is_palindrome.length:
        print('Si es Palindrome')
        exit()


if i != is_palindrome.length:
    print('No es Palindrome')
