# Ptactica 1. Anagram program

string_a = input("Ingresa la primer palabra:  ")
string_b = input("Ingresa la segunda palabra:  ")


a = list(string_a)
b = list(string_b)


for i in string_a:
    if i == ' ':
        a.remove(i)

for i in string_b:
    if i == ' ':
        b.remove(i)


cont = 0
if len(a) == len(b):

    if string_a == string_b:
        print("Son la misma palabra o frase, no es anagrama")

    else:
        for i in a:
            if i in b:
                cont += 1
            else:
                print("No es anagrama")
                exit()
        if cont == len(a):
            print(f"'{string_a}' y '{string_b}' son un anagrama")
            exit()

else:
    print("No es anagrama")
