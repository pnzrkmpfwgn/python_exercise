import time
import random

hare_speed = 0
tortoise_speed = 0
tortoise_position = 0
hare_position = 0

def hare():
    hare_possibility =  random.randint(1,10)
    return hare_possibility

def tortoise():
    tortoise_possibility = random.randint(1,10)
    return tortoise_possibility

def hare_speed(speed):
    global hare_speed
    hare_speed = speed

def tortoise_speed(speed):
    global tortoise_speed
    tortoise_speed = speed

def calculate_tortoise_speed():
    possibility = tortoise()
    if(possibility == 1 or possibility == 2 or possibility == 3 or possibility == 4 or possibility == 5):
        return 3
    elif(possibility == 6 or possibility == 7):
        if(tortoise_position==0):
            return 0
        else:
            return -6
    elif(possibility == 9 or possibility == 10):
        return 0
    else:
        return 0

def calculate_hare_speed():
    possibility = hare()
    if(possibility == 1 or possibility == 2):
        return 9
    elif(possibility == 3):
       if(hare_position == 0):
           return 0
       else:
           return -12
    elif(possibility == 4 or possibility == 5 or possibility == 6):
        return 1
    elif(possibility == 7 or possibility == 8):
        if(hare_position==0):
            return 0
        else:
            return -1
    elif(possibility == 9 or possibility == 10):
        return 0
    else:
        return 0
print("BANG !!!")
print("AND THEY ARE OFF!!!!")

T=""
H=""
j=0
k=0
b=True


for i in range(70):
    time.sleep(1)
    Tspeed = calculate_tortoise_speed()
    Hspeed = calculate_hare_speed()
    tortoise_position = tortoise_position +  Tspeed
    hare_position = hare_position + Hspeed
    Tspeed = 0
    Hspeed = 0
    if(tortoise_position > 0):
        while j < tortoise_position:
            if(Tspeed < 0):
                T=T-"▪"
            else:
                T= T + "▪"
                j=j+1
        print("T " + T)
    else:
        tortoise_position = 0
    if(hare_position > 0):
        while k < hare_position:
            if(Hspeed < 0):
                H = H - "▪"
            else:
                H= H + "▪"
                k=k+1
        print("H " + H)
    else:
        hare_position = 0
    if(len(H) == len(T)):
        print("OUCH !!!")
    if(len(H) == 70 and len(T) == 70):
        print("It's a tide")
        break
    if(len(H) > 70):
        print("HARE WINS !!!")
        b=False
        break
    if(len(T) > 70):
        print("TORTOISE WINS !!")
        b=False
        break

if(b and len(H) > len(T)):
    print("HARE WINS !!")
elif(len(T) > len(H)):
    print("TORTOISE WINS !!")


#▪