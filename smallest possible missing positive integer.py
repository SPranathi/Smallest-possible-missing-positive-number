"""
Smallest possible missing positive integer

In a given List of unsorted values of length (n-1) , 
print the smallest missing positive integer of the list and the resultant list with missing value of length n.
Note: Positive integers start from 1 (not from zero)

Input = 
4           ---- n=4.
1 2 0       ---- read n-1 values.
Output = 
3           ---- print smallest possible missing positive integer.
0 1 2 3     ---- print the sorted resultant list with missing value(sorted order) of length n.    

--------------------------
    
Input = 
5           ---- n=5.
3 4 -1 1    ---- read n-1 values.
Output = 
2           ---- print smallest possible missing positive integer.
-1 1 2 3 4  ---- print the sorted resultant list with missing value(sorted order) of length n.

--------------------------

Input = 
6
7 8 9 11 12
Output = 
1
1 7 8 9 11 12

---------------------

Input = 
8
18 1 15 3 5 4 17
Output = 
2
1 2 3 4 5 15 17 18
 """
n=int(input())
a=[int(x) for x in input().split(" ")]

for i in range(1,10):
    if i not in a:
        c=n
        if(i<c):
            c=i
            break
    else:
        c=0
print(c)
a.append(c)
b=sorted(a)
str1=' '.join(map(str,b))
print(str1)
 
