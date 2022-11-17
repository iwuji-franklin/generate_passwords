import random
#creating defaults variables
symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',':',';','<','>','?','/']
digits = ['1','2','3','4','5','6','7','8','9','0']

# Getting information from user on how to generate the password
print("Please, your name must be greater than 5")
name = input("What is your Name?\n")
digits_num = int(input("How many digits will you need?\n"))
print("number must not be greater than 4")
letters_num = int(input("how many letters will you take from your name?\n"))
format = input("Simple or Complex password?\n(s/c) ")
# checking the correctness of our user input
while name:
    if len(name) <=5:
        print("Please, your name must be greater than 5")
        name = input("What is your Name?\n")
    else:
        break
while letters_num:
    if letters_num <= 4:
        break
    else:
        print("OOPs, looks like the number you inputed before is greater than 4")
        letters_num = int(input("how many letters will you take from your name?\n"))
#then, started to create the password
# Switching the data type of the user name to a list
letters = []
for n in name:
    letters.append(n)
# wants the user to be able to be generating password repeatedly without inputing name again
# but on one condition answer simple or complex to generate, and any other answer will cut the loop

while format:
    if format == "simple" or format=="s":
        # getting some path of name to make use of it
        generated_letters1 = letters[random.randint(0,2):]
        # getting the same result
        # uncomment the below
        # begins = [1,2]
        # generated_letters1 = letters[random.choice(begins):]
        
        # Taking only the number of letters_num inputed by the user
        # to get the number of letters needed
        generated_letters = ""
        for n in range(letters_num):
            generated_letters += generated_letters1[n]

        # Getting the digit from defalt digits using digit num
        generated_digits = ""
        for n in range(int(digits_num)):
            generated_digits += random.choice(digits)
        #Getting a symbol
        generated_symbol = random.choice(symbols)

        # Adding all to create a password
        password = generated_letters + generated_symbol + generated_digits
    elif format == "complex" or format=="c":
        random.shuffle(letters)
        random.shuffle(digits)
        random.shuffle(symbols)
        symbols_num = int(input("How many symbols do you want in it?\n"))
        # to get the number of letters needed
        generated_letters = ""
        for n in range(letters_num):
            generated_letters += letters[n]

        # Getting the digit from defalt digits using digit num
        generated_digits = ""
        for n in range(int(digits_num)):
            generated_digits += digits[n]
        #Getting a symbol
        generated_symbols = ""
        for n in range(int(symbols_num)):
            generated_symbols += symbols[n]
            
        # Adding all together
        password = generated_letters + generated_symbols + generated_digits
    else:
        print("You're only meant to choose between 'Simple' or 'Complex'")
        format = input("Simple or Complex password?\n")
    print("Make use of this password:   " + password)
    # Reloading the loop
    end = input('Do you want to generate another password?\n(y/n) ')
    if end == "y" or end == "yes":
        format = input("Simple or Complex password?\n(s/c) ")
    else:
        print("Thanks for generating password using our program, will like to see you next time!!!")
        break
    
