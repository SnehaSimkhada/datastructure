#!/usr/bin/env python
# coding: utf-8

# In[9]:


#linear algorithm: It is an sequential algorithm. 

def linear_search(list, target):
   #  Returns the index position of the target if found, else returns None
    
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None
    
def verify(index):
    if index is not None:
        print("target found at the index: ", index)
    else:
        print("target not found in the list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers,8)
verify(result)


# In[10]:


#binary search
#iterative method
#space complexity:  O(1)
#iterative is better in pythjon because it takes constant space

def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        mid = (first + last) // 2
        
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid +1
        else:
            last = mid -1
    return None

def verify(index):
    if index is not None:
        print("target found at the index: ", index)
    else:
        print("target not found in the list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers,8)
verify(result)

result = binary_search(numbers,12)
verify(result)


# In[13]:


#recursive binary search
#recursive method
# here it grabs itself
#O(log n)

def recursive_binary_search(list, target):
    if len(list) ==0:
        return False
    else:
        mid = (len(list))//2
        if list[mid] == target:
            return True
        else:
            if list[mid] <target:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid],target)

def verify(result):
    print("Target found:", result)
    
numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers,8)
verify(result)

result = recursive_binary_search(numbers,12)
verify(result)


# In[ ]:


#arrays 
# they are bad at inserting and deleting so we have linked list 
new_list= [1,2,3]
result = new_result[0]

if 1 in new_list: print(True)
    
num_list.append(4) #allocates memmory to the list and adds to it
num_list.extent([5,6]) #extends the list 


# In[ ]:





# In[21]:


#merge Sort

#divide and conquere

def merge_sort(list):
    #sorts a list in an ascending order
    #return a new sorted list
    #Divide: we find the midpoint of the list and devide it to sub list
    #conquer : recursively sort the sublists created in the preveous step
    #combine: merge the sorted creates in prev step
    # takes overall O(n log n) time
    
    if len(list) <=1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)

def split(list):
    #divide the unsorted list at miudpoint into sublists
    #return two sublists - left and right
    # takes overall O(log n) time
    
    mid =len(list)//2
    left = list[:mid]
    right= list[mid:]
    
    return left, right

def merge(left, right):
    #merges lists or arrays sorting them in the process
    #returns a new merges list
    # takes overall O(n) time
    
    l=[]
    i=0
    j=0
    
    while i< len(left) and j <len(right):
        if left[i]< right[j]:
            l.append(left[i])
            i +=1
        else:
            l.append(right[j])
            j += 1
    
    while i < len(left):
        l.append(left[i])
        i+=1
        
    while j< len(right):
        l.append(right[j])
        j+=1
        
    return l

def verify_sorted(list):
    n = len(list)
    
    if n ==0 or n ==1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

alist = [54,62,93,17,77,31,44,55,20]
l= merge_sort(alist)
print(verify_sorted(alist)) 
print(verify_sorted(l)) 


# In[ ]:





# In[ ]:




