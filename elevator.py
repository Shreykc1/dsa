from time import sleep
global current_floor

def lift(press):
    global current_floor
    simulate(5)
    while True:
        if current_floor:
            print(current_floor)
            pressed = sorted(press)
            if current_floor in pressed:
                pressed.pop(current_floor)
            if len(pressed) == 0:
                print("All Floors occupied")
                break
            return pressed
     


def simulate(n): 
    global current_floor
    for i in range(0,n+1):
        print(i)
        current_floor = i
        n+=1
        sleep(1)


          









pressed = [2,5]

lift(pressed)
