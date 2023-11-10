file_path = 'text.txt'

Data = []
# Open the file in read mode
with open(file_path, 'r') as file:
    for line in file:
        a = (line.strip())
        Data.append(a)

#print(Data) #debug text

pattern = list(Data[2].split())
stringSet = list(Data[3].split())


def findmatchLR():
    for i in range(len(stringSet)-1):
        for j in range(len(pattern)):
            if i < len(stringSet) :
                # print("i =",stringSet[i],"j =",pattern[j]) ## debug text
                if stringSet[i] == pattern[j]:
                    i+=1
                    if j == len(pattern)-1:
                        print((i-j),"LR")
                        # print("Found 1 match pattern at position",i-j,"finding more pattern at position",(i-j)+1 ) #debug text
                else:
                    # print("String unmatch, finding new position....") #debug text
                    break
            else:
                # print("String unmatch, finding new position....") #debug text
                break

    # print("End of stringset from left to right")

def findmatchRL():
    rStringSet = stringSet[::-1]
    for i in range(len(rStringSet)-1):
        for j in range(len(pattern)):
            if i < len(rStringSet) :
                print("i =",stringSet[i],"j =",pattern[j]) ## debug text
                if rStringSet[i] == pattern[j]:
                    i+=1
                    if j == len(pattern)-1:
                        print((i-j),"RL")
                        print("Found 1 match pattern at position",i-j,"finding more pattern at position",(i-j)+1 ) #debug text
                else:
                    print("String unmatch, finding new position....") #debug text
                    break
            else:
                print("String unmatch, finding new position....") #debug text
                break

    # print("End of stringset from right to left")



findmatchLR()
findmatchRL()