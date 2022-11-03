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

    self.NP = NPuzzle(9)
    self.goal = self.NP.getGoal()
    self.puzzle = self.goal
    self.lastPeace = self.puzzle_9.styleSheet()
    self.puzzle_9.setStyleSheet("")

    self.Btns = [self.puzzle_1, self.puzzle_2, self.puzzle_3, self.puzzle_4, self.puzzle_5, self.puzzle_6, self.puzzle_7, self.puzzle_8, self.puzzle_9]
    
    self.inital_styles = []

    self.initial = True

  def movePuzzle(self):
    
    temp = self.sender()
    target_num = int(temp.objectName()[-1])

    if self.is_click_moved(target_num):
      self.swapStyleSheet(target_num)
      self.swapZero(target_num)

    self.puzzle = self.NP.getPuzzle()
    
    if self.clear():
      self.puzzle_9.setStyleSheet(self.lastPeace)

  
  def is_click_moved(self, target_num):
    zero_idx = self.puzzle.index(0)
    target_idx = self.puzzle.index(self.puzzle[target_num-1])
    n = self.NP.n

    return ((abs(zero_idx - target_idx) == n) or 
    ((target_idx//n == zero_idx//n) and abs(zero_idx - target_idx) == 1 ))
      

  def swapStyleSheet(self, target_num):
    zero_idx = self.puzzle.index(0)
    target_idx = self.puzzle.index(self.puzzle[target_num-1])

    temp = self.Btns[target_idx].styleSheet()
    self.Btns[target_idx].setStyleSheet("")
    self.Btns[zero_idx].setStyleSheet(temp)

  def swapZero(self, target_num):
    zero_idx = self.puzzle.index(0)
    target_idx = self.puzzle.index(self.puzzle[target_num-1])
    distance = abs(zero_idx - target_idx)

    if distance == 1:
      if zero_idx > target_idx:
        self.NP.move_left()
      else:
        self.NP.move_right()
    elif distance == 3:
      if zero_idx > target_idx:
        self.NP.move_up()
      else:
        self.NP.move_down()

  def shuffle(self):
    
    self.puzzle = self.NP.create_solvable_puzzle()
    self.puzzle_9.setStyleSheet("")
    if self.initial:
      for item in self.Btns:
        self.inital_styles.append(item.styleSheet())
      self.initial = False
    
    for i in range(len(self.Btns)):
      self.Btns[i].setStyleSheet(self.inital_styles[self.goal.index(self.puzzle[i])])
    

  def clear(self):
    return (self.initial == False) and (self.NP.getGoal() == self.NP.getPuzzle())



if __name__ == "__main__":
  app = QApplication(sys.argv)
  widget = MainWindow()
  widget.show()
  
  sys.exit(app.exec())
