import os

class Service:
    def __init__ (self, ident : str):
        self.ident = ident

    def Run (self):
        print (self.ident, ' is now running.')

