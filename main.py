from minus.auth import MinusAuth
from ui.login import LoginWindow
from ui.player import PlayerWindow
from minus.api import MinusApi
from minus.transport import MinusTransport

import gtk

auth = MinusAuth()
def login_success():

    m_transport = MinusTransport(auth)
    api = MinusApi(m_transport)
    player = PlayerWindow(api)

login = LoginWindow(login_success, auth)

if __name__ == "__main__":
    login.show()
    gtk.main()
