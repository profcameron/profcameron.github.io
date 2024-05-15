import mysql.connector
import os
import random
import sys

def processName(fname):
    nameFile = open(fname,"r")
    type = ""
    chinese = []
    japanese = []
    korean = []
    indian = []
    arabic = []
    spanish = []
    american = []
    typeValue = ''

    # split out the file name from the extension, use it to print what we are parsing
    print("Loading and parsing "+fname.split(".")[0]+" names data set...")

    # bring in data from name dataset
    # Need to rstrip() to remove carraige return
    for nameLine in nameFile:
        name = nameLine.rstrip()
        # If there is a * in the line, it's a header for a type of name
        if '*' in name:
            # lowercase the type, and then split on the asterisk
            # [0] is the asterisk, [1] is the value
            # data file format for a header row is asterisk followed by name, such as
            # *american
            type = name.lower().split("*")[1]
        else:
            # Craft a Python command to append the name to the appropriate list
            # Probably a cleaner way to do this
            # command = chinese.append("Liang")
            command = type+".append(\""+name+"\")"
            exec(command)

    nameFile.close()

    return(chinese, japanese, korean, indian, arabic, spanish, american)

def generateEmail(fname, lname):
    mailServers = ["yahoo.com","gmail.com","hotmail.com","gmail.com","live.com","mail.com","aol.com","ymail.com","zohomail.com","optonline.net","verizon.net"]

    firstLen = random.randint(1,len(fname))
    lastLen = random.randint(1,len(lname))
    # Could expand this to use non-Yahoo email
    email = fname[0:firstLen]+lname[0:lastLen]+str(random.randint(10000,99999))+"@"+mailServers[random.randint(0,len(mailServers)-1)]
    return(email)

