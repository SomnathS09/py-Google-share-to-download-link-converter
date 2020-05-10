examList = []
i = input("Enter all strings")

while i != "":
    examList.append(i.split())
    i = input()
    
#print(examList)

for a in examList:
    for s in a:
        print("https://drive.google.com/u/0/uc?id="+s[32:65]+"&export=download")
