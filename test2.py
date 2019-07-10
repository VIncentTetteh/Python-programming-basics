
def man():
    for i in range(0, 4):
        for j in range(0, i +1):
            #print("j is " + str(j) + " i is " + str(i) )
            
            print("*", end=" ")
        print()
            
    for i in range(0, 4):
        for j in range(3,i,-1):
            print("*", end=" ")
        print()
        
        
man()
            
