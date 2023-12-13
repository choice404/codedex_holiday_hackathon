"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

import curses
from . import entities

class Scene:
    # Name: __init__
    # Parameters: self, (string) name, (window.Window) window, (list) entities
    # Return: None
    # Description: Constructor for the scene object
    def __init__(self, name, window, entity_list, show_entities=False, text = [""], text_align="left"):
        self.__name = name
        self.__window = window
        self.__entities = []
        for entity in entity_list:
            self.__entities.append(entity)
        if self.__entities:
            self.__player = self.__entities[0]
        else:
            self.__player = entities.Entity("player", "player", 0, 0, '@')
        self.__show_entities = show_entities
        self.__text = text
        self.__text_align = text_align
        self.__width = self.__window.get_max_width() - (10 * self.__window.get_per_width())
        self.__height = self.__window.get_max_height() - 10
        self.__x = 4 * self.__window.get_per_width()
        self.__y = 1
        self.__x_bounds = [4 * self.__window.per_width, self.__window.max_width - (10 * self.__window.per_width)]
        self.__y_bounds = [1, self.__window.max_height - 10]
        curses.start_color()
        curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)
        self.__event_flag = 0

    # Name: draw
    # Parameters: self, (curses.window) stdscr
    # Return: None
    # Description: Draws the scene
    def draw(self, stdscr):
        horizontal = ('-' * self.__width) + '-' + '-'
        stdscr.addstr(self.__y, self.__x, horizontal)
        stdscr.addstr(self.__y + self.__height + 1, self.__x, horizontal)
        for i in range (self.__height):
            stdscr.addch(self.__y + i + 1, self.__x, '|')
            stdscr.addch(self.__y + i + 1, self.__x + self.__width + 1, '|')
        self.draw_text(stdscr)

    def draw_text(self, stdscr):
        if self.__text_align == "left":
            for i, line in enumerate(self.__text[self.__event_flag].split('\n')):
                stdscr.addstr(self.__y + i + 1, self.__x + 2, line)
        elif self.__text_align == "center":
            for i, line in enumerate(self.__text[self.__event_flag].split('\n')):
                stdscr.addstr(self.__y + i + 1, (self.__window.max_width - len(line)) // 2, line)
        elif self.__text_align == "right":
            for i, line in enumerate(self.__text[self.__event_flag].split('\n')):
                stdscr.addstr(self.__y + i + 1, self.__window.max_width - len(line) - 1, line)

    # Name: get_name
    # Parameters: self
    # Return: (string) self.__name
    # Description: Returns the name of the scene
    def get_name(self):
        return self.__name

    # name: set_name
    # Parameters: self, (string) name
    # Return: None
    # Description: Sets the name of the scene
    def set_name(self, name):
        self.__name = name

    # Name: get_entities
    # Parameters: self
    # Return: (list) self.__entities
    # Description: Returns the entities in the scene
    def get_entities(self):
        return self.__entities

    # Name: set_entities
    # Parameters: self, (Entity[]) entities
    # Return: None
    # Description: Sets the entities in the scene
    def set_entities(self, entities):
        self.__entities = entities

    # Name: get_window
    # Parameters: self
    # Return: (window.Window) self.__window
    # Description: Returns the window of the scene
    def get_window(self):
        return self.__window

    # Name: set_window
    # Parameters: self, (window.Window) window
    # Return: None
    # Description: Sets the window of the scene
    def set_window(self, window):
        self.__window = window

    # Name: handle_key_up
    # Parameters: self
    # Return: None
    # Description: Moves the player up
    def handle_key_up(self):
        self.__player.move(0, -1, self.__x_bounds, self.__y_bounds)

    # Name: handle_key_left
    # Parameters: self
    # Return: None
    # Description: Moves the player left
    def handle_key_left(self):
        self.__player.move(-1, 0, self.__x_bounds, self.__y_bounds)

    # Name: update_event_flag
    # Parameters: self, (int) flag
    # Return: None
    # Description: Updates the event flag
    def update_event_flag(self):
        self.__event_flag += 1
        if self.__event_flag == len(self.__text):
            self.__event_flag = len(self.__text) - 1

    def assign_naughty_or_nice_points(self):
        pass

    # Name: handle_key_down
    # Parameters: self
    # Return: None
    # Description: Moves the player down
    def handle_key_down(self):
        self.__player.move(0, 1, self.__x_bounds, self.__y_bounds)

    # Name: handle_key_right
    # Parameters: self
    # Return: None
    # Description: Moves the player right
    def handle_key_right(self):
        self.__player.move(1, 0, self.__x_bounds, self.__y_bounds)

    # Name: draw_entities
    # Parameters: self, (curses.window) stdscr
    # Return: None
    # Description: Draws the entities in the scene
    def draw_entities(self, stdscr):
        if self.__entities:
            for entity in self.__entities:
                entity.draw(stdscr)

    # Naame: refresh
    # Parameters: self
    # Return: None
    # Description: Refreshes the scene
    def refresh(self):
        self.__width = self.__window.max_width - (10 * self.__window.per_width)
        self.__height = self.__window.max_height - 10
        self.__x = 4 * self.__window.per_width
        self.__y = 1

class TitleScene(Scene):
    # Name: __init__
    # Parameters: self, (string) name, (window.Window) window, (string) title, (Entity[]) entities
    # Return: None
    # Description: Constructor for the TitleScene object
    def __init__(self, name, window, entity_list=[], title=""):
        super().__init__(name, window, entity_list)
        self.__title = title.split('\n')
        self.__title_length = len(self.__title[0])

    # Name: draw
    # Parameters: self, (curses.window) stdscr
    # Return: None
    # Description: Draws the scene
    def draw(self, stdscr):
        super().draw(stdscr)
        for i, line in enumerate(self.__title):
            if i < 5:
                stdscr.attron(curses.color_pair(4))
            elif i < 11:
                stdscr.attron(curses.color_pair(5))
            else:
                stdscr.attron(curses.color_pair(4))

            stdscr.addstr(10 + i, (super().get_window().max_width - self.__title_length) // 2, line)
            if i < 5:
                stdscr.attroff(curses.color_pair(4))
            elif i < 11:
                stdscr.attroff(curses.color_pair(5))
            else:
                stdscr.attroff(curses.color_pair(4))

# Name: main
# Parameters: None
# Return: None
# Description: Main function for testing
def main():
  # Enter code here
  print("scenes.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
