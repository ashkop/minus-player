import pygtk
import gobject

pygtk.require20()

import gtk
from utils import async_call
from minus.auth import MinusAuth

class LoginWindow:

    def login(self, widget, data=None):

        self.error_label.hide()

        username = self.username_entry.get_text()

        password = self.password_entry.get_text()
        cursor = gtk.gdk.Cursor(gtk.gdk.WATCH)
        self.window.get_window().set_cursor(cursor)
        self.login_button.set_sensitive(False)
        self.username_entry.set_sensitive(False)
        self.password_entry.set_sensitive(False)
        async_call(self.auth.authenticate, self.auth_cbk, username, password)
#        if self.auth.authenticate(username, password):
#            self.success_callback()
#        else:
#            self.error_label.show()
#            self.password_entry.set_text('')

    def auth_cbk(self, retval, exception):
        if exception or not retval:
            self.window.get_window().set_cursor(None)
            self.login_button.set_sensitive(True)
            self.username_entry.set_sensitive(True)
            self.password_entry.set_sensitive(True)
            self.error_label.show()
            self.password_entry.set_text('')
        else:
            gobject.idle_add(self.success_callback)


    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def draw_button_box(self):

        self.button_box = gtk.HBox(True, 5)

        self.login_button = gtk.Button('Login')
        self.login_button.connect('clicked', self.login)
        self.button_box.pack_start(self.login_button, False, False, 0)

        self.login_button.show()

        self.box.pack_end(self.button_box, False, False, 0)

        self.button_box.show()

    def draw_entries(self):

        self.error_label = gtk.Label()
        self.error_label.set_markup(r'<span font_size="large" color="#FF0000">Bad password</span>')
        self.box.pack_start(self.error_label, True, False, 0)

        login_label = gtk.Label('Username:')
        login_label.set_alignment(0, 0.5)
        self.box.pack_start(login_label, True, False, 0)
        login_label.show()

        self.username_entry = gtk.Entry()
        self.box.pack_start(self.username_entry, True, False, 0)
        self.username_entry.show()

        hint = gtk.Label()
        hint.set_markup(r'Not a member yet? <a href="http://minus.com">Sign Up!</a>')
        hint.set_alignment(0, 0.5)
        self.box.pack_start(hint, True, False, 0)
        hint.show()

        password_label = gtk.Label('Password:')
        password_label.set_alignment(0, 0.5)
        self.box.pack_start(password_label, True, False, 0)
        password_label.show()

        self.password_entry = gtk.Entry()
        self.password_entry.set_visibility(False)
        self.box.pack_start(self.password_entry, True, False, 0)
        self.password_entry.show()

    def keypress(self, widget, event, data=None):
        if event.keyval == gtk.keysyms.Return:
            import utils
            utils.fake_button_press(self.login_button.get_event_window())

    def __init__(self, success_callback, auth):
        """
        Creates and shows login window

        @type success_callback: function
        @type auth: MinusAuth
        @param success_callback: Function to call after successful login
        @param auth MinusAuth: instance
        
        """
        self.auth = auth
        self.success_callback = success_callback

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_events(gtk.gdk.KEY_PRESS_MASK)
        self.window.connect('key_press_event', self.keypress)
        self.window.set_title('Login')
        self.window.connect('delete_event', self.delete_event)
        self.window.set_border_width(10)

        self.box = gtk.VBox(True, 0)
        self.window.add(self.box)


        self.draw_entries()

        self.draw_button_box()

        self.box.show()
        self.window.show()


if __name__ == '__main__':

    auth = MinusAuth()
    window = LoginWindow(None, auth)
    gtk.main()