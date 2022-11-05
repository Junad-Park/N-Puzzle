# This Python file uses the following encoding: utf-8
import sys

from Puzzle import NPuzzle

from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import resource_rc

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("form.ui", self)
        self.setWindowTitle("N-Puzzle")
        self.setFixedSize(880, 760)

        self.nPzl= NPuzzle(9)
        self.goal = self.nPzl.getGoal()
        self.puzzle = self.nPzl.getPuzzle()

        self.Btns = [
            self.puzzle_1, self.puzzle_2, self.puzzle_3, 
            self.puzzle_4, self.puzzle_5, self.puzzle_6, 
            self.puzzle_7, self.puzzle_8, self.puzzle_9
            ]
        self.inital_styles = [item.styleSheet() for item in self.Btns]

        self.lastPeace = self.puzzle_9.styleSheet()

        self.running = False

    def movePuzzle(self) -> None:
        """ Move the a piece of a puzzle you received with the sender
        
        Returns:
            None
        """
        target = self.sender()
        target_num = int(target.objectName()[-1])

        if self.running:
            if self.isClickMoved(target_num):
                self.swapStyleSheet(target_num)
                self.swapZero(target_num)

            self.updatePuzzle()
        
        if self.clear():
            self.puzzle_9.setStyleSheet(self.lastPeace)
            self.running = False

    
    def isClickMoved(self, target_num) -> bool:
        """ Move the tile you received with the sender
        
        Returns:
            bool: The result of logical operation
        """
        
        zero_idx = self.puzzle.index(0)
        target_idx = self.puzzle.index(self.puzzle[target_num-1])
        n = self.nPzl.n

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
                self.nPzl.moveLeft()
            else:
                self.nPzl.moveRight()

        elif distance == 3:
            if zero_idx > target_idx:
                self.nPzl.moveUp()
            else:
                self.nPzl.moveDown()

    def updatePuzzle(self) -> None:
        """ Receive puzzle from self.nPzl and put it self.puzzle  
        
        Returns:
            None
        """
        self.puzzle = self.nPzl.getPuzzle()

    def shuffle(self) -> None:
        """ Shuffle the puzzle according to self.puzzle
        
        Returns:
            None
        """
        self.running = True
        self.puzzle = self.nPzl.createSolvablePuzzle()
        
        for i in range(len(self.Btns)):
            self.Btns[i].setStyleSheet(
                self.inital_styles[self.goal.index(self.puzzle[i])]
                )

        self.Btns[self.puzzle.index(0)].setStyleSheet("")
        
    

    def clear(self) -> bool:
        """ Returns whether the game is cleared or not 
        
        Returns:
            bool: The result of logical operation
        """
    
        return self.running == True and self.goal == self.puzzle



if __name__ == "__main__":
  app = QApplication(sys.argv)
  widget = MainWindow()
  widget.show()
  help(widget.nPzl)
  sys.exit(app.exec())
