# create your simple Book class in this file

from booklist import Booklist
class Book():
    def __init__(self,book):
        self.book = book

    def get_the_color(self):
        if int(self.book[2]) > 500:
            get_color = (1,0,0,1)
        elif int(self.book[2]) <= 500:
            get_color = (0,1,1,1)
        return get_color