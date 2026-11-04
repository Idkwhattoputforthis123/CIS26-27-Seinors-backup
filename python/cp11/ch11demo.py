# variables arth importing modules

# Demo one variables and assingment
def demo1_variables():
    CAN_VOLUME = 0.335
    BOTTLE_VOLUME = 2.0 # both in liters

    cansPerPack = 6
    packVolume = cansPerPack * CAN_VOLUME
    print("Six Pack Volume is", packVolume, "Liters")
    print("Two Liter bottle", BOTTLE_VOLUME, "liters")

demo1_variables()

# = means set to or get
lives = 3 
print("Lives at start", lives)
lives = lives + 2   #adding 2 lives to your total
print("After", lives)