import random

def login():
    loggedin = False
    while loggedin == False:
        with open("passwords.txt", mode="r",encoding="utf-8") as my_file:
            passwords = my_file.read().splitlines()
        print("Enter Username")
        un = input()
        print("Enter Password")
        pw = input()
        for counter in range(len(passwords)):
            userAndPass = passwords[counter].split(",")
            if un == userAndPass[0] and pw == userAndPass[1]:
                loggedin = True
                return userAndPass[0]
        if loggedin == False:
            print("Details not found")
        else:
            print("Logged in")

def createcards():
    deck = []
    for colour in ["Red","Black","Yellow"]:
        for value in ["1","2","3","4","5","6","7","8","9","10"]:
            deck.append(colour+","+value)
    random.shuffle(deck)
    return(deck)

def playgame(deck, user1, user2):
    player1deck = []
    player2deck = []
    while len(deck) > 0:
        player1 = deck.pop()
        player2 = deck.pop()
        player1deck,player2deck = checkwin(player1,player2,player1deck,player2deck)
        play = input()
    print(len(player1deck),len(player2deck))
    print(player1deck,player2deck)


def checkwin(player1,player2,player1deck,player2deck):
    player1 = player1.split(",")
    player2 = player2.split(",")
    print(player1)
    print(player2)
    if player1[0] == player2[0]:
        print("Same colour card!")
        if int(player1[1]) > int(player2[1]):
            print("Player 1 wins hand on score")
            player1deck.append(player1)
            player1deck.append(player2)
        else:
            print("Player 2 wins hand on score")
            player2deck.append(player1)
            player2deck.append(player2)  
    else:
        if player1[0] == "Red" and player2[0] == "Black":
            print("Player 1 wins hand")
            player1deck.append(player1)
            player1deck.append(player2)
        elif player1[0] == "Red" and player2[0] == "Yellow":
            print("Player 2 wins hand")
            player2deck.append(player1)
            player2deck.append(player2)
        elif player1[0] == "Yellow" and player2[0] == "Red":
            print("Player 1 wins hand")
            player1deck.append(player1)
            player1deck.append(player2)
        elif player1[0] == "Yellow" and player2[0] == "Black":
            print("Player 2 wins hand")
            player2deck.append(player1)
            player2deck.append(player2)
        elif player1[0] == "Black" and player2[0] == "Red":
            print("Player 2 wins hand")
            player2deck.append(player1)
            player2deck.append(player2)
        elif player1[0] == "Black" and player2[0] == "Yellow":
            print("Player 1 wins hand")
            player1deck.append(player1)
            player1deck.append(player2)
    return player1deck,player2deck

def main():
    print("First player now log in:")
    user1 = login()
    print("You are logged in", user1)
    print("Second player now log in:")
    user2 = login()
    print("You are logged in", user2)
    print("Player 1:", user1, " and Player 2:", user2, "are now logged in and ready to play")
    deck = createcards()
    playgame(deck, user1, user2)

main()
