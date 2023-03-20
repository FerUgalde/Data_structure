# TREES 

class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Tree:

    def __init__(self, value):
        self.root = Node(value)
        self.length = 1


    def print(self):
        def print_val(node = Node, level = 0, position = 'Root'):
            if node is not None:
                print('|\t' * level + position + ': ' + str(node.value))
                print_val(node.right, level + 1, 'Right')
                print_val(node.left, level + 1, 'Left')
        
        print_val(self.root)



    def insert(self, value):
        new_node = Node(value)
        temp = self.root

        while True:
            if temp.value == value:
                print(f"\nYa existe el {value} dentro del arbol\n")
                return False
            elif temp.value > value:
                if temp.left == None:
                    temp.left = new_node
                    self.length += 1
                    return False
                temp = temp.left
            else:
                if temp.right == None:
                    temp.right = new_node
                    self.length += 1
                    return False
                temp = temp.right
            
   
    def contains(self, value):
        next = self.root

        while True:
            if value == next.value:
                print(f"\n{value} si se encuentra en el arbol\n")
                return False
            elif next.value > value:  
                if next.left == None:
                    print(f"\n{value} no se encuentra en el arbol")
                    return False 
                next = next.left
            elif next.value < value:
                if next.right == None:
                    print(f"\n{value} no se encuentra en el arbol")
                    return False 
                next = next.right

                
            
my_tree = Tree(32)
my_tree.insert(18)
my_tree.insert(54)
my_tree.insert(29)
my_tree.insert(14)
my_tree.insert(11)


my_tree.contains(4)
my_tree.contains(29)

my_tree.print()

print("\nLength: ", my_tree.length)
