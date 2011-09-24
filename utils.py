import gtk
import gobject
gobject.threads_init()
import threading


def async_call(func, callback, *args, **kwargs):
    class GThread(threading.Thread):
        def __init__(self, f, callback, *args, **kwargs):
            super(GThread, self).__init__()
            self._callback = callback
            self._args = args
            self._kwargs = kwargs
            self._f = f

        def run(self):
            retval = None
            exception = None
            try:
                retval = self._f(*self._args, **self._kwargs)
            except Exception, exc:
                exception = exc
            gobject.idle_add(self._callback, retval, exception)

    thread = GThread(func, callback, *args, **kwargs)
    thread.start()



def fake_button_press(window):
    event = gtk.gdk.Event(gtk.gdk.BUTTON_PRESS)
    event.button = 1
    event.window = window
    event.x = 0.5
    event.y = 0.5
    gtk.main_do_event(event)