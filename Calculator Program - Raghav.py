import random #Importing the random module for the random number generator module in the program.
import math #Importing math module for operations and square root function.

def addition(user_q,user_q_2): #Addition function with 2 arguments (user_q & user_q_2) that is being passed into it.
    a_total = user_q + user_q_2 #Parameter that adds the numbers and stores it
    print("The answer is ", a_total) #Outputs out the answer
    restart() #Calls the restart function

def subtraction(user_q,user_q_2): #Subtraction function with 2 arguments (user_q & user_q_2) that is being passed into it.
    s_total = user_q - user_q_2 #Parameter that subtracts the numbers from each other and stores it.
    print("The answer is ", s_total) #Outputs out the total value
    restart() #Calls the restart function

def multiplication(user_q,user_q_2): #multiplication function with 2 arguments (user_q & user_q_2) that is being passed into it.
    m_total = user_q * user_q_2 #Parameter that multiplies the numbers together and stores it.
    print("The answer is ", m_total) #Outputs out the answer
    restart() #Calls the restart function


def division(user_q,user_q_2): #Division function with 2 arguments (user_q & user_q_2) that is being passed into it.
    d_total = user_q / user_q_2 #Parameter that divides the first number by the second one.
    print("The answer is ", d_total) #Outputs the answer.
    restart() #Calls the restart function

def rng(n): #Random number generator function with argument "n" passed into it.
    rng_number = random.randint(0,n) #Witihin the range of 0 to n, the system picks a number and stores it.
    print("The random number generated is ", rng_number) #Outputs a statement with the random generated number.
    restart() #Calls the restart function

def roots(s_number): #Square root function which takes in the s_number variable from menu function input.
    rootvalue = math.sqrt(s_number) #Square root in-built function.
    print("The square root of your number is ", rootvalue) #Outputs the square root of a number and a statement.
    restart() #Calls the restart function.

def CelsiusToKelvin(): #Function
    c_value = float(input("Please enter the values in Calsius that you wish to convert into Kelvin: ")) #Asking user input for Celsius Value
    k_value = (c_value + 273.15) #Calculating Kelvin value
    print(c_value, " in Celsius is ", k_value, " in Kelvin.") #Outputs statement
    restart() #Calls the restart function

def CelsiusToFahrenheit(): #Function
    ctof_value = float(input("Please enter the values in Calsius that you wish to convert into Fahrenheit: ")) #Asks user to input Celsius value | CTOF - Celsius To Fahrenheit
    ffce_value = (((9/5) * ctof_value) + 32) #Calculates Fahrenheit value | FFCE - Fahrenheit From Celsius
    print(ctof_value, " in Celsius is ", ffce_value, " in Fahrenheit.") # #Outputs statement
    restart() #Calls the restart function

def KelvinToCelsius():
    ktoc_value = float(input("Please enter the values in Kelvin that you wish to convert into Celsius: "))
    ctok_value = (ktoc_value - 273.15)
    print(ktoc_value, " in Kelvin is ", ctok_value, " in Celsius.")
    restart() #Calls the restart function

def KelvinToFahrenheit(): #Function
    ktof_value = float(input("Please enter the values in Kelvin that you wish to convert into Fahrenheit: ")) #Asks user to input Kelvin value | KTOF - Kelvin To Fahrenheit
    ffke_value = (((ktof_value - 273.15) * 9/5) + 32) #Calculates fahrenheit value | FFKE = Fahrenheit From Kelvin
    print(ktof_value, " in Kelvin is ", ffke_value, " in Fahrenheit.") #Outputs statement
    restart() #Calls the restart function

def FahrenheitToCelsius(): #Function
    ftoc_value = float(input("Please enter the value in Fahrenheit that you wish to convert into Celsius: ")) #Asks user to input Fahrenheit value and stores it | FTOC - Fahrenheit To Celsius
    cffa_value = ((ftoc_value - 32) * 5/9)  #Calculates Fahreinheit value | CFFA = Celsius From Fahrenheit
    print(ftoc_value, "in Fahreniheit is ", cffa_value, " in Celsius") #Outputs statement
    restart() #Calls the restart function