def main():
    # Will hold the name of the street (i.e. Main, College)
    street = []
    # Will hold the type of street (i.e. Street, Road, Court)
    streetType = []

    # Three lists to hold the city, state, and ZIP
    city = []
    state = []
    zip = []

    ethnicityTypes = ["chinese","japanese","korean","indian","arabic","spanish","american"]

    # Could probably do this with a 2D array if I have time

    chineseLast = []
    japaneseLast = []
    koreanLast = []
    indianLast = []
    arabicLast = []
    spanishLast = []
    americanLast = []
    
    chineseFirst = []
    japaneseFirst = []
    koreanFirst = []
    indianFirst = []
    arabicFirst = []
    spanishFirst = []
    americanFirst = []

    zipFileName = "ZIP.txt"
    streetFileName = "streets.txt"
    streetTypeFileName = "streetTypes.txt"
    outputFileName = "SQLFile.sql"
    lastFileName = "last.txt"
    firstFileName = "first.txt"

    # Check all critical files exist before start
    # os.path returns 1 if the file exists 
    inputFilesPresent = os.path.exists(zipFileName) +\
                        os.path.exists(streetFileName) +\
                        os.path.exists(streetTypeFileName) +\
                        os.path.exists(lastFileName) +\
                        os.path.exists(firstFileName)

    # Update to dictionary eventually
    if inputFilesPresent != 5:
        print("Missing input files. Ensure ZIP.txt, streets.txt, and streetTypes.txt" +
              "are in the folder along with this file.")
        sys.exit()
    else:
        print("All required data files present")

    outputFilePresent = os.path.exists(outputFileName)

    if(outputFilePresent):
        removeFile = input("Output file is already here. Delete (D), Rename (R), or Quit (Q): ")
        if removeFile.upper() == "D":
            print("Deleting existing",outputFileName)
            os.remove(outputFileName)
        elif removeFile.upper() == "R":
            renameFilePresent = os.path.exists("SQLFile.old")
            if renameFilePresent:
                renameFileName = input("Enter file name: ")
                os.rename(outputFileName,renameFileName)
                print("Renaming existing file to",renameFileName)
            else:
                print("Renaming existing file to SQLFile.old")
                os.rename(outputFileName,"SQLfile.old")
        else:
            print("Exiting program, please rename",outputFileName,".")
            sys.exit()
    # Open SQLfile.sql to store script
    outFile = open(outputFileName, "w")

    inZIP = open(zipFileName,"r")

    print("Loading and parsing ZIP code data set...")
    # bring in data from USPS ZIP database
    # In the format 07013,Clifton,NJ
    # (ZIP,City,State)
    # Need to rstrip() state to remove carraige return
    for lineZip in inZIP:
        splitLine = lineZip.split(",")
        zip.append(splitLine[0])
        city.append(splitLine[1])
        state.append(splitLine[2].rstrip())

    inZIP.close()

    inStreet = open(streetFileName,"r")

    print("Loading and parsing street names data set...")
    # bring in data from street name dataset
    # Need to rstrip() to remove carraige return
    for lineStreet in inStreet:
        street.append(lineStreet.rstrip())

    inStreet.close()
    
    inStreetType = open(streetTypeFileName,"r")

    print("Loading and parsing street types data set...")
    # bring in data from street type dataset
    # Need to rstrip() to remove carraige return
    for lineStreetType in inStreetType:
        streetType.append(lineStreetType.rstrip())

    inStreetType.close()

    # processNames will open files and load values
    chineseLast, japaneseLast, koreanLast, indianLast, arabicLast, spanishLast, americanLast = processName(lastFileName)
    chineseFirst, japaneseFirst, koreanFirst, indianFirst, arabicFirst, spanishFirst, americanFirst = processName(firstFileName)

    numClients = int(input("Enter number of values to generate: "))

    lenClients = len(str(numClients))

    # Start by creating schema and creating table
    outFile.write("CREATE SCHEMA studentTest;\n")
    outFile.write("CREATE TABLE Client (\n")
    outFile.write("    ClientNum CHAR(")
    # Use the number of digits in the user's input to determine length of ClientNum
    outFile.write(str(lenClients))
    outFile.write(") PRIMARY KEY,\n")
    # If I have time, parse array for longest value and use that instead of 15
    outFile.write("    LastName CHAR(15),\n")
    outFile.write("    FirstName CHAR(15),\n")
    outFile.write("    ClientName CHAR(35) NOT NULL,\n")
    outFile.write("    Street CHAR(20),\n")
    outFile.write("    City CHAR(15),\n")
    outFile.write("    State CHAR(2),\n")
    outFile.write("    ZIPCode CHAR(5),\n")
    outFile.write("    Email CHAR(75),\n")
    outFile.write("    Phone CHAR(10)\n")
    outFile.write(");\n")


    # Maybe pad the clientNumber?
    for loopCounter in range(numClients):
        ethnicity = ethnicityTypes[random.randint(0,6)]
        fnameRandom = random.randint(0,19)
        lnameRandom = random.randint(0,19)
        
        command = ethnicity + "First[" + str(fnameRandom) + "]"
        firstNameValue = eval(command)

        command = ethnicity + "Last[" + str(lnameRandom) + "]"
        lastNameValue = eval(command)

        # Could do this with global variables or passing lists but it felt sloppy
  
        location = random.randint(0,len(zip)-1)
        streetValue = random.randint(0,len(street)-1)
        streetTypeValue = random.randint(0,len(streetType)-1)
        outFile.write("INSERT INTO Client VALUES (\"" +
                      str(loopCounter + 1) +
                      "\", \"" +
                      lastNameValue +
                      "\", \"" +
                      firstNameValue +
                      "\", \"" +
                      str(random.randint(100,9999)) +
                      " " +
                      street[streetValue] +
                      " " +
                      streetType[streetTypeValue] +
                      "\", \"" +
                      city[location] +
                      "\", \"" +
                      state[location] +
                      "\", \"" +
                      zip[location] +
                      "\", \"" +
                      generateEmail(firstNameValue,lastNameValue) +
                      # Need to generate phone and email
                      "\", \"" +
                      str(random.randint(200,999))+"-"+str(random.randint(200,999))+"-"+str(random.randint(1000,9999)) +
                      "\")\n")
    # Close the output
    outFile.close()

    mydb = mysql.connector.connect(
      host="cis.pccc.edu",
      user="ecameron",
      password="realpassword",
      database="ecameron"
    )

    print("Complete!")

# This is here in case I decide to use this as a library for another program    
if __name__ == "__main__":
    main()

