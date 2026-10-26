import time

print("-----Sorting Techniques-----")
print("Choose-1 = Selection Sort")
print("Choose-2 = Insertion Sort")
print("Choose-3 = Bubble Sort")
print("Choose-4 = Merge Sort")
print("Choose-5 = Quick Sort")
choice=int(input("Enter your sorting choice: "))
start=time.time()

#SELECTION SORT
def selection_sort(arr):
    for i in range(0,len(arr)):
        min=arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                arr[j]=arr[i]
                arr[i]=min
    return arr

#INSERTION SORT
def insertion_sort(arr):
    for i in range(1,len(arr)): 
        key=arr[i] 
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

    return arr

#BUBBLE SORT
def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-1):        #also range(0,len(arr)-1-i) as the iterations completed that many no's are sorted no need to compare again
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr


#MERGE SORT
def merge(arr,st,mid,n):
    temp=[]
    i=st
    j=mid
    while i < mid and j < n:
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    for k in range(i,mid):
        temp.append(arr[k])
    for k in range(j,n):
        temp.append(arr[k])
    return temp
def merge_sort(arr,st,n):
    mid=(st+n)//2
    if(n-st)<=1:
        return arr
    merge_sort(arr,st,mid)
    merge_sort(arr,mid,n)
    temp=merge(arr,st,mid,n)
    arr[st:n] = temp
    return arr
    


#QUICK SORT
def quick_sort(arr,st,n):
    p=arr[n-1]
    i=st-1
    if n-st<=1:
        return arr
    for j in range(st,n-1):
        if arr[j]<p:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[i+1],arr[n-1]=arr[n-1],arr[i+1]
    pivot_index=i+1
    quick_sort(arr,st,pivot_index) 
    quick_sort(arr,pivot_index+1,n)
    return arr



arr=list(map(int,input().split()))

if choice==1:
    print("Sorted array through Selection sort.")
    print(selection_sort(arr))
elif choice==2:
    print("Sorted array through Insertion sort.")
    print(insertion_sort(arr))
elif choice==3:
    print("Sorted array through Bubble sort.")
    print(bubble_sort(arr))
elif choice==4:
    print("Sorted array through Merge sort.")
    merge_sort(arr,0,len(arr))
    print(arr)
elif choice==5:
    print("Sorted array through Quick sort.")
    n=len(arr)
    print(quick_sort(arr,0,n))
else:
    print("Please, Enter a valid choice.")

end=time.time()
elapsed=end-start
print("Total time taken is ", elapsed)

