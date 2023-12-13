"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

class Window:
    # Name: __init__
    # Parameters: self, (curses.window) stdscr
    # Return: None
    # Description: Constructor for the window object
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.max_height, self.max_width = self.stdscr.getmaxyx()
        self.per_height = self.max_height // 100
        self.per_width = self.max_width // 100

    # Name: get_stdscr
    # Parameters: self
    # Return: (curses.window) self.stdscr
    # Description: Returns the curses window object
    def get_stdscr(self):
        return self.stdscr

    # Name: get_max_height
    # Parameters: self
    # Return: (int) self.max_height
    # Description: Returns the height of the window
    def get_max_height(self):
        return self.max_height

    # Name: get_max_width
    # Parameters: self
    # Return: (int) self.max_width
    # Description: Returns the width of the window
    def get_max_width(self):
        return self.max_width

    # Name: get_per_height
    # Parameters: self
    # Return: (int) self.per_height
    # Description: Returns the height of the window divided by 100
    def get_per_height(self):
        return self.per_height

    # Name: get_per_width
    # Parameters: self
    # Return: (int) self.per_width
    # Description: Returns the width of the window divided by 100
    def get_per_width(self):
        return self.per_width

    # Name: refresh
    # Parameters: self
    # Return: None
    # Description: Refreshes the window
    def refresh(self):
        self.max_height, self.max_width = self.stdscr.getmaxyx()
        self.per_height = self.max_height // 100
        self.per_width = self.max_width // 100

# Name: main
# Parameters: None
# Return: None
# Description: Main function for testing
def main():
  # Enter code here
  print("window.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
