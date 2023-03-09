Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
'Vadim'*6
'VadimVadimVadimVadimVadimVadim'
# This program says hello and asks for my name.

print('Hello, world!')
   print('What is your name?')    # ask for their name
   myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
   print(len(myName))
print('What is your age?')    # ask for their age
   myAge = input()
   print('You will be ' + str(int(myAge) + 1) + ' in a year.')
   
SyntaxError: multiple statements found while compiling a single statement


================================ RESTART: Shell ================================
print('Hello, world!')
print('What is your name?')    # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')    # ask for their age
myAge = input()print('You will be ' + str(int(myAge) + 1) + ' in a year.')
SyntaxError: multiple statements found while compiling a single statement

