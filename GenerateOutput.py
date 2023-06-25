#This helps generate the ouput we use in both the console application and the GUI
def generateOutput(mode, user_entered2, path2Lists, path1Lists):
    output = []
    subject = '';
    classmark = '';
    floor = '';
    ##iterate based on mode 
    if mode == 3:
        #get the location
        for location in path2Lists :
            if(user_entered2.lower() in location[0].lower()):
                for i in range(len(location)):
                    if(i == 0):
                        floor = location[i]
                        continue
                    classmark = location[i]
                    for subjects in path1Lists:
                        for j in range(len(subjects)):
                            if(j ==0):
                                subject = subjects[j]
                                continue
                            if(classmark == subjects[j]):
                                output.append(subject+" | "+ classmark+" | "+floor)
    
   ##iterate based on mode 
    if mode == 1:
        #get the classmark
        for subjectname in path1Lists :
            if (user_entered2.lower() in subjectname[0].lower() ):
                for i in range(len(subjectname)):
                    if(i == 0):
                        subject = subjectname[i]
                        continue
                    classmark = subjectname[i]
                    for loc in path2Lists:
                        #we have the book
                        for k in range(len(loc)):
                            #searching the book leaflet afer leaflet
                            if(k ==0):
                                floor = loc[k]
                                continue
                            if(classmark == loc[k]):
                                output.append(subject+" | "+ classmark+" | "+floor)


 ##iterate based on mode 
    if mode == 2:
        #get the subject name
        for lineitem in path1Lists :
                for m in range(len(lineitem)):
                    if(m == 0):
                        subject = lineitem[m]
                        continue
                    if(user_entered2.lower() in lineitem[m].lower()):
                        classmark = lineitem[m]
                        for location_line_item in path2Lists:
                            #we have the book
                            for k in range(len(location_line_item)):
                                #searching the book leaflet afer leaflet
                                if(k ==0):
                                    floor = location_line_item[k]
                                    continue
                                if(classmark == location_line_item[k]):
                                    output.append(subject+" | "+ classmark+" | "+floor)
    
    return output