import pygtk
from minus.auth import MinusAuth

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
        pass

    def __init__(self, auth):
        """
        Creates and shows palyer window

        @type auth: MinusAuth
        @param auth: MinusAuth instance

        """
        if not isinstance(auth, MinusAuth):
            raise ValueError("MinusAuth instance should be provided")

        if not auth.is_logged_in():
            raise Exception("Player window can be launched only after successful login")

        self.window = gtk.Window()

        self.window.set_title("Player")
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


