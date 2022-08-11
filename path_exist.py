#importing the math module required for square checking
import math
 
#this method is used for perfect square checking of the sum of co-ordinates
def isPerfectSquare(x):
    #checking whether the  number is positive or ot
    if(x >= 0):
        #finding the square root
        sr = int(math.sqrt(x))
       #checking whether it is square root or not and returning
        return ((sr*sr) == x)
    return False
#Main function for checking whether path is possible or not    
#(a,b) is the starting index and (x,y) is the destination index and "c" is the constant
def canReach(c,a,b,x,y):
    # finding the maximum co-ordinate for defining table dimensions
    k=max(a,b,x,y)
    #defining a two dimensional matrix for the dynamic programming technique
    d=[[0 for i in range(k+1)] for j in range(k+1)]
    #declaring the co-ordinate of starting variable as reachable 
    d[a][b]=1
    #looping through every co-ordinate 
    for i in range(a,k+1):
        for j in range(b,k+1):
            #checking if it is perfect square or starting point
            if isPerfectSquare(i+j) or (i==a and j==b):
                continue
            #checking if it is reachable from the previous point of constant
            elif (i-c)>-1 and (j-c)>-1 and d[i-c][j-c]==1:
                d[i][j]=1 
            #checking if it is reachable from the below or left below point
            elif d[i-j][j]==1 or d[i][j-i]==1:
                d[i][j]=1
    #returning yes if the co-ordinate is reachable            
    if d[x][y]==1:
        return "Yes"
    #returning false if the co-ordinate is not reachable
    return "No"   
#calling the main function    
print(canReach(1,7,9,8,10))   