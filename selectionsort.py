def selectsort(arr):
    sorted_arr = []
    
    while len(arr) != 0 :
        i = 0
        index = 0
        min = arr[0]
        while i < len(arr) :
            if arr[i] < min:
                min = arr[i]
                index = i
            i += 1
        sorted_arr.append(arr.pop(index))

    return sorted_arr

def creating_arr():
    new_arr = []

    while True :
        num = input("Add a num to arr(00 for quit) : ")
        if num == "00" :
            return new_arr
        new_arr.append(int(num))
        
# unsort_arr = [1,9,25,10,6,7,4,45,21]
new_arr = creating_arr()
print(new_arr)
print("------Sorted------")

print(selectsort(new_arr)) 
        


