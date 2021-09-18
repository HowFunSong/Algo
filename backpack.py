from collections import deque




#建立物品列表
item_list = deque()
item_list.append("Gitar")
item_list.append("Sound")
item_list.append("NB")
# item_list.append("Iphone")

# print(item_list)
# item = item_list.popleft()


#建立item的價值[0] 、重量[1]
list_data = {}
list_data["Gitar"] = [1500,1]
# print(list_data[item][0])
list_data["Sound"] = [3000,4]
list_data["NB"] = [2000,3]
# list_data["Iphone"] = [2000,1]


#新增物件
Add = input("Do you want add ? (Y/N) : ")
while Add == 'Y' :
    new_item = (input("New item name? : "))
    item_list.append(new_item)
    new_item_value = int(input("New item value : "))
    new_item_weight = int(input("New item weight : "))
    list_data[new_item]=[new_item_value,new_item_weight]
    break


#最大負重
Maxload = 4
# Maxload_change = input("Do you Want change MaxLoading(Y/N)?(Default:4) : ")
# if Maxload_change == 'Y' :
#     Maxload = input("New MaxLoading ? : ") 

Ini = 0

#先根據item數目、最大負重，宣告一個2維陣列矩陣 初始化為0
# loadvalue = [0]*Maxload
# valuetable = [
#                 [0,0,0,0],
#                 [0,0,0,0],
#                 [0,0,0,0],
#              ]
#利用列表生成式
valuetable = [[0 for x in range(Maxload)] for j in range(len(list_data))]


# print(valuetable)
# print(len(list_data))

i = 0 #項目
while i < len(list_data) and len(item_list) >= 1:
    item = item_list.popleft()
    value = list_data[item][0]
    weight = list_data[item][1]
    tempvalue = 0
    j = 1 #負重
    while j <= Maxload:
        #將list第一個項目pop出來檢查，紀錄value weight 
        if i == 0 :
            if j >= weight :
                valuetable[i][j-1] = value
                j += 1
                continue

               
        if j < weight:
            valuetable[i][j-1]= valuetable[i-1][j]
        elif j-weight == 0:
            tempvalue = value
        else:
            tempvalue = value + valuetable[i-1][j-1-weight]


        if tempvalue >= valuetable[i-1][j-1]:
            valuetable[i][j-1] = tempvalue
        else:
            valuetable[i][j-1]= valuetable[i-1][j-1]       
        j += 1
    i+=1

print("------The Highest Value You Can Get------")
print(valuetable[len(list_data)-1][Maxload-1])





#要如何找出所拿的物品
row = len(list_data)-1
colu = Maxload-1
# print(y,x)

key_list =[]
for key in list_data.keys():
    key_list += [key]
# print(key_list)
take_list =[]
while row >= 0 and colu >= 0:

    if row == 0 and valuetable[row][colu] != 0:
        take_list = [key_list[row]] + take_list
    if valuetable[row][colu] > valuetable[row-1][colu]:
        take_list = [key_list[row]] + take_list
        colu -= list_data[key_list[row]][1]

    row -= 1
   

print(f"The Item You Got : {take_list}")












