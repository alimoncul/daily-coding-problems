'''
238. Product of Array Except Self #https://leetcode.com/problems/product-of-array-except-self/
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
def productExceptIndex(liste):
    solArray,sagArray=liste[:],liste[:]
    sonArray=[]
    
    eleman=1
    for i in range(len(liste)):
        solArray[i]=eleman
        eleman=eleman*liste[i]
        
    eleman=1
    for j in range(len(liste)-1,-1,-1):
        sagArray[j]=eleman
        eleman=eleman*liste[j]
    
    for k in range(len(liste)):
        sonArray.append(solArray[k]*sagArray[k])
        
    return sonArray