from minus.auth import MinusAuth
from ui.login import LoginWindow
from ui.player import PlayerWindow
from minus.api import MinusApi
from minus.transport import MinusTransport

import gtk

auth = MinusAuth()
def login_success():

    player = PlayerWindow(auth)

if __name__ == "__main__":

    login = LoginWindow(login_success, auth)
    gtk.main()
