import random

print "Welcome to a virtual dice roller"

response = raw_input("would you like to begin?" )

if response == "yes":
	print "You said yes"
	repeat = True
	
	while(repeat):
		randnum = random.randrange(1,7)
		print "the number is %s" % (randnum)
		response = raw_input("Continue? ")
		if(response == "no"):
			repeat = False
			print "Ending Dice Roller"

else:
	print "Ending Dice Roller"