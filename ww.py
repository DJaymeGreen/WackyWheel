"""D Jayme Green

Implementation of a doubly, circularly Linked List in Python
"""

from myList import *
import random 

class Player():
    __slots__ = ("Money")

"""
    Makes a player object which contains the amount of money
    param   startMoney  int initial money player will start with
    return  player      Player newly created 
"""
def mkPlayer(startMoney):
    player = Player()
    player.Money = startMoney
    return player

"""
    Creates the players and sets there money
    param   startMoney  int initial money players will
                        start with 
    return  tuple       Tuple of created Players
"""
def setPlayers (startMoney):
    player1 = mkPlayer (startMoney)
    player2 = mkPlayer (startMoney)
    player3 = mkPlayer (startMoney)
    return (player1, player2, player3)

"""
    Reads the file and creates the list
    param   file    File that has wheel data
    return  List    List of modified data of wheel data
"""
def readFile(file):
    filename = open(file)
    aList = []
    for line in filename:
        line = line.lstrip('$')
        line = line.rstrip('\n')
        aList += line.split(",")
        aList = [int(i) for i in aList]
        #print(line)
    return aList

"""
    Makes a linkedList and sets the wheel using the values
    from the list from the file
    param   pylst   Modified file which contains wheel data
    return  myList  linkedList representing the wheel
"""
def setWheel (pylst):
    myList = mkList()
    for i in range (0, len(pylst)-1):
        add(myList,pylst[0])
        if myList.size >1:
            forward(myList)
        pylst.pop(0)
    myList = addLast(myList, pylst[0])
    return myList

"""
    Randomly chooses whether the wheel will spin clockwise
    or counterclockwise
    return      boolean     true Clockwise, false counterclockwise
"""
def isclockwise():
    randomNum = random.randint(0,1)
    if randomNum == 0:
        return True
    else:
        return False


"""
    Gets a random number between 2 and
    the linkedList size in order to find how
    many steps the wheel should spin
    param   myList  List containing the wheel
    return     int  randomNum for steps wheel win spin
"""
def getNumofMoves(myList):
    randomNum = random.randint(2,size(myList))
    return randomNum


"""
    Moves the wheel in either clockwise or counterclockwise for
    x many steps (calling getNumofMoves) and returns the item there
    param   myList  List containing the wheel
    param   player  Player doing the move
    return      void
"""
def move(myList, player):
    direction = isclockwise()
    numofMoves = getNumofMoves(myList)
    print("Clockwise:", direction, "numofMoves:", numofMoves)
    for i in range (0, numofMoves):
        if (direction == True):
            forward(myList)
        else:
            backward(myList)
        print(myList.cursor.data)
    amount = myList.cursor.data
    if direction == True:
        player.Money += amount
    else:
        player.Money -= amount
    remove(myList)

"""
    Prints the winner after the game has been played
    param   myList  List containing the wheel
    param   player1 1st player
    param   player2 2nd player
    param   player3 3rd player
    return    void
"""
def printWinner(myList, player1, player2, player3):
    if ((player1.Money <= 0 and player2.Money <= 0) and player3.Money > 0):
        print("Player3 wins!")
    elif((player2.Money <= 0 and player3.Money <= 0) and player1.Money > 0):
        print("Player1 wins!")
    elif((player1.Money <= 0 and player3.Money <= 0) and player2.Money > 0):
        print("Player2 wins!")
    elif(size(myList) >= 3):
        print("Ran out of spins, no true winners...")
    elif(player1.Money > player3.Money and player1.Money > player2.Money):
        print("Player1 wins!")
    elif(player2.Money > player3.Money and player2.Money > player1.Money):
        print("Player2 wins!")
    elif(player3.Money > player1.Money and player3.Money > player2.Money):
        print("Player3 wins!")

"""
    Main code that runs the game. Continues loop where each player goes and continues
    till the end of the game. States winner at the end 
"""
def playGame():
    file = input( "Enter filename (type d for default file): " )
    #file = "F:/Jayme/Documents/Academics/Y1S1/CSCI 141/WackyWheel/test.txt"
    #file = "C:/Users/Jayme/Documents/College Academics/Y1S1/CSCI/test.txt"
    aList = readFile(file)
    player1, player2, player3 = setPlayers(int(aList[0]))
    aList.pop(0)
    myList = setWheel(aList)
    #printList(myList)
    numofRounds = 1
    out = 0

    while (size(myList) >=3 and out <2 ):
        print("START Round:" , numofRounds, " Players are: Player1:", player1.Money,
              "Player2:", player2.Money, "Player3:", player3.Money)
        if (player1.Money > 0):
            print("Player1 spins")
            amount = move(myList, player1)
            print("Player1 account balance:", player1.Money)
            if player1.Money <= 0:
                print("Player1 has been eliminated!")
                out += 1
        if (player2.Money > 0):
            print("Player2 spins")
            amount = move(myList, player2)
            print("Player2 account balance:", player2.Money)
            if player2.Money <= 0:
                print("Player2 has been eliminated!")
                out += 1
        if (player3.Money > 0):
            print("Player3 spins")
            amount = move(myList, player3)
            print("Player3 account balance:", player3.Money)
            if player3.Money <= 0:
                print("Player3 has been eliminated!")
                out +=1
        numofRounds += 1
        
    print( "Ending Results: Player1:", player1.Money,
              "Player2:", player2.Money, "Player3:", player3.Money)

    printWinner(myList, Player1, Player2, Player3)
    




playGame()
