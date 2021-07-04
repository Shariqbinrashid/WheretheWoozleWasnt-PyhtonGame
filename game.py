# Woozle
# Programming Concepts Coursework
# June 2021
def display( A, B ):
    for C in range(15):
        for D in range(15):
            E = (C * 15) + D
            print ( chr( A[E] ), end = " ")
        print ( " " )
    B = B + 1
    return B

def place(A):
    import random
    B = random.random()
    B = int( B * 75 )
    B = B + 75 * ( A == "S" )
    B = B + 150 * ( A == "P" )
    return B
def init( A ):
    for B in range(15):
        A[B] = 35
        A[B + 210] = 35
        A[B * 15] = 35
        A[(B * 15) + 14] = 35
    return A
def row( A ):
    for B in range(15):
        for C in range(15):
            D = (B * 15) + C
            if ( D == A ):
                E = B
    return( E )

def passed( A, B ):
    C = row( B )
    D = C * 15
    E = 0
    for F in range(15):
        if ( (D + F) == A):
            E = 1
    return E

def check( A, B, C, D, E ):
    F = passed( A, B )
    if ( (F == 1) and ( C > D + 5) ):
        D = C
        E = E + 1
    if ( E > 1 ):
        print ("Congratulations. You have gone")
        print ("round the spinney.")
    else:
        print("Keep going. You have not gone")
        print("round the spinney yet.")
    return D, E

def move( A, B):
    print ("Select key and press return to move")
    print ("U = Up, D = Down, L = Left, R = Right")
    C = input ("Enter key ")
    if (C == "U"):
        D = A - 15
    if (C == "D"):
        D = A + 15
    if (C == "L"):
        D = A - 1
    if (C == "R"):
        D = A + 1
    if (B[D] == 46):
        A = D
    return A

def main():
    import os
    clear = lambda: os.system('cls')
    # Following 5 lines essential
    SNOW = [46] * 225
    SNOW = init(SNOW)
    TICK = 0
    EVENT = 0
    CIRCLED = 0
    WINcheck=0

  
    # To store initial positon of both players
    p1=0 
    
    p2=0
    
    #Player 1 initial placement
    while(1):
        player_1 = place( "W" ) 

        if SNOW[ player_1 ] == 46:
            break
    print ("Winnie (Player 1) starts at location", end = " ")
    print ( player_1)
    p1=player_1
    SNOW[ player_1 ] = 87
    

    
    while(1):
        player_2 = place( "P" )
        if SNOW[ player_2 ] == 46:
            break

    #Player 2 initial placement        
    print ("Piglet (Player 2) starts at location", end = " ")
    print ( player_2)
    p2=player_2
    SNOW[ player_2 ] = 80


    #Spinny placement
   
    spinny = 112
    SNOW[ spinny ] = 83
    TICK = display( SNOW, TICK )
    
    # Game logic
    while(1):
        print(" ") 
        dummy = input("Player 1 turn: Press enter to move")


        player_1 = move( player_1, SNOW )
        SNOW[ player_1 ] = 87

        clear()
        TICK = display( SNOW, TICK )
        EVENT, CIRCLED = check( player_1, spinny, TICK, EVENT, CIRCLED )

        #if player 1 has gone thorugh spinny then check for win condition
        if CIRCLED>0:
            if player_1+1==p1 or player_1-1==p1 or player_1+15==p1 or player_1-15==p1:
                WINcheck=1
                break

        print(" ")    
        dummy = input("Player 2 turn: Press enter to move")
        player_2 = move( player_2, SNOW )
        SNOW[ player_2 ] = 80

        clear()
        TICK = display( SNOW, TICK )
        EVENT, CIRCLED = check( player_2, spinny, TICK, EVENT, CIRCLED )
        #if player 2 has gone thorugh spinny then check for win condition
        if CIRCLED>0:
            if player_2-1==p2 or player_2+1==p2 or player_2-15==p2 or player_2+15==p2:
                WINcheck=2
                break

                #Result dipsplay
    if WINcheck==1:
        print("Congratulation! Player 1 wins")    

    if WINcheck==2:
        print("Congratulation! Player 2 wins")  
        
main()