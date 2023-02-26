#Added functions to perform the calculations based on user input
#The input is stored and retrieved from the rtf file based on user input
#Updated variable datatypes to accept decimal input to account for cents
#Called each function in the main program loop
#Allows only selection of numbers 1-4 at the main menu
#Allows only numbers for debits and credits



with open('checkbook.rtf')as f:
    data = f.read()
    f.close()
    

currentbal = data


#Added functions to perform the calculations based on user input
def balance():
    with open('checkbook.rtf')as f: 
            data = f.read()
            f.close()
    currentbal = data
    return float(currentbal)



def debit():
#The input is retrieved from the rtf file based on user input
    with open('checkbook.rtf')as f:
            data = f.read()
            f.close()
    currentbal = data
    currentbal = float(currentbal) - float(debit_input)
#The input is stored in the rtf file based on user input
    with open('checkbook.rtf', 'w') as f:
                f.write(str(currentbal))
    return float(currentbal)



def credit():
    with open('checkbook.rtf')as f:
            data = f.read()
            f.close()
    currentbal = data
#Updated variable datatypes to accept decimal input to account for cents
    currentbal = float(currentbal) + float(deposit_input)
    with open('checkbook.rtf', 'w') as f:
                f.write(str(currentbal))
    return float(currentbal)


def exit():
    exit = "Thank you have a nice day!"
    return exit
    
    
    
#Allows only selection of numbers 1-4 at the main menu

user_input = 1,2,3,4
while user_input == '1' or '2' or '3' or '4':
    print("~~~ Welcome to your terminal checkbook! ~~~")
    print('\n')
    print('What would you like to do?')
    print('\n')
    print('1) view current balance')
    print('2) record a debit(withdraw)')
    print('3) record a credit(deposit)')
    print('4) exit')
    print('\n')
    
    user_input = input('Please make a selection: ')
    print('\n')
    
#Called each function in the main program loop
#1 shows your current balance
    if user_input == '1':
       print(f'Your current balance is {balance()}')
       print('\n')
      
#Allows only numbers for debits and credits 
#2 allows you to make a debit and shows your remaining balance
    elif user_input == '2':
        try:
            debit_input = float(input('How much would you like to withdraw? '))
        except ValueError:
            print('Please input numbers only')
            continue
        print('\n')
        print(f'Your current balance is {debit()}')
        print('\n')
        
#3 allows you to make a credit and shows your new balance
    elif user_input == '3':
        try:
            deposit_input = float(input('How much is your deposit? '))
        except ValueError:
            print('Please input numbers only')
            continue
        print('\n')
        print(f'Your current balance is {credit()}')
        print('\n')
        
#4 exits the program and issues a thank you message      
    elif user_input == '4':
        print(exit())
        
        break
#If the user selects anything other than 1-4 at the main menu 
#they will be prompted to select a number 1-4
    else:
        
        print('Incorrect response, please select 1, 2, 3, or 4 ')
        print('\n')

