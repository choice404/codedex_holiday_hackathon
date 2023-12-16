import dis
import curses

def test(stdscr):
    stdscr.addstr(0, 0, "Hello World!")

    while True:
        key = stdscr.getch()
        if key == ord('q'):
            break

curses.wrapper(test)

print(dis.dis(test))
