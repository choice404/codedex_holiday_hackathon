"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

import curses

class Menu:
    # Constructor for the menu object
    def __init__(self, window, left = 'a', right = 'd'):
        self.__window = window
        self.__width = self.__window.max_width - (8 * self.__window.per_width)
        self.__height = self.__window.max_height - 1
        self.__x = 4 * self.__window.per_width
        self.__y = self.__height - 5
        self.__selected = 0
        self.__current_menu = []
        self.__current_menu_name = ""
        self.__menu_length = len(self.__current_menu)
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        # curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.__left = ord(left)
        self.__right = ord(right)
        self.__menu_arrow = False
        self.__menu_map = {}
        self.__menu_history_stack = []

    # Name: get_current_menu_name
    # Parameters: self
    # Return: (string) self.__current_menu_name
    # Description: Returns the name of the current menu
    def get_current_menu_name(self):
        return self.__current_menu_name

    # Name: append_menu_map
    # Parameters: self, (string) key, (string[]) scene
    # Return: None
    # Description: Adds a menu to the menu map
    def append_menu_map(self, key, menu):
        self.__menu_map[key] = menu

    # Name: get_direction_keys
    # Parameters: self
    # Return: (int) self.__left, (int) self.__right
    # Description: Returns the values to be used to navigate the menu
    def get_direction_keys(self):
        if self.__menu_arrow:
            return [curses.KEY_LEFT], [curses.KEY_RIGHT]
        return [self.__left], [self.__right]

    # Name: move_cursor
    # Parameters: self, (int) dir
    # Return: (int) self.__selected
    # Description: Will change what menu item is selected
    def move_cursor(self, dir):
        self.__selected += dir
        if self.__selected == self.__menu_length:
            self.__selected -= 1
        elif self.__selected < 0:
            self.__selected += 1
        return self.__selected

    # Name: menu_arrow_set
    # Parameters: self
    # Return: (boolean) self.__menu_arrow
    # Description: Menu will be controlled with arrow keys
    def menu_arrow_set(self):
        self.__menu_arrow = True
        return self.__menu_arrow

    # Name: menu_arrow_unset
    # Parameters: self
    # Return: (boolean) self.__menu_arrow
    # Description: Menu will be controlled with the self.__left and self.__right characters
    def menu_arrow_unset(self):
        self.__menu_arrow = False
        return self.__menu_arrow

    # Name: set_menu
    # Parameters: self, string menu_name
    # Return: None
    # Description: Changes which menu to display
    def set_menu(self, menu):
        self.__current_menu = self.__menu_map[menu]
        self.__current_menu_name = menu
        self.__menu_length = len(self.__current_menu)

    # Name: handle_select
    # Parameters: self, (string) menu_item
    # Return: None
    # Description: Handles the selection of a menu item
    def handle_select(self, menu_item):
        if menu_item == 'Back':
            self.set_menu(self.__menu_history_stack.pop())
            self.__selected = 0
            return 'Back'
        elif menu_item == 'Interact':
            return 'Interact'
        elif menu_item == 'Exit':
            exit(0)
        self.__menu_history_stack.append(self.__current_menu_name)
        if menu_item in self.__menu_map:
            self.set_menu(menu_item)
            self.__selected = 0
        return menu_item

    # Name: get_selected
    # Parameters: self
    # Return: (string) self.__current_menu[self.__selected]
    # Description: Returns the currently selected menu item
    def get_selected(self):
        return self.__current_menu[self.__selected]

    # Name: draw
    # Parameters: self, (curses.window) stdscr
    # Return: None
    # Description: Draws the menu on the screen
    def draw(self, stdscr):
        # Get length of the menu based on the number of menu items
        menu_display_length = (self.__menu_length * 3) + 1
        __row = '-' * self.__width
        for i in self.__current_menu:
            menu_display_length += len(i)

        # Get the x coordinate of the menu
        menu_x = (self.__window.get_max_width() - menu_display_length) // 2

        # Draw the menu
        stdscr.addstr(self.__y, self.__x, __row)
        stdscr.addstr(self.__y + 4, self.__x, __row)
        stdscr.addch(self.__y + 1, self.__x, '|')
        stdscr.addch(self.__y + 1, self.__width + self.__x - 1, '|')
        stdscr.addch(self.__y + 2, self.__x, '|')
        stdscr.addch(self.__y + 2, self.__width + self.__x - 1, '|')
        stdscr.addch(self.__y + 3, self.__x, '|')
        stdscr.addch(self.__y + 3, self.__width + self.__x - 1, '|')

        runningX = menu_x + 1
        stdscr.addch(self.__y + 1, runningX, '|')
        stdscr.addch(self.__y + 2, runningX, '|')
        stdscr.addch(self.__y + 3, runningX, '|')
        runningX += 2
        for i, menu_item in enumerate(self.__current_menu):
            item = menu_item

            if self.__selected == i:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(self.__y + 2, runningX, item)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(self.__y + 2, runningX, item)
            runningX += len(item) + 1
            stdscr.addch(self.__y + 1, runningX, '|')
            stdscr.addch(self.__y + 2, runningX, '|')
            stdscr.addch(self.__y + 3, runningX, '|')
            runningX += 2

    # Name: refresh
    # Parameters: self
    # Return: None
    # Description: Refreshes the menu
    def refresh(self):
        self.__width = self.__window.max_width - (8 * self.__window.per_width)
        self.__height = self.__window.max_height - 1
        self.__x = 4 * self.__window.per_width
        self.__y = self.__height - 5


# Name: main
# Parameters: None
# Return: None
# Description: Main function for testing
def main():
  # Enter code here
  print("menu.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
