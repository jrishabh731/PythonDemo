# from sqlite3 import connect


class Manager:
    def __init__(self,):
        print('Init')

    def __enter__(self):
        print("__enter__")

    def __exit__(self, *args):
        print("__exit__")

def action():
    with Manager():
        print("Here")

action()