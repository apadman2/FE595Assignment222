f = open("path to file/Results2.txt", "w")
or j in range(50):
    r = requests.get('http://3.95.249.159:8000/random_company')
    alltext = r.text
    words = alltext.split('\n')
    for i in words:
        if 'Name:' in i:
            namestr = i
            namestr = namestr[16:-5]
            f.write(namestr + '\n')
        if 'Purpose' in i:
            allpurpose = i
            allpurpose = allpurpose[16:-5]
            f.write(allpurpose + '\n')
f.close()

###################### Review of Vaikunth's code - I would suggest creating a dataframe instead for easier manipulation (4/5)


