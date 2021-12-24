list1=["Mike","","Emma","Kelly","","Brad"]
list2=["My","name","is","Kelly"]
list3=list1+list2

print(list3)

list3.reverse()
print(list3)

list3.remove("")
print(list3)

list3.remove("")
print(list3)

list3=list(dict.fromkeys(list3))
print(list3)

list3.append(50)
print(list3)
