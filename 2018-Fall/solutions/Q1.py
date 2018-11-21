def rot_1(A, d): 
    output_list = [] 
      
    # Will add values from n to the new list 
    for item in range(len(A) - d, len(A)): 
        output_list.append(A[item]) 
      
    # Will add the values before 
    # n to the end of new list     
    for item in range(0, len(A) - d):  
        output_list.append(A[item]) 
          
    return output_list 

def rot_2(A, d):
    return (A[-d:] + A[:-d])
    
A = [1, 2, 3, 4, 5, 6, 7] 
d = 2

print rot_1(A, d)
print rot_2(A, d)