<<<<<<< HEAD
def Molarity:
	while True:
		import decimal
		from fractions import Fraction
		print('What is the molarity of the first substance?')
		u = input()
		float(u)
		if u != '':
			print('What is the volume of the substance?')
			uk = input()
			if uk != '':
				print('Whats the ratio of substance 2?')
				i = input()
				if i != '':
						print('How much of it did you use?')
						v = input()
						if v != '':
							f = (float(u) / 1000) * float(uk)
							formula = ((float(f) * float(i)) / float(v)) * 1000
							print('Your concentration of the second substance is: ' + str(round(formula, 2)))
							input()
		else:
			print('Enter a number.')
		break

=======
def Molarity:
	while True:
		import decimal
		from fractions import Fraction
		print('What is the molarity of the first substance?')
		u = input()
		float(u)
		if u != '':
			print('What is the volume of the substance?')
			uk = input()
			if uk != '':
				print('Whats the ratio of substance 2?')
				i = input()
				if i != '':
						print('How much of it did you use?')
						v = input()
						if v != '':
							f = (float(u) / 1000) * float(uk)
							formula = ((float(f) * float(i)) / float(v)) * 1000
							print('Your concentration of the second substance is: ' + str(round(formula, 2)))
							input()
		else:
			print('Enter a number.')
		break

>>>>>>> origin/master
