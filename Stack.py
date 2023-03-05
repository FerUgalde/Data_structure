# STACK     (PILA)
class Node:
    
    def __init__(self, value):

        self.value = value
        self.next = None

class Stack:

    def __init__(self, value):
    
        new_node = Node(value)
        self.top = new_node
        self.height = 1


    def print_list(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


    def push(self, value):
        if self.height == 0:
            self.top = Node(value)
        else:
            new_node = Node(value)
            new_node.next  = self.top
            self.top = new_node
        self.height += 1


    def pop(self):
        if self.height == 0:
            self.top = None
        else:
            temp = self.top
            self.top = temp.next
        self.height -= 1


my_stak = Stack(5)
my_stak.push(10)
my_stak.push(19)
my_stak.push(4)
my_stak.push(12)

print('Pila inicial:')
my_stak.print_list()
print('Top: ', my_stak.top.value)
print('Heigth: ', my_stak.height)


print('\nPila despues de dos pop:')
my_stak.pop()
my_stak.pop()

my_stak.print_list()
print('Top: ', my_stak.top.value)
print('Heigth: ', my_stak.height)

#        self.bottom = new_node             no se ocupa

# LIFO  last in - first out
# push / pop
# Top -Bottom