
from time import *
from random import *
#from test import enemy
#from test import HP


def guardPath():
    print "its a night of festivties, and a night for vengence, you were apart of Lord Winchesters personal guard, but times have changed"
    print "you have sided with the rebellion, you wish to over through the notion of a ruling class, have people judged on there skills and talents, not there birth"
    print "for this reason you have led a small group of rebel soliders into the mannor gardens, unfortantly up head is a lone guard on patrol and even under the cover of darkness, could spot the odd shapes in the shadows"
    print "do you 1.attempt to sneak up to the guard and catch him by surprise, 2. draw your sword and attack the man 3. draw your musket and shoot the man"

    if raw_input() == "1":
        chance = randint(0, 10)

        if chance > 4:

            print"you have successful snuck up to the guard unnoticed"
            print"do you 1. knock the guard out 2. stab the guard with your sword 3. shoot him with your gun"
            if raw_input () == "1":
                print "ya knock the shit out of him good job"
            elif raw_input () == "2":
                print "ya stab the cunt"
            elif raw_input () == "3":
                print "you shoot him, he is dead as fuck now but the gun is pretty fucking loud mate. "
        else :
            print "as you get close to the guard you accidently snap on a twig, causing the guard to spin around and look right at you"
            print "do you 1. attack the man unarmed 2. attack him with your sword 3. attack him with your gun 4. try and reason with him"

    if raw_input() == "2":


        print "you draw your sword and slowly creep towards him, when your close enough you lunge at the man"
        print "unfortantly this guard was actually doing his job and was on alert and manages to draw his sword out just in time"
        print "combat"
        enemyHP = 10
        playerHP = 15
        while playerHP > 0:
            hit = randint (0,5)
            print "you swing your sword and cause" + str(hit) + " damage to the guard"
            enemyHP = enemyHP - hit
            print "enemy HP" + str(enemyHP)
            if enemyHP <= 0:
                break
            enemyhit = randint(0,5)
            print "the guard takes a swing at you and causes" + str(enemyhit) + " damage to you"
            playerHP = playerHP - enemyhit
            print "player HP " + str(playerHP)

        if playerHP > 0:
            print "with a mighty strike you sink your blade into his flesh, victiours in this small battle"
            print "with this single sentry dealt with you quickly move deeper into the garden, in hopes of getting of any exit route for the guests inside"
        else:
            print "your dead as fuck"



    if raw_input() == "3":

        print "you draw your pistol and fire right at the guard"
        print "he doesn't utter a sound as the man collpases to the ground, unfortantly guns are pretty loud, and the discharge from the pistol echos across the garden"
        print "you stand still for a single moment, staring intently at the open balcony to see if anyone investigates"
        print "today must be your lucky day, as no one comes outside, your team remains undetected"

