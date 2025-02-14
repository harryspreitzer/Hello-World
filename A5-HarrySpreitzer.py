# Title:  	Mad Libs
# Author: 	Thomas Luong
# Purpose:	Creates a story based on verbs, adjectives and nouns that the user inputs
# Usage:	Practice python functions and reusability

# Notes:	Create Mad Libs style game where user inputs certain types of words
#			Story doesn't have to be too long but should have some sort of story line.

# Subgoals:
#			If user puts in a name, change first letter to capital letter
#			Change the word "a" to "an" when next word in sentence begins with a vowel



'''

Your hands feel warm.  You wake up and open your eyes slowly.  While lying down you raise your head.  Glancing down
at your hands and see a frog licking your fingers.  It croaks.  Suddenly it jumps onto your chest.  It stares at your 
forehead.  You decide to kiss it.  The frog is enveloped by an intense white light.  It flickers for a while and is 
now only flickering.  Once the light is gone, the frog that was there before is a beautiful human looking back at you.  
The person says, "Hello my name is J, and I love you."  

You married this person and now you have 8 kids.  And a pet frog.

'''

'''

Your hands feel __(adjective describing touch)__.  You wake up and open your eyes slowly.  
While lying down you raise your head.  Glancing down at your __(body part)__ and see [a] __(animal*)__ licking your fingers.  
It __(animal sound)__.  Suddenly it __(verb describing movement and ends in s)__ onto your chest.  It stares at your 
__(body part)__.  You decide to kiss it.  The __(animal*)__ is enveloped by an intense __(color)__ light.  
It flickers for a while and is now only flickering dimly.  Once the light is gone, the __(animal*)__ that was there before 
is a __(a word to describe your crush)__ human looking back at you.  

The person says, "__(greeting)__ my name is __(name of your crush/lover)__, and I love you."  

You married this person and now you have __(number)__ kids.  And a pet __(animal*)__.

'''

from time import sleep
import datetime
def madlibs():
	print("Madlibs starting, please enter the words below: ")
	now = datetime.datetime.now()
	print("------------------------------------------------")
	touchAdj = input("Any adjective: ")
	bodyPart = input("Any body part: ")
	animal = input("What is your favorite animal: ")
	animalSound = input("Write a sound a household pet can make: ")
	color = input("What is your favorite color?: ")
	name = input("The name of your pet: ")
	adjective = input("An adjective you would use to describe the ocean: ")
	number = input("A random number from 6 to 46: ")
	greeting = input("Some kind of greeting for someone you love: ")

	print("\n------------------------------------------------")
	print("Word gathering complete.  Creating story...")
	sleep(5)
	print("\n\nYour face is feeling really " + touchAdj + ".  You run up the hill. ")
	sleep(2)
	print("You finally reach the top.")
	sleep(2)
	print("Glancing down at your " + bodyPart + ", you notice a miniature " + animal + " attacthed to your leg.  ")
	sleep(2)
	print("It lets out a " + animalSound + ".")
	sleep(2)
	print("You cannot beleive how small this animal is.")
	sleep(1)
	print("Before you know it, the " + animal + " turns "+ color + ".")
	sleep(2)
	print("It seems to enjoy its new color.")	
	sleep(2)
	print("Once the color fades, the " + animal + " changes... ")
	sleep(2)
	print("...they are now a " + adjective + " an even smaller" + animal + ".")
	sleep(2)
	print("The extra tiny guy says, \"" + greeting + " my name is " + name + ", and I am getting smaller and smaller.\"")
	sleep(2)
	print("You comfort this animal as they get " + number + " times smaller.  Your temporary pet " + animal + "will soon fade out of existence.")
	sleep(2)
	print("\n Time to generate story:" + str(datetime.datetime.now() - now))
	print("\nThe End.\n\n")

madlibs()