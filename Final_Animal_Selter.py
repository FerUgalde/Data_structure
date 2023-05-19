#Submit the animal shelter project where you can: 
#1. Display pets
#2. Dequeue dogs
#3. Dequeue cats
#4. Dequeue any animal 
#5. Exit

from datetime import datetime 

class Animal:
    
    def __init__(self, specie, name, age, breed, date):
        self.specie = specie
        self.name = name
        self.age = age
        self.breed = breed
        self.date = date
        self.next = None


class Shelter:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    
    def print_list(self):
        temp = self.first
        while temp is not None:
            print(f"Specie: {temp.specie}  Name: {temp.name}   Age: {temp.age}   Breed: {temp.breed}   Entry date: {temp.date}")
            temp = temp.next


    def enqueue_animal(self, specie, name, age, breed, date):

        new_animal = Animal(specie, name, age, breed, date)

        if self.length == 0:
            self.first = new_animal
            self.last = new_animal
        else:
            self.last.next =  new_animal
            self.last = new_animal
        self.length += 1 


    def dequeue_animal(self, specie):
        if self.length == 0:
            return "Sorry! There are no more animals"
        temp = self.first
        if specie == 'Any' or temp.specie == specie:
            if self.first == self.last:
                self.first = None
                self.last = None            
            else:
                self.first = temp.next
                temp.next = None
            self.length -= 1    
            return f"Specie: {temp.specie}  Name: {temp.name}   Age: {temp.age}   Breed: {temp.breed}   Entry date: {temp.date}"
        
        else:       
            while temp.specie != specie:
                if temp == self.last or self.first == self.last:
                    return(f"\nWe don't have any more {specie}s. Sorry!\n")
                connection = temp
                temp = temp.next               
            if temp == self.last: 
                self.last = connection
                self.last.next = None 
            else:
                temp2 = temp.next
                connection.next = temp2
        self.length -= 1    
        return f"Specie: {temp.specie}  Name: {temp.name}   Age: {temp.age}   Breed: {temp.breed}   Entry date: {temp.date}"


my_animal_shelter = Shelter()

op = 0
while op != 4:
    op = int(input("""
    \n\tWelcome to the Animal Shelter!\n
    1. Put in the shelter
    2. Adopt
    3. Show current animals at the shelter
    4. Exit\n"""))

    if op == 1:
        today = datetime.today()
        day = f"{today.day}/{today.month}/{today.year}   {today.hour}:{today.minute}"

        segurity = 0
        while segurity == 0:
            specie = int(input("[1] Dog     [2] Cat\n"))
            if specie == 1 :
                specie = 'Dog'
                segurity = 1
            elif specie == 2:
                specie = 'Cat'
                segurity = 1
            else:
                print('\nInvalid option\n')

        name = input("Enter de name:    ")
        age = input("Enter de age:   ")
        breed = input("Enter de breed:  ")
        my_animal_shelter.enqueue_animal(specie, name, age, breed, day)

    elif op == 2:
        segurity = 0
        print("\nWhat species would you like it to be?\n")
        while segurity == 0:
            specie = int(input("[1] Dog     [2] Cat     [3] Any\n"))
            if specie == 1:
                specie = 'Dog'
                segurity = 1
            elif specie == 2:
                specie = 'Cat'
                segurity = 1
            elif specie == 3:
                specie = 'Any'
                segurity = 1
            else:
                print('\nInvalid option\n')

        get = my_animal_shelter.dequeue_animal(specie)
        print(f'\nThe data of the pet you adopted are: \n\t{get}\n')

    elif op == 3:
        print("\nThe current animals at the shelter are: ")
        my_animal_shelter.print_list()

    elif op == 4:
        print("\nLeaving the program...\n")
    
    else:
        print("\nInvalid option\n")