from base64 import b64decode
from zlib import decompress
from pickle import loads
from time import sleep
from datetime import datetime

font = loads(decompress(b64decode(b'eJxrYJlawMgABrVTNHoYDabETtHo7Ojo6Ozo7ATScAIsltrDaAhW0AmXhiiEEUAFRqgmIHAHCAAVGKMrgLOgVphArICZ3gGVQlhhClIANg4iBqUhNoAUmMGsQFKAYoU53ARUN0IIoAILNEdimGCJRUEnsgIraEDBQweFlVqqBwAoWbU3')))
width = 5
height = len(next(iter(font.values())))//width
scale = 2

def color_in(c):
  return "\x1b[1;30;47m" + c + "\x1b[0m"

lines: list[str] = s.splitlines()

def move_cursor_up():
  n = len(lines)
  print(f'\x1b[{n}F', end="")

grid = [list(line.removesuffix("\n")) for line in lines]
saved_grid = [line.copy() for line in grid]

def place(c, x, y):
  for dx in range(width * scale):
    for dy in range(height * scale):
      if font[c][(dy // scale) * width + dx // scale]:
        grid[y + dy][x + dx] = color_in(grid[y + dy][x + dx])

while True:
  grid = [line.copy() for line in saved_grid]
  x, y = 1, 1
  time_string = datetime.now().strftime("%H:%M:%S")

  for c in time_string:
    place(c, x, y)
    x += (width + 1) * scale

  lines = ["".join(line) for line in grid]
  s = "\n".join(lines)
  print(s)
  sleep(1)
  move_cursor_up()

