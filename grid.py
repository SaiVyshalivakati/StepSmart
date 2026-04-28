store = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,0,1],
    [1,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,1,0,1,1,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]          

items={ "Vegetables":(4,4),
         "Fruits":(2,9),
         "Coffee":(6,6),
         "Meat":(9,9),
         "Bakery":(8,6)}

def basegrid(store,items):
    for i,line in enumerate(store):
        for j,cell in enumerate(line):
                itempos=None
                for name,(r,c) in items.items():
                    if r==i and c==j:
                        itempos=name

                if itempos:
                    print(itempos,end=" ")

                elif cell==1:
                    print("\u2588",end=" ")

                else:
                    print("*",end=" ")

        print()
                    

basegrid(store,items) 

def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

print(heuristic((0,0),(6,6)))