##list
myList=['1','4',5]
##list can be changed
myList[0]='word'
print(myList)
##list can contain list
myList1=[
    [ ],[]
]

##list comprehension
fruits=['apple','banana','cherry']
newFruits=[]
for fruit in fruits:
    if 'a' in fruit:
        newFruits.append(fruit)
print(newFruits)
newList=[x for x in fruits if 'e' in x]
print(newList)
