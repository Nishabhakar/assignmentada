import time
import random

#merge sort function!
def merge(arr, l, m, r):

    n1 = m - l + 1

    n2 = r - m
 

    # creating another empty arrays
    L = [0] * (n1)

    R = [0] * (n2)
 

    #taking data to arrays L[] and R[]

    for i in range(0, n1):
        L[i] = arr[l + i]
        
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        
    i = 0     
    j = 0    
    k = l    
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
def mergeSort(arr, l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
  
# main function

#starting time
start = time.time()
arr=[]

n= int(input("enter ur size:"))
print("enter ur elements:")
for i in range(0,n):
	num = random.randint(0,n)
	arr.append(num)

print("Given array is")

for i in range(n):
    print("%d" % arr[i]),
 
mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print("%d" % arr[i])
    
end = time.time()

#total time taken
print(f"runtime of the program is{end - start}")
[12:33, 27/09/2021] Nishi Bhakar😊: import time
import random
def BubbleSort(arr,n):
    if(n>0):
        for i in range(0,n):
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
        BubbleSort(arr, n - 1)
arr=[]
n = int(input("Enter the size of the array: "))
#starting time
start = time.time()
print("Enter the Element of the array:")
for i in range(0,n):
    num = random.randint(0,n)
    arr.append(num)

BubbleSort(arr, n - 1)
print("After Sorting Array Elements are:")
for i in range(0,n):
    print(arr[i],end=" ")
  
end = time.time()   
#total time taken
print(f"runtime of the program is{end - start}")
