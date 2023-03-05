# QUEUE     (COLA)
class Node:

    def __init__(self, value):

        self.value = value
        self.next = None


class Queve:
    
    def __init__(self, value):

        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1


    def print_list(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def enqueve(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next =  new_node
            self.last = new_node
        self.length += 1


    def dequeve(self):
        if self.first == self.last:
            self.first = None
            self.last = None
            return None 
        else:
            temp = self.first
            self.first = temp.next
            temp.next = None
        self.length -= 1    
        return temp.value



my_queve = Queve(14)
my_queve.enqueve(5)
my_queve.enqueve(7)
my_queve.enqueve(12)
print('Cola inicial:')
my_queve.print_list()
print('First: ', my_queve.first.value)
print('Heigth: ', my_queve.length)


print('\nGet first:')
get = my_queve.dequeve()
print(f'{get}\n')

print('Cola final')
my_queve.print_list()
print('First: ', my_queve.first.value)
print('Heigth: ', my_queve.length)
