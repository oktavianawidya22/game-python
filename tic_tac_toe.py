# Tic Tac Toe Game
def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(space != " " for space in board)

def main():
    board = [" " for _ in range(9)]
    current_player = "X"
    
    while True:
        print_board(board)
        try:
            move = int(input(f"Player {current_player}, pilih posisi (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Posisi harus antara 1-9. Coba lagi.")
                continue
            if board[move] != " ":
                print("Posisi sudah diisi. Coba lagi.")
                continue
            board[move] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Selamat! Player {current_player} menang!")
                break
            if is_draw(board):
                print_board(board)
                print("Seri! Tidak ada pemenang.")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Input tidak valid. Masukkan angka 1-9.")

if __name__ == "__main__":
    main()
