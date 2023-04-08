
#For this challenge you will create a program that contains a class called PlayerCharacter.  
#Your class will use the def __init__ method to create the following attributes:   health, armor rating, attack power.    
#Health can be from 1 - 100.  Armor Rating and Attack Power are from 1 - 20.  DO NOT let the user enter a value outside of this range.  
#You will then create an object from the PlayerCharacter class called Wizard.  
#Next, you will create a main() function that asks the user to input each of the values associated with the PlayerCharacter Attributes.  
#Finally, you will print the Wizard's attributes to the console.  

print('PlayerCharacter: "You are a wizard."')
print('Create your Wizrd by setting your health, armor rating, and attack power.')
print('To do so your health rating will be between 1 and 100, your armor and attack power rating will be between 1 and 20.')

class Wizard:

    def __init__(self, health, armor_rating, attack_power):
        self.__health = health
        self.__armor_rating = armor_rating
        self.__attack_power = attack_power

    #Health can be from 1 - 100
    def set_health_rating(self, armor_rating):
        self.__armor_rating = armor_rating
    #Armor Power are from 1 - 20
    def set_armor_rating(self, armor_rating):
        self.__armor_rating = armor_rating
        #Attack Power are from 1 - 20
    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power

    def get_health(self):
        return self.__health 
    def get_armor_rating(self):
        return self.__armor_rating
    def get_attack_power(self):
        return self.__attack_power

def Wizard_attributes():
    health = int(input("Enter a health rating of 1 to 100: "))
    if health <= 0 or health > 100:
        health = int(input('You can only choose a number between 1-100, try again: '))

    armor = int(input("Enter armor rating of 1 to 20: "))
    if armor <= 0 or armor > 20:
        armor = int(input('You can only choose a number between 1-20, try again: '))
    
    attack = int(input("Enter attack power of 1 to 20: "))
    if attack <= 0 or attack > 20:
        attack = int(input('You can only choose a number between 1-20, try again: '))
    
    wiz = Wizard(health,armor,attack)
    #or when calling from another class.
    #wiz = Wizard.Wiz(health,armor,attack)
    print(f'Your health is {wiz.get_health()}, armor rating is {wiz.get_armor_rating()}, and attack power is {wiz.get_attack_power()}.')

if __name__ == '__main__':

    Wizard_attributes()
