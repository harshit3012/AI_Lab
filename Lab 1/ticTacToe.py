import random
import colorama
from colorama import Fore, Style

board = [' ' for _ in range(10)]
user_char = ''
comp_char = ''


def printBoard(board):
    global user_char, comp_char
    print("\033c", end="")
    print(Fore.GREEN + 'Tic Tac Toe! \n')
    print(Fore.WHITE + f'Your player : {user_char}')
    print(f'Computer player : {comp_char}', end="\n\n")
    print(Fore.BLUE + ' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' +
          board[9] + Style.RESET_ALL, end='\n\n')


def spaceIsFree(pos):
    return board[pos] == ' '


def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def insertLetter(letter, pos):
    board[pos] = letter


def selectRandom(li):
    r = random.randrange(0, len(li))
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False

    return True


def playerMove():
    run = True
    while run:
        move = input(f'\nSelect a position to place an {user_char}: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter(user_char, move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(
        board) if letter == ' ' and x != 0]
    move = 0

    for let in [comp_char, user_char]:
        for i in possibleMoves:
            boardCopy = board.copy()
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    if 5 in possibleMoves:
        move = 5
        return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move


def playerChoose():
    global user_char, comp_char
    print('\nTic Tac Toe! \n')
    user_input = input('Enter your player (O / X): ')
    while(user_input not in ['o', 'O', '0', 'x', 'X']):
        print("Sorry. That's invalid")
        user_input = input('Enter your player (O / X): ')
    if user_input in ['o', 'O', '0']:
        user_char = 'O'
        comp_char = 'X'
    else:
        user_char = 'X'
        comp_char = 'O'


def main():
    global board, user_char, comp_char
    playerChoose()

    play = True
    while play:
        while not(isBoardFull(board)):
            if not(isWinner(board, comp_char)):
                printBoard(board)
                playerMove()
            else:
                print('Computer won this time.. Hehe!')
                break
            if not(isWinner(board, user_char)):
                move = compMove()
                if move == 0:
                    print('Tie Game!')
                else:
                    insertLetter(comp_char, move)
                    print(
                        f'Computer placed an {comp_char} in position', move, ':')
                    printBoard(board)
            else:
                print('You won this time! Good Job!')
                break

        if input('Do you want to play again? (Y/N) ').lower() in ['y', 'yes']:
            board = [' ' for _ in range(10)]
            print('-----------------------------------')

        else:
            play = False


if __name__ == "__main__":
    main()
