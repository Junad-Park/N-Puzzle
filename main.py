# This Python file uses the following encoding: utf-8
import sys
from queue import PriorityQueue

from package.Puzzle import NPuzzle

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic, QtWidgets
import package.ui.resource_rc as resource_rc

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


class MainWindow(QtWidgets.QMainWindow):


    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("designer/form.ui", self)
        self.setWindowTitle("N-Puzzle")
        self.setFixedSize(880, 760)

        self.stackedWidget:QStackedWidget
        
        self.nPzl= NPuzzle(9)
        self.goal = self.nPzl.getGoal()
        self.puzzle = self.nPzl.getPuzzle()
        self.mode = self.nPzl.getN()
        self.running = False

        self.Btns = [self.__dict__[f"puzzle_{i+1}"] 
                    for i in range(self.nPzl.getN())] 

        self._8_initial_styles = [self.__dict__[f"puzzle_{i+1}"].styleSheet() 
                    for i in range(9)]

        self._15_initial_styles = [self.__dict__[f"puzzle_{i+1}"].styleSheet() 
                    for i in range(9, 25)]

        
        self.styles = self._8_initial_styles
        self.lastPeace = self.Btns[-1].styleSheet()

    def movePuzzle(self) -> None:
        """ Move the a piece of a puzzle you received with the sender
        Returns:
            None
        """
        target = self.sender()
        target_num = int(target.objectName().split('_')[1])
        
        if self.mode == 16:
            target_num -=9

        if self.running:
            if self.isClickMoved(target_num):
                self.swapStyleSheet(target_num)
                self.swapZero(target_num)
                self.updatePuzzle()
        
        if self.clear():
            self.Btns[-1].setStyleSheet(self.lastPeace)
            self.running = False
 
    def isClickMoved(self, target_num) -> bool:
        """ Move the tile you received with the sender
        
        Returns:
            bool: The result of logical operation
        """
        
        zero_idx = self.puzzle.index(0)
        target_idx = self.puzzle.index(self.puzzle[target_num-1])
        n = self.nPzl.getn()

        return (abs(zero_idx - target_idx) == n or 
        target_idx//n == zero_idx//n and abs(zero_idx - target_idx) == 1)
      
    def swapStyleSheet(self, target_num) -> None:
        """ Move the tile you received with the sender
        
        Args:
            target_num (int): Number of the puzzle received by sender.

        Returns:
            None
        """
        zero_idx = self.puzzle.index(0)
        target_idx = self.puzzle.index(self.puzzle[target_num-1])

        temp = self.Btns[target_idx].styleSheet()
        self.Btns[target_idx].setStyleSheet("")
        self.Btns[zero_idx].setStyleSheet(temp)

    def swapZero(self, target_num) -> None:
        """ Move the tile you received with the sender
        
        Args:
            target_num (int): Number of the puzzle received by sender.
        
        Returns:
            None
        """
        zero_idx = self.puzzle.index(0)
        target_idx = self.puzzle.index(self.puzzle[target_num-1])
        distance = abs(zero_idx - target_idx)

        if distance == 1:
            if zero_idx > target_idx:
                self.puzzle = self.nPzl.moveLeft()
            else:
                self.puzzle = self.nPzl.moveRight()

        elif distance == self.nPzl.getn():
            if zero_idx > target_idx:
                self.puzzle = self.nPzl.moveUp()
            else:
                self.puzzle = self.nPzl.moveDown()

    def updatePuzzle(self, other=None) -> None:
        """ Receive goal, puzzle, mode from self.nPzl and put it 
        
        Returns:
            None
        """
        if other==None:
            self.goal = self.nPzl.getGoal()
            self.mode = self.nPzl.getN()
            self.puzzle = self.nPzl.getPuzzle()
        else:
            self.goal = other.getGoal()
            self.mode = other.getN()
            self.puzzle = other.getPuzzle()

    def shuffle(self) -> None:
        """ Shuffle the puzzle according to self.puzzle
        
        Returns:
            None
        """
        self.running = True
        self.puzzle = self.nPzl.createSolvablePuzzle()

        for i in range(len(self.Btns)):
            self.Btns[i].setStyleSheet(
                self.styles[self.goal.index(self.puzzle[i])]
                )

        self.Btns[self.puzzle.index(0)].setStyleSheet("")
        
            
    def clear(self) -> bool:
        """ Returns whether the game is cleared or not 
        
        Returns:
            bool: The result of logical operation
        """
    
        return self.running == True and self.goal == self.puzzle

    def whatMode(self, N):
        """ Select mode according to the value of 'N'

        Args:
            None
        """
        if N == 9:
            self.stackedWidget.setCurrentWidget(self.page)
            self.styles = self._8_initial_styles
            for i in range(self.mode):
                self.Btns.append(self.__dict__[f"puzzle_{i+1}"])

        elif N == 16:
            self.stackedWidget.setCurrentWidget(self.page_2)
            self.styles = self._15_initial_styles
            for i in range(self.mode):
                self.Btns.append(self.__dict__[f"puzzle_{i+1+9}"])

    def changeMode(self):
        """ Change mode according to the value of 'N'

        Args:
            None
        """
        target = self.sender()
        N = int(target.objectName().split('_')[1])+1
        
        self.nPzl.updatePuzzle(N)
        self.updatePuzzle()
        self.Btns = []

        self.whatMode(N)
        
        self.lastPeace = self.Btns[-1].styleSheet()

        for i in range(len(self.Btns)):
            self.Btns[i].setStyleSheet(self.styles[i])
        self.running = False

    def solve(self, initial_board):
        """
            returns a list of moves from 'initial_board' to goal state
                calculated using A* algorithm
        """
        queue = PriorityQueue()
        queue.put(initial_board.to_pq_entry(0))

        i = 1

        while not queue.empty():
            board = queue.get()[2]
            if not board.is_goal():
                for neighbour in board.neighbours():
                    if neighbour != board.previous:
                        queue.put(neighbour.to_pq_entry(i))
                        i += 1
                # board.display()
                
            else:
                return board.get_previous_states()

        return None
    
    def ai(self):        
        moves = self.solve(self.nPzl)
        for i in range(len(moves)):
            self.updatePuzzle(moves[i])
            self.ai_swapStyleSheet()
            # moves[i].display()
            # print(moves[i].get_f())
            self.reset()

        if self.clear():
            self.Btns[-1].setStyleSheet(self.lastPeace)
            self.running = False
            
            
    def ai_swapStyleSheet(self):
        for i in range(len(self.styles)):
            self.Btns[i].setStyleSheet(
                self.styles[self.goal.index(self.puzzle[i])]
            )
        self.Btns[self.puzzle.index(0)].setStyleSheet("")
        
    def reset(self):
        loop = QEventLoop()
        QTimer.singleShot(100, loop.quit)
        loop.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()


    mainWindow.show()

    app.exec()
