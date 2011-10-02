import pygtk
from threading import Thread, Event
from minus.api import MinusApi
from Queue import PriorityQueue

pygtk.require20()

import gtk

class PlayerWindow:

    def init_minus_tree(self):
        self.minus_tree = gtk.TreeView(self.minus_store)
        tree_column = gtk.TreeViewColumn()
        name_renderer = gtk.CellRendererText()
        thumb_renderer = gtk.CellRendererPixbuf()
        tree_column.pack_start(thumb_renderer, False)
        tree_column.pack_start(name_renderer, False)
        tree_column.add_attribute(name_renderer, 'text', 1)
        tree_column.add_attribute(thumb_renderer, 'pixbuf', 3)
        self.minus_tree.append_column(tree_column)
        self.minus_tree.set_headers_visible(False)

    def load_minus_folders(self):
        self.folders = self.api.get_user_folders('shkop')
        folder_pb = self.window.render_icon(gtk.STOCK_DIRECTORY, gtk.ICON_SIZE_MENU)
        for folder in self.folders:
            self.minus_store.append(None, [folder.id, folder.name, 1, folder_pb])

    def load_file_for_folder(self):

        while not self.finish_file_loading.is_set():
            folder = self.queue.get()
            folder.files = self.api.get_folder_files(folder)
            self.queue.task_done()

    def load_files(self):
        self.queue = PriorityQueue(5)
        self.finish_file_loading = Event()

        for i in range(5):
            t = Thread(target=self.load_files_for_folder)
            t.daemon = True
            t.start()

        for folder in self.folders:
            self.queue.put(folder, True, None)

        self.finish_file_loading.set()




    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self, api):
        """
        Creates and shows palyer window

        @type api: MinusApi
        @param api: MinusApi instance

        """
        if not isinstance(api, MinusApi):
            raise ValueError("MinusApi instance should be provided")
        self.api = api
        self.window = gtk.Window()
        self.window.set_title("Player")
        self.window.connect('delete_event', self.delete_event)
        #columns - id, name, type, thumbnail
        self.minus_store = gtk.TreeStore(str, str, int, gtk.gdk.Pixbuf)

        self.init_minus_tree()
        self.load_minus_folders()

        self.vbox = gtk.VBox(False, 0)
        self.tree_box = gtk.HBox(True, 10)
        self.tree_box.pack_start(self.minus_tree, True, True, 0)
        self.tree_box.show()
        self.minus_tree.show()
        self.vbox.pack_start(self.tree_box, True, True, 0)

        self.window.add(self.vbox)
        self.vbox.show()
        
        self.window.show()


