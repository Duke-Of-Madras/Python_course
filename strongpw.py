password=input("Enter new password: ")
result={}

if len(password)>=8:
    result["length"]=True
else:
    result["length"]=False

digit=False
uppercase=False
for i in password:
    if i.isdigit():
        digit=True

result["digits"]=digit

for i in password:
    if i.isupper():
        uppercase=True

result["uppercase"]=uppercase

print(result)

if all(result.values())==True:
    print("strong password!")
else:
    print("weak password!")


#dictionaries!

