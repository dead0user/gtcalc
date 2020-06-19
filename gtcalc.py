#!/usr/bin/python

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
''' Simple calculator with RPN'''

class mainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="gtCalc")

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.add(self.grid)

        self.display = Gtk.Entry(xalign=1, editable=False)

        self.zero = Gtk.Button(label="0")
        self.one = Gtk.Button(label="1")
        self.two = Gtk.Button(label="2")
        self.three = Gtk.Button(label="3")
        self.four = Gtk.Button(label="4")
        self.five = Gtk.Button(label="5")
        self.six = Gtk.Button(label="6")
        self.seven = Gtk.Button(label="7")
        self.eight = Gtk.Button(label="8")
        self.nine = Gtk.Button(label="9")
        self.double_zero = Gtk.Button(label="00")
        self.point = Gtk.Button(label=".")
        self.addiction = Gtk.Button(label="+")
        self.substraction = Gtk.Button(label="-")
        self.multiplication = Gtk.Button(label="*")
        self.division = Gtk.Button(label="/")
        self.enter = Gtk.Button(label="Enter")

        self.turn_off = Gtk.Button(label="OFF")
        self.turn_off.connect("clicked", self.on_close_clicked)

        self.grid.attach(self.display, 0, 0, 5, 1)

        self.grid.attach(self.seven, 0, 2, 1, 1)
        self.grid.attach(self.eight, 1, 2, 1, 1)
        self.grid.attach(self.nine, 2, 2, 1, 1)
        self.grid.attach(self.division, 3, 2, 1, 1)
        self.grid.attach(self.enter, 4, 2, 1, 2)

        self.grid.attach(self.four, 0, 3, 1, 1)
        self.grid.attach(self.five, 1, 3, 1, 1)
        self.grid.attach(self.six, 2, 3, 1, 1)
        self.grid.attach(self.multiplication, 3, 3, 1, 1)

        self.grid.attach(self.one, 0, 4, 1, 1)
        self.grid.attach(self.two, 1, 4, 1, 1)
        self.grid.attach(self.three, 2, 4, 1, 1)
        self.grid.attach(self.substraction, 3, 4, 1, 1)

        self.grid.attach(self.zero, 0, 5, 1, 1)
        self.grid.attach(self.double_zero, 1, 5, 1, 1)
        self.grid.attach(self.point, 2, 5, 1, 1)
        self.grid.attach(self.turn_off, 3, 5, 1, 1)


    def on_close_clicked(self, turn_off):
        Gtk.main_quit()


if __name__ == '__main__':
    win = mainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
