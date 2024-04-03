/*
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, 
they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),
 where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
*/

#define EMPTY '.'
#define SHIP 'X'

void removeBattleship(char** board, int boardSize, int* boardColSize, int y, int x){
    bool inBounds = y >= 0 && y < boardSize && x >= 0 && x < boardColSize[y];
    if(!inBounds){
        return;
    }
    if(board[y][x] != SHIP){
        return;
    }
    board[y][x] = EMPTY;
    removeBattleship(board, boardSize, boardColSize, y+1, x);
    removeBattleship(board, boardSize, boardColSize, y-1, x);
    removeBattleship(board, boardSize, boardColSize, y, x+1);
    removeBattleship(board, boardSize, boardColSize, y, x-1);
}

int countBattleships(char** board, int boardSize, int* boardColSize) {
    int count = 0;
    for(int y = 0; y < boardSize; y++){
        for(int x = 0; x < boardColSize[y]; x++){
            if(board[y][x] == SHIP){
                removeBattleship(board, boardSize, boardColSize, y, x);
                count++;
            }
        }
    }
    return count;
}