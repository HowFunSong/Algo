from collections import deque


graph = {}
graph["You"]=["Alice","Risa","John"]
graph["Alice"] = ["Shawn", "Jack"]
graph["Shawn"] = ["Sam"]
graph["Jack"] = ["Erica"]
graph["Risa"] = ["Erica"]
graph["John"] = []

applesellar = ["Erica","Sam"]


def person_is_seller(person):
    if person in applesellar :
        return True
    else:
        return False

# print(person_is_seller("Erica"))


def Searchseller(nam):
    search_queue = deque()
    search_queue += graph[nam]
    searched = []

    while search_queue :
        person = search_queue.popleft()
        # print (searched)
        if person not in searched:
            if person_is_seller(person) :
                print(person + " is Apple salesman")
                return True
            else : 
                search_queue += graph[person]
                searched.append(person)
    return False
Searchseller("You")









