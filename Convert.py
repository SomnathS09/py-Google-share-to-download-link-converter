downloadList = []
i = input("Enter all share links:\n")

downloadList.append(i.split())

print("\nPrinting all the download links\n")
    
for a in downloadList:
    for s in a:
        if(len(s)<65):
            print("Invalid share link, Please recheck")
            continue
        print("https://drive.google.com/u/0/uc?id="+s[32:65]+"&export=download")

