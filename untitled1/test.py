from Tkinter import *

from time import *
from random import *
from Tkinter import *
#from noble import villager
from noble import noblePath
from servant import servantPath
from guard import guardPath
import os, sys
#import Image
#myImage = Image.open("mansion.jpg")





#root = Tk()
#termf = Frame(root, width = 400, height = 200)
#termf.pack(fill=BOTH, expand=YES)
#wid = termf.winfo_id()

def clear_screen():  # Simple function that clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')


def north():
    print "To go north press n then enter"


def east():
    print "To go east press e then enter"


def south():
    print "to go south press s then enter"


def west():
    print "To go west press w then enter"


def setup_class():
    # global is used to create variables that can be used throughout our game
    global name
    global HP
    global CP
    global Hclass
    # Our variable "name" is used to store our name, captured by keyboard input.
    Hclass = raw_input("What class shall you pick ?\n a proud noble ? \n a lowly servant?\n a couragious guard?\n"
                       "Press 1 for noble, 2 for servant, 3 for guard\n")

    # randint is a great way of adding some variety to your players statistics.
    if Hclass == '1':
        HP = randint(8, 20)
        CP = randint(5, 10)
    elif Hclass == '2':
        HP = randint(5, 20)
        CP = randint(5, 20)
    elif Hclass == '3':
        HP = randint(5, 15)
        CP = randint(10, 20)
def enemy():
    global enemyHP
    global enemyCP
    global enemyname
    enemyHP = randint(5, 20)
    enemyCP = randint(5, 20)
    # Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "Ogre"
    print "\nSuddenly you hear a roar, and from the shadows you see an " + enemyname + " coming straight at you...."
    # print enemyname
    print "Your enemy has " + " " + str(enemyHP) + " " + "Health Points"
    print "Your enemy has " + " " + str(enemyCP) + " " + "Combat Power"

def castle():
    print ("*                                 |>>>                    +        ")
    print ("+          *                      |                   *       +")
    print ("                    |>>>      _  _|_  _   *     |>>>		   ")
    print ("           *        |        |;| |;| |;|        |                 *")
    print ("     +          _  _|_  _    \\.    .  /    _  _|_  _       +")
    print (" *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|")
    print ("               \\..      /    ||:+++. |    \\.    .  /           *")
    print ("      +         \\.  ,  /     ||:+++  |     \\:  .  /")
    print ("                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *")
    print ("          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +")
    print ("                 ||+++ ||.    .     .      . ||+++.|   *")
    print ("+   *            ||: . ||:.     . .   .  ,   ||:   |               *")
    print ("         *       ||:   ||:  ,     +       .  ||: , |      +")
    print ("  *              ||:   ||:.     +++++      . ||:   |         *")
    print ("     +           ||:   ||.     +++++++  .    ||: . |    +")
    print ("           +     ||: . ||: ,   +++++++ .  .  ||:   |             +")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |        *")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |")
def setup():
    # global is used to create variables that can be used throughout our game
    global name
    global HP
    global CP
    # Our variable "name" is used to store our name, captured by keyboard input.
    name = raw_input("What is your name ")
    # randint is a great way of adding some variety to your players statistics.



clear_screen()
setup_class()
setup()

global name
global Hclass
global gear

global HP
global CP
global move
global enemyHP

if Hclass == '1':
    Hclass = 'Noble'
elif Hclass == '2':
    Hclass = 'Servant'
elif Hclass == '3':
    Hclass = 'Guard'
else:
    Hclass = 'thing'

Test = "proud"
if Hclass == 'Noble':
    Test = "proud"
elif Hclass == 'Servant':
    Test = 'lowly'
elif Hclass == 'Guard':
    Test = "couragious"
print "Welcome, " + name + " the " + Test + " " + Hclass + " and best of luck on your advantures"
# Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
# Below we are using the helper functions to join a string of text to an integer via the str() helper.
#print "\nYour health is" + " " + str(HP)
#print "Your combat skill is" + " " + str(CP)
castle()
sleep(1)
print "Its a dark and stormy night, and here at Winchester mannor will the lives of three indivduals will be changed forever "

sleep(1)

if Hclass == "Noble":
    noblePath()

elif Hclass == "Servant":
    servantPath()
elif Hclass == "Guard":
    guardPath()


#enemy()
##########COMBAT LOOP
# print "there is a man infront of you, would you like to fight him? Press 1 for yes or 2 for no"
# if raw_input() == "1":
#     while HP > 0:
#         # This loop will only work while our characters HP is greater than 0.
#         hit = randint(0, 5)
#         print "You swing your sword and cause " + str(hit) + " damage"
#         #enemyHP = 10;
#         enemyHP = enemyHP - hit
#         print "E"
#         print enemyHP
#         if enemyHP <= 0:
#             break
#         enemyhit = randint(0, 5)
#         print "The ogre swings a club at you and causes " + str(enemyhit) + "  damage"
#         HP = HP - enemyhit
#         print "P"
#         print HP
#
#
# elif raw_input() == "2":
#     print "you die like a hoe"
#     print "Game Over"
#     sys.exit(0)

















# if Hclass == 'Warrior':
#    print "you have two starting options for gear\n 1. A sword and shield\n 2. a big fuck off club\n input 1 or 2 to make your choice\n"
#    if raw_input() == "1":
#        gear = "1"
#    elif raw_input() == "2":
#        gear = "2"
# elif Hclass == 'Rogue':
#     print "you have two starting options for gear\n 1. Two daggers\n 2. A short sword with two smoke bombs\n input 1 or 2 to make your choice\n"
#     if raw_input() == "1":
#         gear = "1"
#     elif raw_input() == "2":
#         gear = "2"
# elif Hclass == 'Mage':
#     print "you have two starting options for gear\n 1. A wizard staff\n 2. A large wizard tome\n input 1 or 2 to make your choice\n"
#     if raw_input() == "1":
#         gear = "1"
#     elif raw_input() == "2":
#         gear = "2"



# print "Would you like to venture out into the land? Press y then enter to continue"
# # Below we use raw_input to ask for user input, and if it is equal to y, then the code underneath is run.
# if raw_input() == "y":
#     print "You are in your home, with a roaring fireplace in front of you, above the fire you can see your sword and shield"
#     print "Would you like to take your sword and shield? Press y then enter to continue"
#     if raw_input() == "y":
#         # This is a list, and it can store many items, and to do that we "append" items to the list.
#         weapons = []
#         weapons.append("sword")
#         weapons.append("shield")
#         print "You are now carrying your" + " " + weapons[0] + " " + "and your" + " " + weapons[1]
#         print "Armed with your " + weapons[0] + " " + "and " + weapons[
#             1] + " you swing open the door to your home and see a green valley gleaming in the sunshine."
#     else:
#         print "You choose not to take your weapons"
#         print "Armed with your sense of humour, You swing open the door to see a green valley full of opportunity awaiting you."
# else:
#     print "You stay at home, sat in your favourite chair watching the fire grow colder. The land of Narule no longer has a hero."
#     print "Game Over"
#     sys.exit(0)
