def songPairs_1(A): # O(n^2)
    count = 0

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            a = A[i] + A[j]
            if (a % 60 == 0):
                count += 1
    return count


def songPairs_2(A): # O(n)
    mem = [0]*60
    for a in A :
        mem[a%60] += 1

    count = mem[0]*(mem[0]-1)//2
    for i in range(1,(60+1)//2) :
        count += mem[i]*mem[60-i]

    if 60%2 == 0:
        count += mem[60//2]*(mem[60//2]-1)//2

    return count

A = [30, 20, 150, 100, 40]

print(songPairs_1(A)) 
print(songPairs_2(A)) 


'''
songPairs_2 explanation: 

Lets break it down to a simpler problem:
[6 4 7 9 8 3 17 12] and k = 4 (instead of 60)

Values with remainder 0, can be paired with themselves. That's because even after addition
 the remainder will remain 0. If there are c such integers, no. of pairs = c*(c-1)/2

Values with remainder r can be paired with values with remainder k-r, since, remainder of 
sum becomes k i.e. 0. In above example, values with remainder 1 and 3 can be paired : 
(9,3), (9,7), (17,3), (17,7). Total number of pairs = product of counts.

Finally, values with remainder exactly k/2, can be paired with themselves 
(Calculation same as remainder 0 values).
'''
