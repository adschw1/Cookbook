import pygtk
pygtk.require('2.0')
import gtk

class Base:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        # Set opacity
        self.window.set_opacity(0.25)
        self.window.show()

    def main(self):
        gtk.main()
        
if __name__ == "__main__":
    base = Base()
    base.main()
