class Solution:

    moves =[[0,0],[2,0],[1,1],[2,1],[2,2]]

    def tictactoe(moves):
        
        grid = [[' ' for i in range(3)] for j in range(3)]

        if len(moves) < 5:
            return 'Pending'
        if len(moves) == 9:
            return 'Draw'
        
        for i, move in enumerate(moves):
            if i % 2 == 0:
                grid[move[0]][move[1]] = 'X'
            else:
                grid[move[0]][move[1]] = 'O'
        print(grid)

        

    print(tictactoe(moves))


    