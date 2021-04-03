def bacaTextFIle(x):
    f = open(x,'r') 
    file = f.readlines()
    operand = []
    #melakukan replace beberapa character seperti koma, titik, dan newline
    for lines in file:
        lines = lines.replace("\n"," ")
        operand.append(lines)
    opfinal = []
    for lines in operand:
        lines = lines.split()
        opfinal.append(lines)
    return opfinal

def tetangga(x):
    matrix = []
    for i in range(2,len(x)):
        for j in range(len(x[0])):
            if(int(x[i][j]) > 0):
                matrix.append((x[0][i-2],x[0][j]))
    return matrix

def coordinates(x) :
    matrix =[]
    print(x[1])
    specChar = ['(', ')', ',']
    for loc in x[1]:
        loc = loc.replace('(',' ')
        loc = loc.replace(')',' ')
        loc = loc.replace(',',' ')
        matrix.append(loc)
    print("coordinates : ")
    print(matrix)
    loc = []
    for lines in matrix :
        lines = lines.split()
        loc.append(lines)
    return loc

def jarak(x, y):
    
arr = []
arr = bacaTextFIle("test.txt")
print(arr)
arrNeigh = []
arrNeigh = tetangga(arr)
print(arrNeigh)
loc = []
loc = coordinates(arr)
print(loc)