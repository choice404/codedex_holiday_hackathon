"""
Copyright (C) 2023 Austin "Choisauce" Choi
See end of file for extended copyright information
"""

class Entity:
    def __init__(self, name, description, x=0, y=0, char = '0'):
        self.__name = name
        self.__desc = description
        self.__x = x
        self.__y = y
        self.__char = char

    # Name: get_x
    # Parameters: self
    # Return: (int) self.__x
    # Description: Returns the x coordinate of the entity
    def get_x(self):
        return self.__x

    # Name: set_x
    # Parameters: self, x
    # Return: None
    # Description: Sets the x coordinate of the entity
    def set_x(self, x):
        self.__x = x

    # Name: get_y
    # Parameters: self
    # Return: (int) self.__y
    # Description: Returns the y coordinate of the entity
    def get_y(self):
        return self.__y

    # Name: set_y
    # Parameters: self, y
    # Return: None
    # Description: Sets the y coordinate of the entity
    def set_y(self, y):
        self.__y = y

    # Name: get_name
    # Parameters: self
    # Return: (string) self.__name
    # Description: Returns the name of the entity
    def get_name(self):
        return self.__name

    # Name: set_name
    # Parameters: self, name
    # Return: None
    # Description: Sets the name of the entity
    def set_name(self, name):
        self.__name = name

    # Name: get_desc
    # Parameters: self
    # Return: (string) self.__desc
    # Description: Returns the description of the entity
    def get_desc(self):
        return self.__desc

    # Name: set_desc
    # Parameters: self, description
    # Return: None
    # Description: Sets the description of the entity
    def set_desc(self, description):
        self.__desc = description

    # Name: get_char
    # Parameters: self
    # Return: (char) self.__char
    # Description: Returns the character of the entity
    def get_char(self):
        return self.__char

    # Name: set_char
    # Parameters: self, char
    # Return: None
    # Description: Sets the character of the entity
    def set_char(self, char):
        self.__char = char

    # Name: check_collision
    # Parameters: self, (int[2]) x_bound, (int[2]) y_bound
    # Return: None
    # Description: Checks if the entity is colliding with the set bounds
    def check_collision(self, x_bound, y_bound):
        if self.__x >= x_bound[1]:
            self.__x = x_bound[1] - 1
        if self.__y >= y_bound[1]:
            self.__y = y_bound[1] - 1
        if self.__x <= x_bound[0]:
            self.__x = x_bound[0] + 1
        if self.__y <= y_bound[0]:
            self.__y = y_bound[0] + 1

    # Name: move
    # Parameters: self, (int) dx, (int) dy, (int[2]) x_bound, (int[2]) y_bound
    # Return: None
    # Description: Moves the entity by dx and dy, and checks for collision
    def move(self, dx, dy, x_bound, y_bound):
        self.__y += dy
        self.__x += dx
        self.check_collision(x_bound, y_bound)
    
    # Name: draw
    # Parameters: self
    # Return: None
    # Description: Draws the entity on the screen
    def draw(self, stdscr):
        stdscr.addch(self.__y, self.__x, self.__char)

class Shape:
    # Name: __init__
    # Parameters: self, (int) x, (int) y
    # Return: None
    # Description: Constructor for the Shape object
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    # Name: get_x
    # Parameters: self
    # Return: (int) self.__x
    # Description: Returns the x coordinate of the shape
    def get_x(self):
        return self.__x

    # Name: get_y
    # Parameters: self
    # Return: (int) self.__y
    # Description: Returns the y coordinate of the shape
    def get_y(self):
        return self.__y

class Rectangle(Shape):
    # Name: __init__
    # Parameters: self, (string) text, (int) length, (int) height, (int) x, (int) y
    # Return: None
    # Description: Constructor for the Rectangle object
    def __init__(self, text="", length=1, height=1, x=0, y=0):
        super().__init__(x, y)
        self.__length = length
        self.__height = height
        self.__text = text

    # Name: get_length
    # Parameters: self
    # Return: (int) self.__length
    # Description: Returns the length of the rectangle
    def get_length(self):
        return self.__length

    # Name: set_length
    # Parameters: self, (int) length
    # Return: None
    # Description: Sets the length of the rectangle
    def set_length(self, length):
        self.__length = length

    # Name: get_height
    # Parameters: self
    # Return: (int) self.__height
    # Description: Returns the height of the rectangle
    def get_height(self):
        return self.__height

    # Name: set_height
    # Parameters: self, (int) height
    # Return: None
    # Description: Sets the height of the rectangle
    def set_height(self, height):
        self.__height = height

    # Name: get_text
    # Parameters: self
    # Return: (string) self.__text
    # Description: Returns the text of the rectangle
    def get_text(self):
        return self.__text

    # Name: set_text
    # Parameters: self, (string) text
    # Return: None
    # Description: Sets the text of the rectangle
    def set_text(self, text):
        self.__text = text

    # Name: draw
    # Parameters: self
    # Return: None
    # Description: Draws the rectangle on the screen
    def draw(self, stdscr):

        # Draw the top and bottom borders
        horizontal = ('-' * self.__length) + '-' + '-'
        stdscr.addstr(super().get_y(), super().get_x(), horizontal)
        stdscr.addstr(super().get_y() + self.__length + 1, super().get_x(), horizontal)
        # Draw the left and right borders
        for i in range (self.__height):
            stdscr.addch(super().get_y() + i + 1, super().get_x(), '|')
            stdscr.addch(super().get_y() + i + 1, super().get_x() + self.__length + 1, '|')

# Name: main
# Parameters: None
# Return: None
# Description: Main function for testing
def main():
  # Enter code here
  print("entities.py created")

if __name__ == '__main__':
   main()

"""
Copyright (C) 2023 Austin "Choisauce" Choi

Tuitoy

A library to make pretty Terminal projects by drawing screens, menus, and other components. Uses Curses under the hood

This code is licensed under the MIT License.
Please see the LICENSE file in the root directory of this project for the full license details.
"""
