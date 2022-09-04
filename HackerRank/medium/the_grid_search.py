def gridSearch1(G, P):
    # Write your code here
    index_start = -1
    for string in G:
        index_start += 1
        if P[0] in string:
            break
    new_array = G[index_start:index_start+len(P)]
    result = 'NO' 
    index_check = 0
    for string in P:
        if string in new_array[index_check]:
            result = 'YES' 
        else:
            result = 'NO' 
            break
        index_check += 1
    return result

array1 = ['7283455864', '6731158619', '8988242643', '3830589324', '2229505813', '5633845374', '6473530293', '7053106601', '0834282956', '4607924137']
pattern1 = ['9505', '3845', '3530']
array2 = ['34889246430321978567', '58957542800420926643', '35502505614464308821', '14858224623252492823', '72509980920257761017', '22842014894387119401', '01112950562348692493', 
'16417403478999610594', '79426411112116726706', '65175742483779283052', '89078730337964397201', '13765228547239925167', '26113704444636815161', '25993216162800952044', 
'88796416233981756034', '14416627212117283516', '15248825304941012863', '88460496662793369385', '59727291023618867708', '19755940017808628326']
pattern2 = ['1641', '7942', '6517', '8907', '1376', '2691', '2599']
array3 = ['1234', '4321', '9999', '9999']
pattern3 = ['12', '21']
array7 = ['123412', '561212', '123634', '781288']
pattern7 = ['12', '34']

def gridSearch2(G, P):
    index_found = -1
    for string in G:
        index_found += 1
        if P[0] in string:
            break 

    index_start = G[index_found].index(P[0])
    
    # Create new array
    new_array = []
    for substring in G[index_found:index_found+len(P)]:
        new_array.append(substring[index_start:index_start+len(P[0])])
    
    # Check if array is same with pattern
    output = 'NO'
    for n in range(len(new_array)):
        if P[n] == new_array[n]:
            output = 'YES'
        else:
            output = 'NO'
            break

    return output

def gridSearch3(G, P):
    
    for string in G:
        print(string)


# print(gridSearch(array1, pattern1))
# print(gridSearch(array2, pattern2))
# print(gridSearch(array3, pattern3))
print(gridSearch3(array7, pattern7))