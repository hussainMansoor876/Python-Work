pos={'x':0,'y':0}
while True:
    line=input(">")
    if not  line:
        break
    direction,step=line.split()
    if direction=="UP":
        pos['y']+=int(step)
    elif direction=="DOWN":
        pos['y']-=int(step)
    elif direction=="LEFT":
        pos['x']-=int(step)
    elif direction=="RIGHT":
        pos['x']+=int(step)
print(int(round(pos['x']**2+pos['y']**2)**0.5))