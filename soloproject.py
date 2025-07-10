# Building my version of pet evolution

import random 


response1 = [ " oh!", "Goodie!", "Geez!", "Isn't that creative?",
              "Well! Well ! Well!", "Oh creartive!", 
              "Your pet is so lucky!", "Well genius!", "Well hello there!"
] 

response2 = [ " is such a nice name" , "might be a baddie!", "is a name for a queen "] 
print ("Welcome to Pet Evolution!")

user_name = input ("Whats your name ?: ")

print (f"Hello",user_name) 

name = input ("Now name your pet :")


print (random.choice(response1), f"{name}",random.choice(response2) )

class Pet :
    def __init__ (self, name ):
        self.name = name 
        self.hunger = 0
        self.dirty= 0
        
    def feed (self, food):
        while self.hunger < 100 :
            try :
                food = int (input ( "It's time to feed your pet,\ninput a desired number 1-90:"))   
                if food < 12 :
                    print ("No starving your pet. Animals need food to grow!!")  
                    continue 

                self.hunger += food 
                if self.hunger >= 100:
                   self.hunger = 100 
                   print (f" {name} is now full, 100 is the max,(Hunger : {self.hunger})")

                elif self.hunger <= 30 :
                    print (f"{name} is still very hungry.(Hunger lvl: {self.hunger})")  
                else :
                    print (f" {name} is  feeling really good.")

            except ValueError :
                    print ("Enter a number, not an alphabet just number") 
        print (f"Feeding complete\nNow lets go on to the next task!!! {name} says thank you.")
       
     

    def bath_brush (self, wash):
        self.dirty +=wash
        pass
         
        
    

    def mood (self, alternate):
        pass
     


  
my_pet = Pet (name)

my_pet.feed(0) 


          
  