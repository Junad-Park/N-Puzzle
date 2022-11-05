import random, math

class NPuzzle:
    
    def __init__(self, N):

        self.N = N
        self.n = int(math.sqrt(N))
        self.goal = [ _ for _ in range(1, N)] + [0]
        self.puzzle = self.goal
    
    def getRandomPuzzle(self) -> list[int]:
        """ Get random puzzle based on self.goal
        
        Returns:
            list[int]: The shuffle of the self.goal.copy
        """
        temp_puzzle = self.goal.copy()
        random.shuffle(temp_puzzle)
        return temp_puzzle

    def createSolvablePuzzle(self) -> list[int]:
        """ Create solvable puzzle 
        
        Returns:
            list[int]: solvable puzzle
        """
        while True:
            random_puzzle = self.getRandomPuzzle()
            row_from_bottom = self.n - (random_puzzle.index(0)//self.n)
            if self.isSolved(row_from_bottom, random_puzzle):
                break
        self.puzzle = random_puzzle
        #temp_puzzle
        #[1,2,3,4,5,6,7,0,8]
        return self.puzzle
  
    def isSolved(self, row, random_puzzle) -> bool:
        """ Decide it can be solved
        
        Args:
            row (int): row of puzzle from bottom
            puzzle (list[int]): random puzzle

        Returns:
            list[int]: solvable puzzle
        """
        if (self.n%2 == 1):
            return self.getInversionCnt(random_puzzle) % 2 == 0
        else:
            if (row % 2 == 0):
                return self.getInversionCnt(random_puzzle) % 2 == 1
            else:
                return self.getInversionCnt(random_puzzle) % 2 == 0
  
    def getInversionCnt(self, random_puzzle) -> int:
        """ Get inversion count

        Args:
            random_puzzle (list[int]): random puzzle

        Returns:
            int: inversion count
        """
        inversion_cnt = 0
        for i in range(len(random_puzzle)):
            for j in range(i, len(random_puzzle)):
                if (random_puzzle[i]!=0 and random_puzzle[j] !=0 and random_puzzle[i] > random_puzzle[j]):
                    inversion_cnt += 1
        return inversion_cnt

    def moveUp(self) -> bool:
        """ Swap zero, above element in puzzle 

        Returns:
            bool: Can move up
        """
        zero_idx = self.puzzle.index(0)
        if zero_idx < self.n:
            print(f"{zero_idx} < {self.n}")
            return False
        change_elemnt = self.puzzle[zero_idx]
        self.puzzle[zero_idx] = self.puzzle[zero_idx-self.n]
        self.puzzle[zero_idx-self.n] = change_elemnt
        return True

    def moveDown(self) -> bool:
        """ Swap zero, bottom element in puzzle 

        Returns:
            bool: Can move down
        """
        zero_idx = self.puzzle.index(0)
        if zero_idx >= (self.N-self.n):
            print(f"{zero_idx} >= {self.N-self.n}")
            return False
    
        change_elemnt = self.puzzle[zero_idx]
        self.puzzle[zero_idx] = self.puzzle[zero_idx+self.n]
        self.puzzle[zero_idx+self.n] = change_elemnt
        return True

    def moveRight(self) -> bool:
        """ Swap zero, right element in puzzle 

        Returns:
            bool: Can move right
        """
        zero_idx = self.puzzle.index(0)
        if zero_idx%self.n == (self.n-1):
            print(f"{zero_idx%self.n} == {self.n-1}")
            return False
      
        change_elemnt = self.puzzle[zero_idx]
        self.puzzle[zero_idx] = self.puzzle[zero_idx+1]
        self.puzzle[zero_idx+1] = change_elemnt
        return True

    def moveLeft(self) -> bool:
        """ Swap zero, left element in puzzle 

        Returns:
            bool: Can move left
        """
        zero_idx = self.puzzle.index(0)
        if zero_idx%self.n == 0:
            print(f"{zero_idx%self.n} == {0}")
            return False
      
        change_elemnt = self.puzzle[zero_idx]
        self.puzzle[zero_idx] = self.puzzle[zero_idx-1]
        self.puzzle[zero_idx-1] = change_elemnt
        return True

    def display(self) -> None:
        """ Output in 2D

        Returns:
            None
        """
        for i in range(self.n):
            for j in range(self.n):
                print(f"{self.puzzle[i*self.n+j]:<3}", end="")
            print()
        print()

    def getPuzzle(self) -> list[int]:
        """ Return self.puzzle """
        return self.puzzle

    def getGoal(self) -> list[int]:
        """ Return self.goal """
        return self.goal

