import re
n=int(input())
names=[]
emailid=[]
for i in range(n):
    a,b=input().split()
    names.append(a)
    emailid.append(b)
# ALL INPUTS TAKEN and stored into seperate lists
# sweep through the email ids list and find matches and print corresponding first names
searchkey='@gmail'
matches=[]
for i in range(n):
    x=re.findall(searchkey,emailid[i])
    if x:
        matches.append(names[i])#stores index of email ids having desired string
m=sorted(matches)
for k in m:
    print(k)
    
