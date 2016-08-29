from time import *
from random import *

#from test import *

def noblePath():
    print "It is a night of festivities, you have through a very laxious ballroom party for all the neighbouring lords and ladies\n"
    print "you are speaking with Lord Gibbions, a man who has made a fortune of minning"
    print "he complains to you how is 'useless' workers keep complaining, making insane demands of increase pay and fairer hours\n"
    print "during Lord Gibbions ramble however you here a loud boom of in the distance"
    print "what do you do 1. investigate the sound, 2. it was propably just thunder or 3. use it as an excuse to escape Lord Gibbions\n"
    choice = raw_input()
    if choice == '1':
        print "'excuse me Lord Gibbions, there is something I must look into' as you turn from him and make your way to the outdoor balcony\n"
        print "as you approuch the balcony you stare out across your dimly light garden, pouring rain and a cloudy sky making it near immpossible to make anything out\n"
        print "right as your about to walk back to the party, something glimmers in the dark"
        print "do you 1. take another look or 2. walk back inside"

        if raw_input() == "1":
            sleep(0.5)
            print " you step back out and stare where you saw the glimmer, as your stare out however you see notice the movement in the nearby shadows\n"
            print "as your curiousity takes hold and you learn over the balcony, a flash of lighting briefly alimunates the garden\n"
            print "in that brief second you realize that the glimmer from earlier was the barrel of a gun"
            print " do you 1. ran inside and sound the alarm 2. run inside and tell no one 3. stay out on the balcony\n"

        elif raw_input() == "2":
            print "believe it is a simple trick of the night you give it no thought and head back into the ballroom"
            print "as you enter the ballroom again do you 1. get a drink 2. socialize with guests"

            if raw_input() == "1":
                print "as you approuch a servant for a drink, you hear panicked screams from the front of the mannor"
                print "the servant infront of you is startled and drops his plater spilling champagne and other drinks all over your formal clothes"
                print "do you 1. investigate the sound 2. call the guards 3. slap the shit out of this servant who just ruined your clothes"

            elif raw_input() == "2":
                print "you begin socializng once more with guests, discussing how the lower class are getting more rowdy and self entitled"
                print "when you hear panicked screams from the front of the mannor"
                print "do you 1. investiagate 2. call the guards 3. slowly take your small group towards a nearby exit just in case"

            elif raw_input() == "3":
                print "fuck ya"

    elif raw_input() == '2':
        print "you continue to talk with Lord Gibbions, feigning inverest in his 'problems', after a few minutes however you hear screams and shouts echoing from the front of the mannor\n"
        print "what do you do 1.investigate 2. call your guards 3. make your way to the back of the ballroom near an exit"
        if raw_input() == "1":
                print "hi"

    elif raw_input() == '3':
        print "you quickly cut Lord Gibbions mid sentence, unable to take another word from his mouth and use the commation to move away from him"
        print "after doing so you find the neariest servant with hard liquor, after that conversation you realize you will most likely need it"
        print "as you approuch the servant, the entrance of the ballroom, on the opporsite side blasts open, men in uniform stampede in, muskets at the ready"
        print "this sudden entrance surprises the waiter infront of you, he loses his balance and spills your drink all over your formal wear"
        print "do you 1. call the guards 2. try making a silent exit 3. slap the shit out of the servant"

        if raw_input() == '3':
            print "you slap the shit out of this servant, he is on the ground so fast"
            print "he just ruined a suit that cost more then this guy makes in a year"
            print "you feel so strong in that moment, above this servant, you feel pleased"
            print "then behind you, you hear men exploding out of the ballroom door armed with muskets"
            print "your momentary feeling of strength is replaced with pure dread"



