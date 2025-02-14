board = [[".",".","."],
         [".",".","."],
         [".",".","."]]
board_to_show = [["(1)","(2)","(3)"],
                 ["(4)","(5)","(6)"],
                 ["(7)","(8)","(9)"]]
board_codes = [[1, [0,0]],
               [2, [0,1]],
               [3, [0,2]],
               [4, [1,0]],
               [5, [1,1]],
               [6, [1,2]],
               [7, [2,0]],
               [8, [2,1]],
               [9, [2,2]]]

def ttt():
    def winner(b):
        def winner_row(b):
            if b == []:
                return [False]
            else:
                b00 = b[0][0]
                if b00 == ".":
                    return winner_row(b[1:])
                elif b00==b[0][1] and b00==b[0][2]:
                    return [True, b00]
                else:
                    return winner_row(b[1:])
        def winner_col(b, col):
            if col == 3:
                return [False]
            else:
                b0col = b[0][col]
                if b0col == ".":
                    return winner_col(b, col+1)
                elif b0col==b[1][col] and b0col==b[2][col]:
                    return [True, b0col]
                else:
                    return winner_col(b, col+1)
        def winner_diag(b):
            b11 = b[1][1]
            if b11 == ".":
                return [False]
            elif b[0][0]==b11 and b11==b[2][2] or b[0][2]==b11 and b11==b[2][0]:
                return [True, b11]
            else:
                return [False]
        
        row = winner_row(b) 
        col = winner_col(b, 0)
        diag = winner_diag(b)

        if row[0]:
            return row
        elif col[0]:
            return col
        else:
            return diag
    def code_to_move(code, lst):
        if lst == []:
            return -1
        elif lst[0][0] == code:
            return lst[0][1]
        else:
            return code_to_move(code, lst[1:])
    def print_board(board):
        if board == []:
            return
        else:
            printr = board[0]
            print(printr[0]+" "+printr[1]+" "+printr[2])
            return print_board(board[1:])
    def ttt_main(turn, counter):
        if counter == 9:
            print("it's a tie!")
            return
        win = winner(board)
        if win[0]:
            print_board(board_to_show)
            print(win[1] + " wins!!")
        else:
            print_board(board_to_show)
            code = input(turn + "'s Turn: ")
            if code == "reset":
                board.clear()
                board.append([".",".","."])
                board.append([".",".","."])
                board.append([".",".","."])

                board_to_show.clear()
                board_to_show.append(["(1)","(2)","(3)"])
                board_to_show.append(["(4)","(5)","(6)"])
                board_to_show.append(["(7)","(8)","(9)"])
                return ttt_main("X", 0)
            else:
                code = int(code)
                move = code_to_move(code, board_codes)
                if move == -1:
                    print("invalid spot")
                    return ttt_main(turn, counter)
                else:
                    spot = board[move[0]][move[1]]
                    if turn == "X":
                        other = "O"
                    else:
                        other = "X"

                    if move == -1 or spot == "X" or spot == "O":
                        print("invalid spot")
                        return ttt_main(turn, counter)
                    else:
                        board[move[0]][move[1]] = turn
                        board_to_show[move[0]][move[1]] = " " + turn + " "
                        return ttt_main(other, counter+1)
                
    return ttt_main("X", 0)

ttt()
