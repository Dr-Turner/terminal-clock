from datetime import datetime
from os import name, system
import shutil
from time import sleep

clear = 'clear'
if name == 'nt':        # for windows users, bless em!
    clear = 'cls'

def draw(CHARS, timeStr):
    """Draws the clock (pattern & time) onto the terminal"""
    x, y = shutil.get_terminal_size()
    lines = ['{}{}'.format(CHARS[0], CHARS[1]) * 20,
             '{}{}{}'.format(CHARS[1], ' ' * 38, CHARS[0]),
             '{}{}{}'.format(CHARS[0], timeStr.center(38), CHARS[1])]
    for _ in range(int(y/2-2)):
        print('')
    print(lines[0].center(x))
    print(lines[1].center(x))
    print(lines[2].center(x))
    print(lines[1].center(x))
    print(lines[0].center(x))

try:
    while True:
        system(clear)
        dt = datetime.now()
        sd = dt.strftime('%H:%M:%S')  # sd = string date
        last = int(sd[-1:])

        if last % 2 == 0:       # even
            draw(['*', '+'], sd)
        else:                   # odd
            draw(['+', '*'], sd)

        sleep(1)

except KeyboardInterrupt:
    system(clear)
    print('/nClock Exited./n')