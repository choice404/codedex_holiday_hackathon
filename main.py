"""
Copyright (C) 2023 faLALALALA
See end of file for extended copyright information
"""

import curses
import time
from tuitoy import entities, menu, scenes, window
# from objects import *
import objects
import frame
import random

# Name: handle_menu_enter
def handle_menu_enter(menu_item):
    pass

# Name: main
# Parameters: (curses.window) stdscr
# Return: None
# Description: Main function
def main(stdscr):
    # Initialize the game
    main_window, main_menu, scenes, scenes_map = objects.init(stdscr)
    game = Game(stdscr, main_window, main_menu, scenes, scenes_map)

    # Run the game
    game.run()

class Game:
    # Name: __init__
    # Parameters: self, (curses.window) stdscr, (window.Window) window, (menu.Menu) menu, (Scene[]) scenes
    # Return: None
    # Description: Constructor for the game object
    def __init__(self, stdscr, window, menu, scenes, scenes_map):
        self.stdscr = stdscr
        curses.curs_set(0)
        self.entities = [entities.Rectangle("", 10, 5, 5)]
        self.window = window
        self.menu = menu
        self.scenes = scenes
        self.scenes_map = scenes_map
        self.current_scene_name = "Title"
        self.current_scene = self.scenes[0]
        self.scene_history_stack = []
        self.frames = frame.Frame()

    # Name: run
    # Parameters: self
    # Return: None
    # Description: Runs the game
    def run(self):

        self.menu.menu_arrow_set()
        left, right = self.menu.get_direction_keys()
        fps = 240

        self.stdscr.nodelay(1)

        snowflakes = []

        for i in range(0, 50):
            snowflakes.append(objects.Snowflake(random.randint(0, self.window.get_max_width() - 1), random.randint(0, self.window.get_max_height() - 1), self.window))

        while True:
            if True:
                self.stdscr.clear()
                self.menu.draw(self.stdscr)
                self.current_scene.draw(self.stdscr)
                self.current_scene.draw_entities(self.stdscr)
                self.frames.increment_frame(fps)
                self.frames.draw(self.stdscr)

                if self.current_scene.get_name() == "title":
                    for snowflake in snowflakes:
                        snowflake.draw(self.stdscr)
                        if self.frames.get_frame() % 16 == 0:
                            snowflake.fall()

                # scene_entities = self.current_scene.get_entities()
                # for entity in scene_entities:
                #     entity.draw()
                

                self.stdscr.refresh()
                self.window.refresh()
                self.current_scene.refresh()
                self.menu.refresh()
                time.sleep(1/fps)

                # Handle key presses
                key = self.stdscr.getch()

                if key == ord('w'):
                    self.current_scene.handle_key_up()
                elif key == ord('a'):
                    self.current_scene.handle_key_left()
                elif key == ord('s'):
                    self.current_scene.handle_key_down()
                elif key == ord('d'):
                    self.current_scene.handle_key_right()

                if key in left:
                    self.menu.move_cursor(-1)
                elif key in right:
                    self.menu.move_cursor(1)

                if key == ord('\n'):
                    value = self.menu.handle_select(self.menu.get_selected())
                    if value == 'Back' and self.menu.get_current_menu_name() == "Start":
                        self.current_scene_name = self.scene_history_stack.pop()
                        self.current_scene = self.scenes[self.scenes_map[self.current_scene_name]]
                    elif value == 'Interact':
                        self.current_scene.update_event_flag()
                    elif value == 'Move':
                        self.menu.set_menu('Move')
                    else:
                        self.scene_history_stack.append(self.current_scene_name)
                        self.current_scene_name = value
                        self.current_scene = self.scenes[self.scenes_map[self.current_scene_name]]
                    

if __name__ == '__main__':
    curses.wrapper(main)

"""
Copyright (C) 2023 faLALALALA

The Great Christmas Rescue!

A text adventure game made for the 2023 Codedex Holiday Hackathon

This code is licensed under the GNU General Public License v3.0.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
