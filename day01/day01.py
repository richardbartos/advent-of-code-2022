import os.path

#setup list of sums for each elf
mapElfCalories = []

with open(os.path.join(os.path.dirname(__file__), 'data.txt')) as fh:

    singleElfCalories = []
    
    for line in fh.readlines():
        line = line.strip()
        
        if line == "":
            mapElfCalories.append(sum(singleElfCalories))
            singleElfCalories = []
        else:
            singleElfCalories.append(int(line))
    
    #Add the last elf to the map as the "" is missing on the last line 
    mapElfCalories.append(sum(singleElfCalories))

print("Elf with most calories:")
print(max(mapElfCalories))

print("Top 3 with most calories:")
mapElfCalories.sort(reverse=True)
print(mapElfCalories[0]+mapElfCalories[1]+mapElfCalories[2])
