import random, math

class NPuzzle:
    

    def __init__(self, N):
        self.__N = N
        self.__n = int(math.sqrt(N))
        self.__goal = [ _ for _ in range(1, N)] + [0]
        self.__puzzle = self.__goal

    def getRandomPuzzle(self) -> list[int]:
        """ Get random puzzle based on self.goal
        
        Returns:
            list[int]: The shuffle of the self.goal.copy
        """
        temp_puzzle = self.__goal.copy()
        random.shuffle(temp_puzzle)
        return temp_puzzle

    def createSolvablePuzzle(self) -> list[int]:
        """ Create solvable puzzle 
        
        Returns:
            list[int]: solvable puzzle
        """
        while True:
            random_puzzle = self.getRandomPuzzle()
            row_from_bottom = self.__n - (random_puzzle.index(0)//self.__n)
            if self.isSolved(row_from_bottom, random_puzzle):
                break
        self.__puzzle = random_puzzle
        #random_puzzle
        #[1,2,3,4,5,6,7,0,8]
        #[1,2,3,4,5,6,7,8,9,10,11,12,13,14,0,15]
        return self.__puzzle
  
    def isSolved(self, row, random_puzzle) -> bool:
        """ Decide it can be solved
        
        Args:
            row (int): row of puzzle from bottom
            puzzle (list[int]): random puzzle

        Returns:
            list[int]: solvable puzzle
        """
        if (self.__n%2 == 1):
            return self.getInversionCnt(random_puzzle) % 2 == 0
        else:
            if (row%2 == 0):
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
                if (random_puzzle[i]!=0 and 
                    random_puzzle[j] != 0 and 
                    random_puzzle[i] > random_puzzle[j]
                    ):
                    inversion_cnt += 1
        return inversion_cnt

    def moveUp(self) -> bool:
        """ Swap zero, above element in puzzle 

        Returns:
            bool: Can move up
        """
        zero_idx = self.__puzzle.index(0)
        if zero_idx < self.__n:
            print(f"{zero_idx} < {self.__n}")
            return False
        change_elemnt = self.__puzzle[zero_idx]
        self.__puzzle[zero_idx] = self.__puzzle[zero_idx-self.__n]
        self.__puzzle[zero_idx-self.__n] = change_elemnt
        return True

    def moveDown(self) -> bool:
        """ Swap zero, bottom element in puzzle 

        Returns:
            bool: Can move down
        """
        zero_idx = self.__puzzle.index(0)
        if zero_idx >= (self.__N-self.__n):
            print(f"{zero_idx} >= {self.__N-self._n}")
            return False
    
        change_elemnt = self.__puzzle[zero_idx]
        self.__puzzle[zero_idx] = self.__puzzle[zero_idx+self.__n]
        self.__puzzle[zero_idx+self.__n] = change_elemnt
        return True

    def moveRight(self) -> bool:
        """ Swap zero, right element in puzzle 

        Returns:
            bool: Can move right
        """
        zero_idx = self.__puzzle.index(0)
        if zero_idx%self.__n == (self.__n-1):
            print(f"{zero_idx%self.__n} == {self.__n-1}")
            return False
      
        change_elemnt = self.__puzzle[zero_idx]
        self.__puzzle[zero_idx] = self.__puzzle[zero_idx+1]
        self.__puzzle[zero_idx+1] = change_elemnt
        return True

    def moveLeft(self) -> bool:
        """ Swap zero, left element in puzzle 

        Returns:
            bool: Can move left
        """
        zero_idx = self.__puzzle.index(0)
        if zero_idx%self.__n == 0:
            print(f"{zero_idx%self.__n} == {0}")
            return False
      
        change_elemnt = self.__puzzle[zero_idx]
        self.__puzzle[zero_idx] = self.__puzzle[zero_idx-1]
        self.__puzzle[zero_idx-1] = change_elemnt
        return True

    def display(self) -> None:
        """ Output in 2D

        Returns:
            None
        """
        for i in range(self.__n):
            for j in range(self.__n):
                print(f"{self.__puzzle[i*self.__n+j]:<3}", end="")
            print()
        print()

    def getPuzzle(self) -> list[int]:
        """ Return self.__puzzle """
        return self.__puzzle

    def getGoal(self) -> list[int]:
        """ Return self.goal """
        return self.__goal
    
    def getN(self) -> int:
        return self.__N

    def getn(self) -> int:
        return self.__n

    def setN(self, N):
        self.__N = N

    def setn(self, n):
        self.__n = n
    
    def setGoal(self):
        self.__goal = [ _ for _ in range(1, self.__N)] + [0]
    
    def setPuzzle(self):
        self.__puzzle = self.__goal
    
    def updatePuzzle(self, N):
        n = int(math.sqrt(N))
        self.setN(N)
        self.setn(n)
        self.setGoal()
        self.setPuzzle()
