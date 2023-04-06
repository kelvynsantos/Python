import curses 
from curses import wrapper
import queue
import time

maze = [
     ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    for i, row in enumerate(maze):
        ## Enumerate = index and values
        for j, value in enumerate(row):
            stdscr.addstr(i, j*2, value, BLUE)

def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path(maze, stdscr):
    start = "O"
    end  = "X"
    start_pos = find_start(maze, start)
    q = queue.Queue()
    q.put(start_pos, [start_pos])
    visited = set()
    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        if maze[row][col] == end:
            return path

def find_neighbors(maze, row , col):
    neighbors = []
    
def main(stdscr):
    ##standard out put screen argument, override shell
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    # blue_and_black = curses.color_pair(1)
    stdscr.clear()
    # stdscr.addstr(5,5,"hello fellow!", blue_and_black) ##position,output
    print_maze(maze, stdscr)
    stdscr.refresh() 
    stdscr.getch()
    ##get input


wrapper(main)
