import random
#creating defaults variables
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','PQ','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']',':',';','<','>','?','/']
digits = ['1','2','3','4','5','6','7','8','9','0']

# Getting information from user on how to generate the password
characters = input("How many Characters do you want?\n")
digits_num = int(input("How many digits will you need?\n"))
format = input("Simple or Complex password?\n(s/c) ")
# checking the correctness of our user input
while characters:
    # How to check if the inserted varuable is an integer
    # if characters.isnumeric:
    if characters.isdigit():
        characters = int(characters)
        break
    else:
        print("This is not a number")
        characters = input("How many Characters do you want?\n")
#then',' started to create the password
password = None
# wants the user to be able to be generating password repeatedly without inputing name again
# but on one condition answer simple or complex to generate',' and any other answer will cut the loop
while format:
    if format == "simple" or format=="s":
        generated_letters = ""
        for n in range(characters):
            generated_letters += random.choice(letters)

        # Getting the digit from defalt digits using digit num
        generated_digits = ""
        for n in range(digits_num):
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
        for n in range(characters):
            generated_letters += random.choice(letters)

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
    print("Make use of this password:   ", password)
    # Reloading the loop
    end = input('Do you want to generate another password?\n(y/n) ')
    if end == "y" or end == "yes":
        format = input("Simple or Complex password?\n(s/c) ")
    else:
        print("Thanks for generating password using our program',' will like to see you next time!!!")
        break
    
