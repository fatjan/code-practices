# Write your code here
new_line = input()
l1 = [int(x) for x in new_line.split(" ")]
# div = l1[2]
# result = []
# for i in range(l1[0],l1[1]+1):
#     for j in range(l1[0],l1[1]+1):
#         if i % div == 0 and j % div == 0:
#             pair = [i,j]
#             if pair not in result:
#                 result.append(pair)
# print(result)
# print(len(result))

def gcd(a,b): 
  
    return gcd(b, a % b) if b>0 else a 
  
   
# Return the count of pairs 
# having GCD equal to g. 
def countGCD(L,R,g): 
  
    # Setting the value of L, R. 
    L = (L + g - 1) // g 
    R = R// g 
   
    # For each possible pair 
    # check if GCD is 1. 
    ans = 0
    for i in range(L,R+1): 
        for j in range(L,R+1): 
            if (gcd(i, j) == 1): 
                ans=ans +1
   
    return ans 
  
# Driver code 
# 1 11 5
L = l1[0]
R = l1[1]
g = l1[2]
  
print(countGCD(L, R, g)) 