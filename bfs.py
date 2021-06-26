from collections import deque
graph = dict(
    you=['alice', 'bob', 'claire'],
    bob=['peggy', 'anuj'],
    alice=['peggy'],
    claire=['thom', 'jonny'],
    peggy=[],
    anuj=[],
    thom=[],
    jonny=[]
)


def person_is_seller(name):
    return name[-1] == 'm'


def bfs(name):
    search_queue = deque()
    search_queue += graph[name]  # use plus sign to concat two lists
    searched = []  # list to record searched person
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + ' is a mango seller')
                return person
            else:
                search_queue += graph[person]
                searched.append(person)
    print('No mango seller in your network')
    return -1


bfs('you')
