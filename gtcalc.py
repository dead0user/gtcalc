#!/usr/bin/python

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
''' Simple calculator with RPN'''


stack = []
display_locker = False


class mainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="gtCalc")

        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.add(self.grid)

        self.display = Gtk.Entry(xalign=1, editable=False)

        self.zero = Gtk.Button(label="0")
        self.zero.connect("clicked", self.insert_zero)

        self.one = Gtk.Button(label="1")
        self.one.connect("clicked", self.insert_one)

        self.two = Gtk.Button(label="2")
        self.two.connect("clicked", self.insert_two)

        self.three = Gtk.Button(label="3")
        self.three.connect("clicked", self.insert_three)

        self.four = Gtk.Button(label="4")
        self.four.connect("clicked", self.insert_four)

        self.five = Gtk.Button(label="5")
        self.five.connect("clicked", self.insert_five)

        self.six = Gtk.Button(label="6")
        self.six.connect("clicked", self.insert_six)

        self.seven = Gtk.Button(label="7")
        self.seven.connect("clicked", self.insert_seven)

        self.eight = Gtk.Button(label="8")
        self.eight.connect("clicked", self.insert_eight)

        self.nine = Gtk.Button(label="9")
        self.nine.connect("clicked", self.insert_nine)

        self.double_zero = Gtk.Button(label="00")
        self.point = Gtk.Button(label=".")

        self.addiction = Gtk.Button(label="+")
        self.addiction.connect("clicked", self.acting_addiction)

        self.substraction = Gtk.Button(label="-")
        self.substraction.connect("clicked", self.acting_substraction)

        self.multiplication = Gtk.Button(label="*")
        self.multiplication.connect("clicked", self.acting_multiplication)

        self.division = Gtk.Button(label="/")
        self.division.connect("clicked", self.acting_division)

        self.enter = Gtk.Button(label="Enter")
        self.enter.connect("clicked", self.add_to_stack)

        self.turn_off = Gtk.Button(label="OFF")
        self.turn_off.connect("clicked", self.on_close_clicked)

        self.clear_display = Gtk.Button(label="CD")
        self.clear_display.connect("clicked", self.activate_clear_display)

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
        self.grid.attach(self.turn_off, 4, 4, 1, 1)

        self.grid.attach(self.zero, 0, 5, 1, 1)
        self.grid.attach(self.double_zero, 1, 5, 1, 1)
        self.grid.attach(self.point, 2, 5, 1, 1)
        self.grid.attach(self.addiction, 3, 5, 1, 1)
        self.grid.attach(self.clear_display, 4, 5, 1, 1)


    def on_close_clicked(self, turn_off):
        Gtk.main_quit()


    def insert_zero(self, zero):
        global display_locker
        if display_locker == True:
            self.display.set_text("0")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "0")


    def insert_one(self, one):
        global display_locker
        if display_locker == True:
            self.display.set_text("1")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "1")


    def insert_two(self, two):
        global display_locker
        if display_locker == True:
            self.display.set_text("2")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "2")


    def insert_three(self, three):
        global display_locker
        if display_locker == True:
            self.display.set_text("3")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "3")


    def insert_four(self, four):
        global display_locker
        if display_locker == True:
            self.display.set_text("4")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "4")


    def insert_five(self, five):
        global display_locker
        if display_locker == True:
            self.display.set_text("5")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "5")


    def insert_six(self, six):
        global display_locker
        if display_locker == True:
            self.display.set_text("6")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "6")


    def insert_seven(self, seven):
        global display_locker
        if display_locker == True:
            self.display.set_text("7")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "7")


    def insert_eight(self, eight):
        global display_locker
        if display_locker == True:
            self.display.set_text("8")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "8")


    def insert_nine(self, nine):
        global display_locker
        if display_locker == True:
            self.display.set_text("9")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "9")


    def activate_clear_display(self, clear_display):
        self.display.set_text('')


    def add_to_stack(self, enter):
        global display_locker
        stack.append(float(self.display.get_text()))
        display_locker = True
        print(stack)


    def acting_addiction(self, addiction):
        global display_locker
        x = stack[-1]
        stack.pop()
        y = stack[-1]
        stack.pop()
        score = x + y
        stack.append(score)
        self.display.set_text(str(score))
        display_locker = True
        print(stack)


    def acting_substraction(self, substraction):
        global display_locker
        x = stack[-1]
        stack.pop()
        y = stack[-1]
        stack.pop()
        score = x - y
        stack.append(score)
        self.display.set_text(str(score))
        display_locker = True
        print(stack)


    def acting_multiplication(self, multiplication):
        global display_locker
        x = stack[-1]
        stack.pop()
        y = stack[-1]
        stack.pop()
        score = x * y
        stack.append(score)
        self.display.set_text(str(score))
        display_locker = True
        print(stack)


    def acting_division(self, division):
        global display_locker
        x = stack[-1]
        stack.pop()
        y = stack[-1]
        stack.pop()
        score = x / y
        stack.append(score)
        self.display.set_text(str(score))
        display_locker = True
        print(stack)


if __name__ == '__main__':
    win = mainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
