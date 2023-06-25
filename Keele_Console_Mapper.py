from GenerateOutput import generateOutput
from ReadMyFile import ReadMyFile


path1 = 'firstFile.csv'
path2 = 'secondFile.csv'


path1Lists = ReadMyFile(path1)
path2Lists = ReadMyFile(path2)

locations = []


def KeeleLib_Map():
   
   # print("Please enter a subject name, a classmark or a location")
    print("Please Select an Option")
    print("1. SubjectName")
    print("2. ClassMark")
    print("3. Location")
    
    user_entered  = input()
    

    mode = 0 # mode is used to track user input

    if (user_entered == '1') | (user_entered.lower() == "subjectname") :
        print("Please Enter Subject Name")
        mode = 1
    elif (user_entered == '2') | (user_entered.lower() == "classmark"):
        print("Please Enter ClassMark")
        mode = 2
    elif (user_entered == '3') | (user_entered.lower() == "location"):
        mode = 3
        print("Please Select a Location")
        i = 1
        #loop through location file to get locations
        for location in path2Lists:
            print(str(i) +'.'+location[0])
            locations.append(location[0])
            i+=1
    else:
        print ("Invalid option entered!!!")


    user_entered2 = input()
    userinput =''
    if mode ==3:
        userinput = locations[int(user_entered2)-1]
    else:
        userinput = user_entered2

    output = generateOutput(mode, userinput, path2Lists, path1Lists)
    if(len(output) < 1): print ("Data not found")
    for outpt in output: print (outpt)



KeeleLib_Map()

input("press enter to exit;")



