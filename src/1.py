#!/usr/bin/env python3
# coding: utf8
import curses, curses.textpad
def init(scr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.textpad.rectangle(scr, 0,0,10,10)
    curses.textpad.rectangle(scr, 5,5,20,20)
    textbox = curses.textpad.Textbox(scr)
    content = textbox.edit() # Ctrl+G で終了
    with open('file.txt', 'w') as f:
        f.write(content)
curses.wrapper(init)

