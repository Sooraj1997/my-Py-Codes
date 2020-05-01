n= int(input('Enter number of entries'))
print("Enter names and details")
names=[]
numbers=[]
for i in range(n):# Creates phone book dictionary using user input
    a,*b=input().split(' ')
    names.append(a)
    numbers.append(b)
phonebook={names[i]:numbers[i] for i in range(n)}
testcases=[]
print("Now input entries for search")
while True:#Inputs search queries unless there is no queries
    k = input()
    if k =='':
        break
    testcases.append(k)
for i in range(len(testcases)):#Searching the phonebook and returning
    if testcases[i] in phonebook:
        print(testcases[i]," = ",phonebook[testcases[i]])
    else:
        print('Not found')
input('Press Any key to stop')
