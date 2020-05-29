import csv
inputfile=input("Enter CSV file name with heading, containing list of IPs to expand, with extention: ")
text_file = open("Output.txt", "w")
with open(inputfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'{", ".join(row)}')
                line_count += 1
            else:
                if "-" in row[0]:
                    ip1=row[0]
                    end= row[0].find("-")
                    startip= (ip1[0:end])
                    startipparts=startip.split(".")
                    start=int(startipparts[3])
                    endip=(ip1[end+1:len(ip1)])
                    endipparts=endip.split(".")
                    end=int(endipparts[3])
                    while start<end+1:
                        newip=startipparts[0]+"."+startipparts[1]+"."+startipparts[2]+"."+str(start)
                        print(newip+",", end="", file=text_file)
                        start+=1
                else:
                    newip=row[0]
                    print(newip+",", end="", file=text_file)
                line_count += 1
print ("The expanded IPs can be found in OUTPUT.TXT")
print ("Changes made.")      
