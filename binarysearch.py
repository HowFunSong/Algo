def binarysearch(list,target):
    low = 0 
    high = len(list) - 1

    while low <= high :
        mid = int((low + high)/2)
        if list[mid] == target :
            return mid
        elif list[mid] < target :
            low = mid + 1
        elif list[mid] > target :
            high = mid - 1
    
    return None

my_list = [1,3,5,6,9,11,23,56,67,75,76,79]
search = input("what value do you want to search ： ")
if binarysearch(my_list,int(search)) == None :
    print("There is no matched value")
else :
    print(f"The value you wanna find , index is {binarysearch(my_list,int(search))}")