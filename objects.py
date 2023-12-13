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
        scenes.Scene('Backstory', _window, [], text=[
    """
You walk into the dark cave and run into something and fluffy.

Herbert: Well aren't you a cute little one.. You're a long way from Santa's workshop.
Shouldn't you be helping them make some new toys so they have them in time for Christmas?
Why are you here?
...
Well, nobody's ever asked me that question before... 
I didn't always hate Christmas, ya know...
    """,
    """
Herbert: I used to enjoy Christmas, like any other polar bear.
Back when I was a cub, I used to love spending time with my penguin friends.
One day, they went to a monastary and started learning Card Jitsu. 
These ninja penguins weren't allowed to talk with those who weren't studying at the Dojo.

Since I can't see my old friends, Christmas has never been the same.
Every year, I wake up and run to check if they sent me a message or a present for Christmas, only to find the mailbox empty.
Why should everyone else have a good Christmas if I can't have one?
    """
        ]),
        scenes.Scene('Workshop', _window, [], text=[
    """
You see a large set of wooden, double doors. You turn the gold handle and when you open the door, you can hardly believe your eyes.
In the center of the room is the largest Christmas tree you have ever seen, filled with so many colored ornaments and decorations.
Directly under the Christmas tree, there are multiple workshop benches. Each elf is diligently working on constructing and inspecting their toy.
You are about to take a step forward, but an elf with a clip board stops you.
    """
        ]),
        scenes.Scene('Neighborhood', _window, [], text=[
        """
When you reach the top of the giant snow covered hill, you look down and see a small cluster of houses.
As you walk down the hill, you see a group of elves making snowmen and making snow angels. 
One elf walks up to you and asks if you want to join.
        """    
        ]),
        scenes.Scene('House', _window, [], text=[
        """
When you open the door, you are greeted with a warm feeling that you've never experienced before. 
You look to your left and that the wood fireplace is lit. Mrs. Claus is sitting in the chair right next to it, reading a Christmas Story.
She looks up and sees you standing in the doorway. She stands up and walks over to you.

Mrs. Claus: Hello, sweetie. Did you come to take a break from making toys?
        """ 
        ]),
        scenes.Scene('Stables', _window, [], text=[
        """
You walk outside Santa\'s house and see a a Stable. You decide to walk over and check it out.
When you open the stable door, it's so dark you can't even see in front of your hand.
You are just about to turn around and walk back outside when you see a faint red light shining brightly in the distance.
You take one step in front of another, walking closer to the light, in hopes of discovering its original source.
        """
        ]),
        scenes.Scene('Kitchen', _window, [], text=[
        """
After talking with Mrs. Claus, you are greeted with the smell of freshly baked cookies.
You walk over to the counter and see a plate of different types of cookies.
Of course, there is Chocolate Chip cookies. A Christmas Classic!
You see some sugar cookies, snickerdoodles, oatmeal raisin cookies, lady locks, and gingersnap cookies.

        """
        ]),
         scenes.Scene('Back', _window, [], text=[
        """
This is the back menu.

        """
        ]),
    ]
    _scenes_map = {
            "Title": 0,
            "Help": 1,
            "Credits": 2,
            "Menu": 3,
            "Start": 4,
            "Backstory": 5,
            "Workshop": 6,
            "Neighborhood": 7,
            "House": 8,
            "Stables": 9,
            "Kitchen": 10,
            "Back":11
    }
    _menu = menu.Menu(_window, 'a', 'd')
    _menu.append_menu_map('Title', ['Start', 'Help', 'Credits', 'Exit'])
    _menu.append_menu_map('Help', ['Back'])
    _menu.append_menu_map('Credits', ['Back'])
    _menu.append_menu_map('Start', ['Interact', 'Move', 'Inventory', 'Menu'])
    _menu.append_menu_map('General', ['Interact', 'Inventory', 'Menu', 'Back'])
    _menu.append_menu_map('Start', ['Interact', 'Move', 'Inventory', 'Menu', 'Back', 'Exit'])
    _menu.append_menu_map('Menu', ['Back'])
    _menu.append_menu_map('Move', ['Workshop', 'Stables', 'Kitchen', 'House', 'Neighborhood', 'Back'])
    _menu.set_menu('Title')
    return _window, _menu, _scenes, _scenes_map

class Snowflake:
    def __init__(self, x, y, window):
        self.x = x
        self.y = y
        self.char = '*'
        self.window = window

    def draw(self, stdscr):
        stdscr.addstr(self.y, self.x, self.char)

    def fall(self):
        self.y += 1
        if self.y == self.window.get_max_height():
            self.y = 0
        self.at_bottom()

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
