#!/usr/bin/env python3
from termcolor import colored # color Error messages
from itertools import cycle

# just get the color name here. eg string "red"


if __name__ == '__main__':
  string = 'Hello World'
  colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
  num = len(colors)
  for i, s in enumerate(string):
    if s != ' ':
      print(colored(s, colors[i%num]), end='')
    else:
      print(s, end = '')


  ''' solution 1. if dont use `cycle`, use `enumerate`
  colors = cycle(['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white'])
  for s, c in zip(string, colors):
    print(colored(s, c), end='')
    '''

