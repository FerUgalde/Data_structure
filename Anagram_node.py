import os
from nodos_clases import Node, linkedlist

os.system('cls')

a = input("Ingresa la primer palabra o frase:  ")
b = input("Ingresa la segunda palabra o frase:  ")

# pasa a listas las palabras o frases ingresadas
string_a = list(a)
string_b = list(b)

# se inicializan los nodos respectivos
node1 = linkedlist(string_a[0])
node2 = linkedlist(string_b[0])


# se crean nodos de las listas
for i in string_a:
    node1.append(i)
node1.popfirst()

for i in string_b:
    node2.append(i)
node2.popfirst()


# se remueven los espacios en caso que sean frases
cont = 0
for i in string_a:
    if i == ' ':
        node1.remove_index(cont)
        cont -= 1
    cont += 1

cont = 0
for i in string_b:
    if i == ' ':
        node2.remove_index(cont)
        cont -= 1
    cont += 1

print(node1, node2)

cont = 0
j = 0
k = 0
# se evalua la longitud de los nodos 
if node1.length == node2.length:

    # guardar cantidad de iteraciones
    iterations = node1.length

    for i in range(iterations):
        while node1.get(j).value != node2.get(k).value:
            j += 1
            cont += 1
        k += 1
        node1.remove_index(j)
        j = 0
        
    if cont == 0:
        print("Son la misma palabra o frase, no es anagrama")
    else:
        print(f"'{a}' y '{b}' son un anagrama")
        exit()

else:
    print("No es anagrama")

