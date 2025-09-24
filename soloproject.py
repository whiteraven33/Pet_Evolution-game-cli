# Building my version of pet evolution

import random 
import sys
import time 
import os


def type_text (text):
    for line in text.splitlines() :
        for char in line :
           sys.stdout.write(char)
           sys.stdout.flush()
           time.sleep (0.05)
           print (end= "" )

response1 = [ " oh!", "Goodie!", "Geez!", "Isn't that creative?",
              "Well! Well ! Well!", "Oh creartive!", 
              "Your pet is so lucky!", "Well genius!", "Well hello there!"
] 

response2 = [ " is such a nice name" , "might be a baddie!", "is a name for a queen "] 
response3 = [ "Snape said 'You dare use my own spells against me, Potter?'" , " Hermione said 'You foul, loathsome, evil little cockroach!?'",
"Draco said 'Training for the ballet, Potter?'", "Dumbledore said 'It does not do to dwell on dreams and forget to live?.' "
 ] 


print( "Welcome to Pet Evolution!")

user_name = input ("What's your name?:")

#gender = input ("What's your gender? 'Male' or 'Female': ").lower()


while True:
    type_text (f"""Hello,{user_name}!, Here's the rule of the game.
This is an game, where you get to play 
an interactive  CLI game with a  pet based on your personality trait.
Type "continue" to proceed and "exit" to quit :.""")
  

    rule = input ("\n\n Enter:").lower().strip()
    if rule == "exit" :
       print ("Have a nice day.")
       sys.exit() 
    elif rule == "continue" :
      print ("Awesome you made the right choice ")
      break
    else :
           print ("oops you were only supposed to type 'exit' or 'continue' ")
    time.sleep(2)           
    os.system("cls")
   

def personality_questions():

    type_text ("""Glad you continued anyway here's the main deal.
A pet would be given to you based on your personality.
And as a parent it would be your sole  purpose to take care of this pet till 
they are adults.""")
    time.sleep(3)
    os.system("cls")
    user_data1 = input ("""personality Test \n\
1. Did you own a pet as a kid? [Yes/No] :""").lower().strip()
    
    if user_data1 == "yes":
     print ("Nice!")
    elif user_data1 == "No"  :
        print ("Not bad, then this is your first pet.")
    time.sleep (2)
    os.system("cls")
    user_data2 = input (""" If one would could describe you what would it be?\n\
                       
-Calm\n\
-Weird\n\
-Playful\n\
-Sad\n\
-Joyful\n\
     Enter : """).lower().strip()
  
    if user_data2 == 'calm':
        print ("Nice")    
    elif user_data2 == 'weird'   :
        print ("Wow, wasn't expecting that.") 
    elif user_data2 == 'playful' :
        print ("bet!")   
    elif user_data2 == 'sad' :
        print ("We can always do something about that.")
    elif user_data2 == 'joyful'    :
        print ("wonderful")
    else :
        print ("You only have to choose from the option above.")    
        time.sleep (2)
        os.system("cls") 

    user_data3 = input (" Do you like the harry potter series? [Yes/No]:") .lower().strip()
    if user_data3 == "yes":
        print (f" {user_name}, do you remember when", random.choice(response3) )
        time.sleep(1)
        print ("I bet you do, but that's by the way")
    else :
        print ("Thats sad... But let's move on.")
    time.sleep (2)
    os.system("cls")         
     
    return user_data1, user_data2, user_data3 

def pet_given (user_data1, user_data2, user_data3):
    if user_data1 == "yes" and user_data2 ==  "calm" and user_data3 == "yes" :
     print ("From the information gotten, you have been assigned a Dog as a pet." )
     result1 = "dog"
    elif user_data1 == "no" and user_data2 == "weird" and user_data3== "yes":
     print ("From the information gotten, you have been assigned a cat as a pet.")
     result2 = "cat" 
    elif user_data1 == "yes" and user_data2 == "playful" and user_data3 == "yes" :
        print ("From the information gotten, you have been assigned a Dragon.")
        result3 = "dragon"
    elif user_data1 == "yes" and user_data2 == "sad"   and user_data3 == "no "  :
        print ("From the information gotten, you haver been assigned a Tiger.")
        result4= "tiger"
    elif user_data1 == "no" and user_data2 == "joyful"   and user_data3 == "yes":
        print ("From the information gotten, you have been assigned a Dog.")
        result5= "dog" 
    time.sleep(2)  
    os.system("cls")  
    return (result1,result2,result3,result4,result5)
user_data1, user_data2, user_data3 = personality_questions()
 
pet_given(user_data1, user_data2, user_data3)
 

     


name = input ("Now name your pet :")






#print (random.choice(response1), f"{name}",random.choice(response2) )

class Pet :
      def __init__ (self, name, pet_type):
        self.name= name 
        self.hunger = 0
        self.dirty= 0
        self.cleanliness= 100
        self.pet_type= pet_type 
        self.mood= "neutral"


        
      def feed (self):
        while self.hunger < 100 :
            try :
                food = int (input ( "Feed your pet 1-90:"))   
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
       
     

      def bath_brush (self):
        while True:
            try : 
               clean = int (input("Bath&brush your pet (1-100)"))
               if clean <0 :
                  print ("Oh no no, thats not how to clean your pet, try again!")
               elif clean <= 10 :
                  print (f"argh you took your pet to the bathroom...Do something {gender} !") 
               elif clean <= 30:
                   print ("You know you must bath and brush the pet right?")
               elif clean == 50 :
                   print ("Hurray you just cleaned the teeth of your pet!") 
               elif clean == 70 :
                   print (""" Hurray!,I guess... successfuly clean. Now dry your pet
                          it might get cold and you don't want that.""")  
               elif clean in [90,100]:
                   print ("Your pet is clean!!!")
                   self.cleanliness = 100
                   break
               else :
                   self.cleanliness +=clean
                   if self.cleanliness >100:
                       self.cleanliness= 100
                   print (f"Your pet is {self.cleanliness}% clean.")   
                   break
            except ValueError:
                   print ("sigh... I clearly said 1-100.") 
            

      def mood (self, alternate):
        pass



