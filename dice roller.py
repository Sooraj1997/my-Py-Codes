import random
def diceprinter(number):
    
    print('#'*13)
    print('#','#'.rjust(11))
    print('#',str(number).rjust(5),'#'.rjust(5))
    print('#','#'.rjust(11))
    print('#'*13)
print('Welcome to dice roller')
r=input('Press "R" key to Roll')
if r!='r':
    print('Wrong Response!!. try again')
while r=='r':
    diceprinter(random.randint(1,6))
    print("Roll Again?? Press 'R'")
    r=input()
    if r!='r':
        print("Terminating")