def FahrenheitToKelvin(): #Function
    ftok_value = float(input("Please enter the value in Fahrenheit that you wish to convert into Kelvin: ")) #Asks user to input Fahrenheit value | FTOK - Fahrenheit to Kelvin
    kffa_value = (((ftok_value - 32) * 5/9) + 273.15) #Calculates Kelvin value | KFFA = Kelvin From Fahrenheit
    print(ftok_value, "in Fahreniheit is ", kffa_value, " in Kelvin.") #Outputs statement
    restart() #Calls the restart function


def menu(): #Menu Function
    print("-----------------START-----------------") #Start menu with a list of options for the user to choose
    print("-----Please choose an option below-----")
    print("-1-  Addition")
    print("-2- Subtraction")
    print("-3- Multiplication")
    print("-4- Division")
    print("-5- Random Number Generation")
    print("-6- Calculate the Square root of a function")
    print("-7- Converting Temperature between Celsius, Fahrenheit and Kelvin.")
    menu_input = int(input("Waiting for your input, please enter a number corresponding to its option here: ")) #Asks for user input by selecting an option from the menu and taking its corresponding number.  
    if menu_input == 1:  #If loop that loops through conditions until one is met
        addition(user_q,user_q_2) #Calling addition function with the 2 numbers
    elif menu_input == 2: #Condition
        subtraction(user_q,user_q_2) #Calling subtraction function with the 2 numbers
    elif menu_input == 3: #Condition
        multiplication(user_q,user_q_2) #Calling multiplication function with the 2 numbers
    elif menu_input == 4: #Condition
        division(user_q,user_q_2) #Calling division function with the 2 numbers
    elif menu_input == 5: #Condition
        n = int(input("Please enter the number for the range, i.e if you input 7, the program will generate a random number between 1 - 7: ")) #Asks for user input on range value
        rng(n) #Calling random number generator function with argument n
    elif menu_input == 6: #Condition
        s_number = float(input("Please input a number you wish to find the square root of: ")) #Asking input to get the square root of
        roots(s_number) #Calling root function
    elif menu_input == 7: #Condition
        print("List of options below:") #Outputs text as a selection menu
        print("-----------------Temperature Conversions-----------------")
        print("-1-  Celsius to Kelvin")
        print("-2- Celsius to Fahrenheit")
        print("-3- Kelvin to Celsius")
        print("-4- Kelvin to Feahrenheit")
        print("-5- Fahrenheit to Celsius")
        print("-6- Fahreneheit to Kelvin")
        choice = int(input("Please enter an number from the options list: ")) #Asks for user input and stores it in variable choice
        if choice == 1: #Condition | #If loop that loops through conditions until one is met
            CelsiusToKelvin() #Calls Celsius to Kelvin function
        elif choice == 2: #Condition
            CelsiusToFahrenheit() #Calls Celsius to Fahrenheit function
        elif choice == 3:
            
            KelvinToCelsius() #Calls Kelvin to Celsius function
        elif choice == 4:
            KelvinToFahrenheit() #Calls Kelvin to Fahrenheit function
        elif choice == 5:
            FahrenheitToCelsius() #Calls Fahrenheit to Celsius function
        elif choice == 6:
            FahrenheitToKelvin() #Calls Fahrenheit to Kelvin function 
        else:
            print("You have not picked a correct option") #Outputs statement
            restart() #Calls restart function
    else: #If no other conditions are met, program moves to last commannd 
        print("You have not entered a number available from the options list...") #Outputs a statement
        menu() #Calls menu function

def restart(): #Restart function
    restart_q = int(input("Would you like to use the calculator again? Type 1 for Yes or 2 for No: ")) #User input on whether they wish to use the calculator again
    if restart_q == 1: #Condition | #If loop that loops through conditions until one is met
        menu() #If condition successful, it goes back to the menu function 
    elif restart_q == 2: #Second condition in the loop to check
        print("Thank you for using the calculator, enjoy your day...") #Outputs statement
    else: #If all conditions aren't met, it will execute the command underneath
        print("You did not type an appropriate input...") #Outputs a statement
        restart() #Calling out the restart function 

print("Welcome to the Calculator program where you can perform numerous functions from adding two numbers together, to conversions between different temperature units") #Text to greet the user and state different functions.
print("For example, your values a and b with a multiplication operation will be a*b")
user_q = float(input("Please input the first value you will be using for the equation: ")) #Asks for user input for first number.
user_q_2 = float(input("Please input the second value you will be using for the equation: ")) #Asks for user input for second number.

menu() #Calls the menu function

