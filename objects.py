"""
Copyright (C) 2023 faLALALALA
See end of file for extended copyright information
"""

from tuitoy import entities, menu, scenes, window
import random

def init(stdscr):
    _window = window.Window(stdscr)
    _scenes = [
            scenes.TitleScene("title", _window, [],
"""___________.__               ________                      __   
\\__    ___/|  |__   ____    /  _____/______   ____ _____ _/  |_ 
  |    |   |  |  \\_/ __ \\  /   \\  __\\_  __ \\_/ __ \\\\__  \\\\   __\\
  |    |   |   Y  \\  ___/  \\    \\_\\  \\  | \\/\\  ___/ / __ \\|  |  
  |____|   |___|  /\\_____>  \\________/__|    \\_____>______/__|  
                                                                
_________ .__          .__          __                          
\\_   ___ \\|  |_________|__| _______/  |_  _____ _____    ______ 
/    \\  \\/|  |  \\_  __ \\  |/  ___/\\   __\\/     \\\\__  \\  /  ___/ 
\\     \\___|   Y  \\  | \\/  |\\___ \\  |  | |  Y Y  \\/ __ \\_\\___ \\  
 \\________/___|__/__|  |__/______> |__| |__|_|__|____  /______> 
                                                                
         __________                                             
         \\______   \\ ____   ______ ____  __ __   ____           
          |       _// __ \\ /  ___// ___\\|  |  \\_/ __ \\          
          |    |   \\  ___/ \\___ \\\\  \\___|  |  /\\  ___/          
          |____|___/\\_____>______>\\_____>____/  \\_____>         
                                                               """
        ),
        scenes.Scene("Help", _window, [], text = [
        # Text for help
        """
Christmas is in Danger!!!

Toys have been destroyed by the evil Krampus and scattered across the North Pole!
It's up to you to go on an adventure to work on these toys and accomplish other things along the way!
But depending on what you do, you may end up on the naught or nice list.

To Play:
Use the left and right arrow keys to navigate the menu.
Press enter to select a menu item.

In minigames where you control a character,
the player will be indicated in green
and you can control the player with the wasd keys.
        """],
        text_align = "left"),
        scenes.Scene("Credits", _window, [], text = [
        # Text for credits
        """
The Great Christmas Rescue!

A text adventure game made for the 2023 Codedex Holiday Hackathon made by team faLALALALA

Austin
Hannah
Yaz
        """],
        text_align="center"),
        scenes.Scene("Menu", _window, [], text =
        ["""
        """],
        ),
        scenes.Scene("Start", _window, [], text = [
        """
You wake up in the snow in the North Pole.
You see an elf walking towards you in a panic.

Elf: "Oh no! You're awake! You have to help us!
The toys have been destroyed by the evil Krampus and scattered across the North Pole!
It's up to you to go on an adventure to work on these toys and accomplish other things along the way!
But depending on what you do, you may end up on the naughty or nice list."

What would you like to do?
        """,
        """
Elf: "Thank you for helping us!
We need the toys to be fixed before Christmas and the evil Krampus
to be defeated before he ruins Christmas!
Look around the North Pole to fix the toys and to do other tasks!"
        """,
        ]),
    ]
    _scenes_map = {
            "Title": 0,
            "Help": 1,
            "Credits": 2,
            "Menu": 3,
            "Start": 4,
    }
    _menu = menu.Menu(_window, 'a', 'd')
    _menu.append_menu_map('Title', ['Start', 'Help', 'Credits', 'Exit'])
    _menu.append_menu_map('Help', ['Back'])
    _menu.append_menu_map('Credits', ['Back'])
    _menu.append_menu_map('Start', ['Interact', 'Move', 'Menu'])
    _menu.append_menu_map('General', ['Interact', 'Move', 'Menu']) 
    _menu.append_menu_map('Interact', ['Workshop', 'Stables', 'House', 'Neighborhood', 'Back'])
    _menu.append_menu_map('Workshop', ['Work on Toys', 'Leave Toys Broken'])
    _menu.append_menu_map('Stables', ['Raisin Cookie', 'Chocolate Chip Cookie'])
    _menu.append_menu_map('House', ['Hot Chocolate', ''])
    _menu.append_menu_map('Menu', ['Back'])
    _menu.append_menu_map('Move', ['Workshop', 'Stables', 'Kitchen', 'House', 'Neighborhood', 'Back'])
    _menu.set_menu('Title')
    return _window, _menu, _scenes, _scenes_map

class Snowflake:
    # Name: __init__
    # Parameters: x, y, window
    # Return: None
    # Description: Constructor for Snowflake class
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.char = '*'
        self.window = window

    # Name: draw
    # Parameters: stdscr
    # Return: None
    # Description: Draws the snowflake
    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, self.char)

    # Name: fall
    # Parameters: None
    # Return: None
    # Description: Makes the snowflake fall
    def fall(self):
        self.y += 1
        if self.y == self.window.get_max_height():
            self.y = 0
        self.at_bottom()

    # Name: at_bottom
    # Parameters: None
    # Return: None
    # Description: Moves the snowflake to the top if it reaches the bottom
    def at_bottom(self):
        self.x = random.randint(0, self.window.get_max_width() - 2)

# Name: Main
# Parameters: None
# Return: None
# Description: Main function
def main():
  # Enter code here
  print("objects.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 faLALALALA

The Great Christmas Rescue!

A text adventure game made for the 2023 Codedex Holiday Hackathon

This code is licensed under the GNU General Public License v3.0.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
