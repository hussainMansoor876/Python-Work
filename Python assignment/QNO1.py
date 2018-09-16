rab=1
head=35
for value in range(1,36):
    head=35
    chik=(head-rab)
    chikl=chik*2
    rabl=rab*4
    if(chikl+rabl==94):
        break
    rab+=1
print("In 94 leg and 35 heads")
print("Chickens=",chik)
print("Rabbit=",rab)