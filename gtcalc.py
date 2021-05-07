import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango
import math
''' Simple calculator with RPN'''


stack = []
display_locker = True


class MainWindow(Gtk.Window):

    key = Gdk.KEY_0

    def __init__(self):

        Gtk.Window.__init__(self, title="gtCalc")

        self.create_buttons()
        self.create_display()
        self.create_grid()

        self.connect("key-press-event", self.numeric_on_key_press_event)
        self.connect("key-press-event", self.on_key_press_event)

    def create_buttons(self):
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

        self.change_sign = Gtk.Button(label="CHS")
        self.change_sign.connect("clicked", self.do_change_sign)

        self.point = Gtk.Button(label=".")
        self.point.connect("clicked", self.insert_point)

        self.addiction = Gtk.Button(label="+")
        self.addiction.connect("clicked", self.acting_addiction)

        self.subtraction = Gtk.Button(label="-")
        self.subtraction.connect("clicked", self.acting_subtraction)

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

        self.square = Gtk.Button(label="SQR")
        self.square_root = Gtk.Button(label="SQT")

        self.pi_const = Gtk.Button(label="PI")
        self.pi_const.connect("clicked", self.insert_pi_const)

        self.e_const = Gtk.Button(label="E")
        self.e_const.connect("clicked", self.insert_e_const)

    def create_display(self):
        self.display = Gtk.Entry(xalign=1, editable=False)
        self.display.set_max_length(25)
        self.display.modify_font(Pango.FontDescription('Dejavu Sans Mono 11'))
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_hexpand(True)
        self.scrolled_window.set_vexpand(False)
        self.scrolled_window.set_min_content_width(200)
        self.stack_display = Gtk.TextView(editable=False)
        self.textbuffer = self.stack_display.get_buffer()
        self.scrolled_window.add(self.stack_display)
    
    def reload_stack_disply_buffer(self):
        i = 0
        self.textbuffer.set_text("")
        for item in stack:
            i += 1
            self.textbuffer.insert_at_cursor(str(i) + ": " + str(item) + "\n")



    def create_grid(self):
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.add(self.grid)

        self.grid.attach(self.display, 0, 0, 5, 1)
        self.grid.attach(self.scrolled_window, 7, 0, 3, 6)

        self.grid.attach(self.seven, 0, 2, 1, 1)
        self.grid.attach(self.eight, 1, 2, 1, 1)
        self.grid.attach(self.nine, 2, 2, 1, 1)
        self.grid.attach(self.division, 3, 2, 1, 1)
        self.grid.attach(self.enter, 4, 2, 1, 2)
        self.grid.attach(self.square, 5, 2, 1, 1)
        self.grid.attach(self.square_root, 6, 2, 1, 1)

        self.grid.attach(self.four, 0, 3, 1, 1)
        self.grid.attach(self.five, 1, 3, 1, 1)
        self.grid.attach(self.six, 2, 3, 1, 1)
        self.grid.attach(self.multiplication, 3, 3, 1, 1)

        self.grid.attach(self.one, 0, 4, 1, 1)
        self.grid.attach(self.two, 1, 4, 1, 1)
        self.grid.attach(self.three, 2, 4, 1, 1)
        self.grid.attach(self.subtraction, 3, 4, 1, 1)
        self.grid.attach(self.turn_off, 4, 4, 1, 1)

        self.grid.attach(self.zero, 0, 5, 1, 1)
        self.grid.attach(self.change_sign, 1, 5, 1, 1)
        self.grid.attach(self.point, 2, 5, 1, 1)
        self.grid.attach(self.addiction, 3, 5, 1, 1)
        self.grid.attach(self.clear_display, 4, 5, 1, 1)
        self.grid.attach(self.pi_const, 5, 5, 1, 1)
        self.grid.attach(self.e_const, 6, 5, 1, 1)

    def on_close_clicked(self, turn_off):
        Gtk.main_quit()

    def insert_point(self, point):
        if self.display.get_text() != "":
            self.display.set_text(self.display.get_text() + ".")
        else:
            pass

    def do_change_sign(self, change_sign):
        global display_locker
        if display_locker is True:
            self.display.set_text("-")
            display_locker = False
        else:
            pass

    def insert_zero(self, zero):
        global display_locker
        if display_locker is True:
            self.display.set_text("0")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "0")

    def insert_one(self, one):
        global display_locker
        if display_locker is True:
            self.display.set_text("1")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "1")

    def insert_two(self, two):
        global display_locker
        if display_locker is True:
            self.display.set_text("2")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "2")

    def insert_three(self, three):
        global display_locker
        if display_locker is True:
            self.display.set_text("3")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "3")

    def insert_four(self, four):
        global display_locker
        if display_locker is True:
            self.display.set_text("4")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "4")

    def insert_five(self, five):
        global display_locker
        if display_locker is True:
            self.display.set_text("5")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "5")

    def insert_six(self, six):
        global display_locker
        if display_locker is True:
            self.display.set_text("6")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "6")

    def insert_seven(self, seven):
        global display_locker
        if display_locker is True:
            self.display.set_text("7")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "7")

    def insert_eight(self, eight):
        global display_locker
        if display_locker is True:
            self.display.set_text("8")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "8")

    def insert_nine(self, nine):
        global display_locker
        if display_locker is True:
            self.display.set_text("9")
            display_locker = False
        else:
            self.display.set_text(self.display.get_text() + "9")

    def insert_pi_const(self, pi_const):
        self.display.set_text(str(math.pi))

    def insert_e_const(self, e_const):
        self.display.set_text(str(math.e))

    def activate_clear_display(self, clear_display):
        self.display.set_text('')

    def add_to_stack(self, enter):
        global display_locker
        stack.append(float(self.display.get_text()))
        display_locker = True
        self.reload_stack_disply_buffer()

    def acting_addiction(self, addiction):
        global display_locker
        try:
            x = stack[-1]
            stack.pop()
            y = stack[-1]
            stack.pop()
            score = x + y
            stack.append(score)
            self.display.set_text(str(score))
            display_locker = True
            self.reload_stack_disply_buffer()
        except:
            self.textbuffer.set_text("Empty stack")
            pass


    def acting_subtraction(self, subtraction):
        global display_locker
        try:
            x = stack[-1]
            stack.pop()
            y = stack[-1]
            stack.pop()
            score = x - y
            stack.append(score)
            self.display.set_text(str(score))
            display_locker = True
            self.reload_stack_disply_buffer()
        except:
            self.textbuffer.set_text("Empty stack")
            pass

    def acting_multiplication(self, multiplication):
        global display_locker
        try:
            x = stack[-1]
            stack.pop()
            y = stack[-1]
            stack.pop()
            score = x * y
            stack.append(score)
            self.display.set_text(str(score))
            display_locker = True
            self.reload_stack_disply_buffer()
        except:
            self.textbuffer.set_text("Empty stack")
            pass

    def acting_division(self, division):
        global display_locker
        try:
            x = stack[-1]
            stack.pop()
            y = stack[-1]
            stack.pop()
            score = x / y
            stack.append(score)
            self.display.set_text(str(score))
            display_locker = True
            self.reload_stack_disply_buffer()
        except:
            self.textbuffer.set_text("Empty stack")
            pass

    def numeric_on_key_press_event(self, grid, event):
        if event.keyval == Gdk.KEY_0 or event.keyval == Gdk.KEY_KP_0:
            self.insert_zero(self)

        if event.keyval == Gdk.KEY_1 or event.keyval == Gdk.KEY_KP_1:
            self.insert_one(self)

        if event.keyval == Gdk.KEY_2 or event.keyval == Gdk.KEY_KP_2:
            self.insert_two(self)

        if event.keyval == Gdk.KEY_3 or event.keyval == Gdk.KEY_KP_3:
            self.insert_three(self)

        if event.keyval == Gdk.KEY_4 or event.keyval == Gdk.KEY_KP_4:
            self.insert_four(self)

        if event.keyval == Gdk.KEY_5 or event.keyval == Gdk.KEY_KP_5:
            self.insert_five(self)

        if event.keyval == Gdk.KEY_6 or event.keyval == Gdk.KEY_KP_6:
            self.insert_six(self)

        if event.keyval == Gdk.KEY_7 or event.keyval == Gdk.KEY_KP_7:
            self.insert_seven(self)

        if event.keyval == Gdk.KEY_8 or event.keyval == Gdk.KEY_KP_8:
            self.insert_eight(self)

        if event.keyval == Gdk.KEY_9 or event.keyval == Gdk.KEY_KP_9:
            self.insert_nine(self)

    def on_key_press_event(self, grid, event):

        ctrl = (event.state & Gdk.ModifierType.CONTROL_MASK)

        if event.keyval == Gdk.KEY_KP_Separator:
            self.insert_point(self)

        if event.keyval == Gdk.KEY_c:
            self.activate_clear_display(self)

        if event.keyval == Gdk.KEY_Return or event.keyval == Gdk.KEY_KP_Enter:
            self.add_to_stack(self)

        if event.keyval == Gdk.KEY_KP_Add:
            self.acting_addiction(self)

        if event.keyval == Gdk.KEY_KP_Subtract:
            self.acting_subtraction(self)

        if event.keyval == Gdk.KEY_KP_Multiply:
            self.acting_multiplication(self)

        if event.keyval == Gdk.KEY_KP_Divide:
            self.acting_division(self)

        if ctrl and event.keyval == Gdk.KEY_minus:
            self.do_change_sign(self)

        if ctrl and event.keyval == Gdk.KEY_q:
            self.on_close_clicked(self)

        if ctrl and event.keyval == Gdk.KEY_d:
            self.activate_clear_display(self)


if __name__ == '__main__':
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
