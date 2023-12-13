"""
Copyright (C) 2023 faLALALALA
See end of file for extended copyright information
"""

import curses

class Frame:
    def __init__(self):
        self.frame = 0

    def increment_frame(self, fps):
        self.frame += 1
        self.frame = self.frame % fps

    def get_frame(self):
        return self.frame

    def draw(self, stdscr):
        stdscr.addstr(0, 0, f'frame: {str(self.frame)}')

def main():
  # Enter code here
  print("frame.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 faLALALALA

The Great Christmas Rescue!

A text adventure game made for the 2023 Codedex Holiday Hackathon

This code is licensed under the GNU General Public License v3.0.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
