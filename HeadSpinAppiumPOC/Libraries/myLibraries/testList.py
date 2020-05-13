list1=['1','2','3','4','5','6','7']
list2=['a','b','c']

list3=[]

diff=len(list1)-len(list2)
for i in range(diff): 
    list2.append("")   
    
def join_lists(firstList, secondList):
    for x,y in zip(firstList,secondList):
        list3.append(x+y)
    print(list3)    


join_lists(list1,list2)        
    