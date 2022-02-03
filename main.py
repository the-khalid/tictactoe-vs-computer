print("Welcome a-board\nTIC TAC TOE vs Computer\nComputer-'O'\tPlayer-'X'")
print("Computer will make the first move\nPress Y/y to start :)")
feed = input()
import os
import random

def play():
    list = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    def board():
        os.system('clear')
        print(list[0], "|", list[1], "|", list[2])
        print(list[3], "|", list[4], "|", list[5])
        print(list[6], "|", list[7], "|", list[8])

    board()
    playerFlag = True
    # O is computer

    def posCheck(pos):
        if pos > 9 or pos < 1:
            return False
        if list[pos - 1] != "-":
            return False
        return True

    def numSpaces(list):
      count = 0;
      for i in range(9):
        if list[i]=='-':
          count=+1
      return count

    def minimax(list, turnFlag, alpha, beta):
      if gameCheck() == 'O':
        index = numSpaces(list)*1
        return index
      elif gameCheck() == 'X':
        index = -1*numSpaces(list)
        return index
      elif list.count('-') == 0:
        index = 0
        return index
      if turnFlag:
        maxScore = -9
        for i in range(9):
          if list[i]=='-':
            list[i]='O'
            score = minimax(list, False, alpha, beta)
            list[i]='-'
            maxScore = max(maxScore, score)
            alpha = max(score, alpha)
            if beta <= alpha:
              break;
        return maxScore
      else:
        minScore = 9
        for i in range(9):
          if list[i]=='-':
            list[i]='X'
            score = minimax(list, True, alpha, beta)
            list[i]='-'
            minScore = min(minScore, score)
            beta = min(beta, score)
            if beta <= alpha:
              break;
        return minScore

    def compMove():
      if list.count("-") == 9:
        return random.randint(0,8);
      bestScore = -9
      bestMove = 0
      for i in range(9):
        if list[i]=='-':
          list[i]='O'
          score = minimax(list, False, -9, 9)
          list[i]='-'
          if score > bestScore:
            bestScore = score
            bestMove = i
      return bestMove

    def gameCheck():
        if list[0] == list[1] == list[2] and list[0] != '-':
            return list[0]
        elif list[3] == list[4] == list[5] and list[3] != '-':
            return list[3]
        elif list[6] == list[7] == list[8] and list[6] != '-':
            return list[6]
        elif list[0] == list[3] == list[6] and list[0] != '-':
            return list[0]
        elif list[1] == list[4] == list[7] and list[1] != '-':
            return list[1]
        elif list[2] == list[5] == list[8] and list[2] != '-':
            return list[2]
        elif list[0] == list[4] == list[8] and list[0] != '-':
            return list[0]
        elif list[2] == list[4] == list[6] and list[2] != '-':
            return list[2]
        else:
            return '-'

    while True:
        if playerFlag:
            pos = compMove()
            list[pos] = "O"
        else:
            print("its your chance\ntype in the position: ")
            pos = int(input())
            while not posCheck(pos):
                print("please enter valid position: ")
                pos = int(input())
            list[pos - 1] = "X"
        if gameCheck() == 'O':
            board()
            print("Computer won!!\nlook at your face lol")
            print("=====================")
            break
        elif gameCheck() == 'X':
            board()
            print("Hurrayy\nYou just beat the computer!")
            print("=====================")
            break;
        if list.count("-") == 0:
            board()
            print("its a tie!")
            break
        playerFlag = not playerFlag
        board()
      
while feed == 'Y' or feed == 'y':
    play()
    print("Wanna Play again?(Y/N)")
    feed = input()
