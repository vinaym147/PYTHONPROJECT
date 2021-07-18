#!/usr/bin/env python
# coding: utf-8

# In[2]:


lst = [1,3,2,4,5,6,9,8,7,10] #declaring the array of numbers to be sorted/searched
lst.sort() #use of the sorting function
first=0
last=len(lst)-1
mid = (first+last)//2
item = int(input("enter the number to be search")) #taking the  input from the user.the number that is to be searched 
found = False #initially assigning that number is not found
while( first<=last and not found):# use of the while loop to determine the location of the number to searched
    mid = (first + last)//2 # finding the middle term.
    if lst[mid] == item :
         print(f"found at location {mid}")
         found= True
    else:# in the else loop the comparison of the item and the middle number is done
        if item < lst[mid]:
            last = mid - 1 
        else:
            first = mid + 1 
   
if found == False:#even after searching if the number is noy found returning false
    print("Number not found")#printing that number is not found and it declares that the required is not present in the list


# In[ ]:




