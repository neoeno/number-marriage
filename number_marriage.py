def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		pass
	return False
	

def cancellation3():
	print """
	
	How did you even GET here, you DEVIANT!
	
	"""
	exit(0)


def cancellation2(wrong, bad):
	print """
	
	I am afraid we do not live in the kind of world where %s and %s can get married.
	
	We may as well let HARES marry RABBITS.
	
	""" % (wrong, bad)
	exit(0)


def cancellation1(wrong, bad):
	print """
	
	I am afraid we do not live in the kind of world where %s and %s can get married.
	
	We may as well let FOXES get married.
	
	""" % (wrong, bad)
	exit(0)


def holy_matrimony(bride, groom):
	wife = float(bride)
	husband = float(groom)
	return wife + husband



print """
\twhat a beautiful spring morning.
\tthe birds are jumping, the fish are chirping;
\tand none of the owls are awake.

\twho is our bride-to-be?

"""

bride = raw_input("[please enter a number]: ")
shoe_test = is_number(bride)

print """

\tand who is our groom?

"""

groom = raw_input("[please enter another number]: ")
beard_test = is_number(groom)

while True:
	if beard_test == False and shoe_test == True:
		cancellation2(bride, groom)
	elif beard_test == True and shoe_test == False:
		cancellation2(bride, groom)
	elif beard_test == False and shoe_test == False:
		cancellation1(bride, groom)
	elif beard_test == True and shoe_test == True:
		break
	else:
		cancellation3()		

print """

\tdearly beloved,
\twe are gathered here today
\tto join together two numbers
\tin holy matrimony...

"""

raw_input(">> ")

print """

\tinto this holy estate
\tthese two numbers present now come to be joined,

\tas one number.

"""

raw_input(">> ")

print "\n%s, do you take %s to be your lawfully wedded husband?" % (bride, groom)
print "%s: \"I do!\"\n" % bride

raw_input(">> ")

print "\n%s, do you take %s to be your lawfully wedded wife?" % (groom, bride)
print "%s: \"I do!\"\n" % groom

raw_input(">> ")

print """

\tif any number can show just cause why these two numbers
\tmay not be joined together,

\tlet them speak now,

\tor forever

"""

raw_input(">> ")

print """

\thold their peace.

"""

raw_input(">> ")

raw_input("proceed with holy matrimony? press CTRL + C to cancel >> ")

union = holy_matrimony(bride, groom)

print """

\t%s and %s...

""" % (bride, groom)

raw_input(">> ")

print """


									<3<3<3<3<3<3
								<3<3<3<3<3<3<3<3<3
							<3<3<3<3<3<3<3<3<3<3<3
						<3<3<3<3<3<3<3<3<3<3<3<3<3
					<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
				<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
			<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
		<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
	<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
	<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
		<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
			<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
				<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
					<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
						<3<3<3<3<3<3<3<3<3<3<3<3<3
							<3<3<3<3<3<3<3<3<3<3<3
								<3<3<3<3<3<3<3<3<3
									<3<3<3<3<3<3

\tI now pronounce you %g!

<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3

""" % union
