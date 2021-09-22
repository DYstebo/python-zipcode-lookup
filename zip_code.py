import csv

with open('geo-data.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = list(reader)
    zCode = input("Enter a zip code to lookup: ")
    for i in range(0,len(mydict)):
        if zCode == mydict[i][0]:
            print("Zipcode " + zCode + " belongs to " + mydict[i][3] + ", " + mydict[i][1] + ", " + mydict[i][2] + " county.")
            infile.close()
            exit()
    print("No match for that zipcode.")
    infile.close()