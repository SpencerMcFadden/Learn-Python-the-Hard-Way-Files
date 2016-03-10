from sys import exit

def grocery_store():
    print "You arrive at the grocery store."
    print "Are you here to get junk food, or healthy food?"
    
    choice = raw_input("> ")
    
    if choice == "junk":
        fail("Terrible life choices, you die from junk food!")
    elif choice == "healthy":
        print "Are you getting vegan food, or a steak?"
        food_type = raw_input("> ")
        
        if food_type == "steak":
            fail("Trick question, meat is evil, you are dead now!")
        elif food_type == "vegan":
            print "Are you going to be a super hero now? Or a villian?"
            super_choice = raw_input("> ")
            
            if super_choice == "hero":
                print "Hooray new super hero! You win!"
                exit(0)
            elif super_choice == "villian":
                print "Time to go to the bank!"
                bank()
            else:
                fail("Really dude?")
    else:
        fail("You really suck")

def bank():
    print "You arrive at the bank."
    print "Are you here to rob it, or make a withdrawl?"
    
    choice = raw_input("> ")
    
    if choice == "rob":
        fail("You're not supposed to rob banks silly!")
    elif choice == "withdraw":
        print "How much money do you want to take out?"
        amount = raw_input("> ")
        
        if amount < 500:
            fail("Damn, you have a boring life")
        else:
            fail("You're broke now!")
    else:
        fail("You get afraid and retreat home!")
            

def fail(why):
    print why, "Congratulations!"
    exit(0)

def start():
    print "You have errands to do"
    print "You can go to the bank or the grocery store."
    print "Where would you like to go?"
    
    choice = raw_input("> ")
    
    if choice == "bank":
        bank()
    elif choice == "grocery store":
        grocery_store()
    else:
        fail("You sit in your house and ignore your responsibilities")

start()