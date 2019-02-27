import re
def valid_inputs(pattern,message,error):
	"""check Validation inputs in the function  
	Parameters:
		pattern(str): Search the pattern to compare input.
		message(str): Message throw to input and display 
		error(str): If the condition is false display error message
	Returns(str):
		get string inputs"""	
	while True:
		UserInput = input(message)		 
		if re.search(pattern, UserInput):
			break
		else:
			print(error)	
	return UserInput
def instruct_manage_account():
	"""Display instruction manage account"""	
	print("Please select any one below given:\n1.Check Your Balance\n2.Debit Amount")
	print("3.Credit Amount\n4.Profile Details\n5.Exit")
def get_money(Debit):
	"""Get money from account 
	Parameters:
		Debit(int): Balance is subtracted to Debit and get total money"""
	global Balance
	Balance = Balance - Debit  	
def transfer_money(Credit):
	"""Transfer money in the same account
	Parameters:
		Credit(int): Balance is added to credit and get total money"""		
	global Balance
	Balance = Credit + Balance 	
def manage_account():
	"""Debit, Credit, Check balance and Profile details in managing account"""	
	while True:
		try:
			Option = int(input("Enter Option:"))
			if Option == 1:
				print("Currently Your Available Balance:",Balance)
			elif Option == 2:
				Debit = int(input("Enter the Debit Amount:"))
				if Balance >= Debit:						
					get_money(Debit)							
					print(Balance)
				else:
					print("No Available Balance")								
			elif Option == 3:
				Credit = int(input("Enter the Credit Amount:"))
				transfer_money(Credit)		
				print(Balance)
			elif Option == 4:
				print("Profile Details\nUserName: {}\nMobileNumber: {}\nEmailId: {}\nAvailable Balance: {}".format(UserName,MobileNumber,Email,Balance)) 				
			elif Option == 5:
				print("Your transcation cancel")
				exit()
			else:
				print("Doesn't exist")
		except (SyntaxError, ValueError):		
			print("You didn't enter a number")	
def main():
	global UserName,MobileNumber,Email,Balance
	UserName = valid_inputs("[a-zA-Z_][a-zA-Z0-9]*","Enter Your Name:","Invalid UserName")	
	MobileNumber = valid_inputs("(0/91)?[7-9][0-9]{9}","Enter Your MobileNumber:",
	"Invalid MobileNumber")
	Email = valid_inputs(r"[^@]+@[^@]+\.[^@]+","Enter Your EmailId:","Invalid EmailId")
	Balance = valid_inputs(r"[1234567890]\d{2}$","Enter the Amount:","Invalid Digits")
	Balance = int(Balance)
	instruct_manage_account()
	manage_account()
if __name__ == '__main__':
  main()  