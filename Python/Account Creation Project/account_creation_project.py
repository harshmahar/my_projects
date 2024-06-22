print("_"*50)
print("Welcome to New Account Registration!")
print("_"*50)

fname = input("Enter full name: ")
email = input("Enter email address: ")
mob = int(input("Enter mobile number: "))
dob = input("Enter DOB (DD/MM/YYYY): ")
user = input("Enter username: ")
ps1 = input("Enter password: ")
ps2 = input("Confirm your password: ")

if ps1==ps2:
	print("_"*50)
	print("Thank you. Your account has been created.")
	print("_"*50)
	print("Here are your account details :-")
	print(f"Name         : {fname}")
	print(f"Username     : {user}")
	print(f"Email address: {email}")
	print(f"Mobile Number: {mob}")
	print(f"DOB          : {dob}")

	print("\nLogin to your account now.\n")
	login1 = input("Enter your username: ")

	if login1==user:
		login2 = input("Enter your password: ")
		if login2==ps1:
			print("\nYou are logged in.\n")
		else:
			print("\nIncorrect Password. \nPlease try again.\n")
			re2 = input("Enter password again: ")
			if re2==ps1:
				print("\nYou are logged in.\n")
			else: 
				print("\nTry again after some time.\n")
	else:
		print("\nIncorrect Username. \nPlease try again.\n")
		re1 = input("Enter username again: ")
		if re1==user:
			re2 = input("Enter your password: ")
			if re2==ps1:
				print("\nYou are logged in.\n")
			else:
				print("\nIncorrect password.\n Please try again.\n")
				re2 = input("Enter password again: ")
				if re2==ps1:
					print("\nYou are logged in.\n")
				else: 
					print("Try again after some time.")
		else: 
			print("\nIncorrect Username.\nTry again after some time.\n")
else:
	print("\nPasswords do not match.\nPlease check and try again.\n")
	re3 = input("Enter password again: ")
	if re3==ps1:
		print("_"*50)
		print("Thank you. Your account has been created.")
		print("_"*50)
		print("Here are your account details :-")
		print(f"Name         : {fname}")
		print(f"username     : {user}")
		print(f"Email address: {email}")
		print(f"Mobile Number: {mob}")
		print(f"dob          : {dob}")
		print("\nLogin to your account now.\n")
		login1 = input("Enter your username: ")

		if login1==user:
			login2 = input("Enter your password: ")
			if login2==ps1:
				print("You are logged in.")
			else:
				print("\nIncorrect Password.\nPlease try again.\n")
				re2 = input("Enter your password: ")
				if re2==ps1:
					print("\nYou are logged in.\n")
				else: 
					print("\nTry again after some time.\n")
		else:
			print("\nIncorrect Username.\nPlease try again.\n")
			re1 = input("Enter username again: ")
			if re1==user:
				re2 = input("Enter your password: ")
				if re2==ps1:
					print("You are logged in.")
			else: 
				print("\nIncorrect Username.\nTry again after some time.")
	else:
		print("\nIncorrect Password.\nPlease try again after some time.")