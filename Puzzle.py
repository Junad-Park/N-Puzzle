import random, math

class NPuzzle:
  def __init__(self, N):
    self.N = N
    self.n = int(math.sqrt(N))
    self.goal = [ _ for _ in range(1, N)] + [0]
    self.puzzle = []
  
  def shuffle_puzzle(self):
    temp_puzzle = self.goal.copy()
    random.shuffle(temp_puzzle)
    return temp_puzzle

  def create_solvable_puzzle(self):
    while True:
      temp_puzzle = self.shuffle_puzzle()
      row_from_bottom = self.n - (temp_puzzle.index(0)//self.n)
      if self.is_solved(row_from_bottom, temp_puzzle):
        break
    self.puzzle = temp_puzzle
  
  def is_solved(self, row, puzzle):
    if (self.n%2 == 1):
      return self.getInversionCnt(puzzle) % 2 == 0
    else:
      if (row % 2 == 0):
        return self.getInversionCnt(puzzle) % 2 == 1
      else:
        return self.getInversionCnt(puzzle) % 2 == 0
  
  def getInversionCnt(self, puzzle):
    inversion_cnt = 0
    for i in range(len(puzzle)):
      for j in range(i, len(puzzle)):
        if (puzzle[i]!=0 and puzzle[j] !=0 and puzzle[i] > puzzle[j]):
          inversion_cnt += 1
    return inversion_cnt

  def move_up(self):
    idx = self.puzzle.index(0)
    if idx < self.n:
      print(f"{idx} < {self.n}")
      return False
    change_elemnt = self.puzzle[idx]
    self.puzzle[idx] = self.puzzle[idx-self.n]
    self.puzzle[idx-self.n] = change_elemnt
    return True

  def move_down(self):
    idx = self.puzzle.index(0)
    if idx >= (self.N-self.n):
      print(f"{idx} >= {self.N-self.n}")
      return False
    
    change_elemnt = self.puzzle[idx]
    self.puzzle[idx] = self.puzzle[idx+self.n]
    self.puzzle[idx+self.n] = change_elemnt
    return True

  def move_right(self):
    idx = self.puzzle.index(0)
    if idx%self.n == (self.n-1):
      print(f"{idx%self.n} == {self.n-1}")
      return False
      
    change_elemnt = self.puzzle[idx]
    self.puzzle[idx] = self.puzzle[idx+1]
    self.puzzle[idx+1] = change_elemnt
    return True

  def move_left(self):
    idx = self.puzzle.index(0)
    if idx%self.n == 0:
      print(f"{idx%self.n} == {0}")
      return False
      
    change_elemnt = self.puzzle[idx]
    self.puzzle[idx] = self.puzzle[idx-1]
    self.puzzle[idx-1] = change_elemnt
    return True

  def display(self):
    for i in range(self.n):
      for j in range(self.n):
        print(f"{self.puzzle[i*self.n+j]:<3}", end="")
      print()
    print()
