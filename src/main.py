from astar import bacaTextFile, listOfNode, tetangga, coordinates, jarak, matrixJarak, getNeighbour, getIdx, sortingFn, closestPath, getMinFn, derivate
              
filename = str(input("Masukkan nama file : "))
fileDir = "../test/" + filename
arr = bacaTextFile(fileDir)
listNode = listOfNode(arr) #['A', 'B', 'C', 'D', ...] A,B,C,D,... adalah node 
arrNeigh = tetangga(arr,listNode) # [('A', 'B'), ('A', 'C'), ...] B tetangga A, C tetangga A
loc = coordinates(arr) # [['1', '2'], ['2', '1'], ['1','1'], ...] elmt pertama adalah ada latitude, dan kedua adalah longitude
matrixDistance = matrixJarak(arr, loc)
# 0 2 1
# 2 0 2
# 1 2 0
src = str(input("Masukkan node awal : ")) # A
dest = str(input("Masukkan node tujuan : ")) # G
jalan = closestPath(src, dest, arrNeigh, matrixDistance, listNode) # [('A', 0), ('B', 20.62), ('G', 159.84)], elmt kedua dari tuple dalam satuan meter
print(jalan)
