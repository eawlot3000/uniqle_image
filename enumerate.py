#!/usr/bin/env python3
colors = ['red', 'green', 'blue']
for i, color in enumerate(colors):
  print(f"Color {i+5} is {color}.")



from termcolor import colored
string = 'Hello World'
colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
num_colors = len(colors)
for i, s in enumerate(string):
  color = colors[i % num_colors]
  # dont work !!! color = colors[i]
  print(colored(s, color), end='')
