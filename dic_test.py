#!/usr/bin/env python3
from itertools import islice

colors = { '\033[31m': 'red', '\033[32m': 'green', '\033[33m': 'yellow', '\033[34m': 'blue', '\033[35m': 'magenta', '\033[36m': 'cyan', '\033[37m': 'white', '\033[38;5;0m': 'gray', '\033[38;5;1m': 'maroon', '\033[38;5;2m': 'green', '\033[38;5;3m': 'olive', '\033[38;5;4m': 'navy', '\033[38;5;5m': 'purple', '\033[38;5;6m': 'teal', '\033[38;5;7m': 'silver', '\033[38;5;8m': 'gray', '\033[38;5;9m': 'red', '\033[38;5;10m': 'green', '\033[38;5;11m': 'yellow', '\033[38;5;12m': 'blue', '\033[38;5;13m': 'magenta', '\033[38;5;14m': 'cyan', '\033[38;5;15m': 'white', '\033[38;5;16m': 'gray', '\033[38;5;17m': 'maroon', '\033[38;5;18m': 'green', '\033[38;5;19m': 'olive', '\033[38;5;20m': 'navy', '\033[38;5;21m': 'purple', '\033[38;5;22m': 'teal', '\033[38;5;23m': 'silver', '\033[38;5;24m': 'gray', '\033[38;5;25m': 'red', '\033[38;5;26m': 'green', '\033[38;5;27m': 'yellow', '\033[38;5;28m': 'blue', '\033[38;5;29m': 'magenta', '\033[38;5;30m': 'cyan', '\033[38;5;31m': 'white', '\033[38;5;32m': 'gray', '\033[38;5;33m': 'maroon', '\033[38;5;34m': 'green', '\033[38;5;35m': 'olive', '\033[38;5;36m': 'navy', '\033[38;5;37m': 'purple', '\033[38;5;38m': 'teal', '\033[38;5;39m': 'silver' }

for code, c in colors.items():
  print(f"The color code {code} corresponds to the color {c}.")

'''
for code, c in islice(colors.items(), 10):
  print(f"The color code {code} corresponds to the color {c}.")
  '''
