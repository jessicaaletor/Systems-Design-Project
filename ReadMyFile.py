import csv

def ReadMyFile(pathString):
     pathLists = []

     with open(pathString,'r') as mycsvFile:
        reader = csv.reader(mycsvFile)
        
        for row in reader:
            pathLists.append(row)
     return pathLists
