"""
Name: Pierre Jordan Harrison
Date: 31 January 2017
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from booklist import Booklist
from book import Book

# Create your main program in this file, using the ReadingListApp class


class ReadingListApp(App):
    information_bar = StringProperty()
    count_the_page = StringProperty()

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.data_list = Booklist()
        self.data_list.get_books()

    def build(self):
        """
        This function is build the kivy app and shows the initial look on the kivy app
        :return: self.root
        """
        self.title = "Reading List by Pierre Jordan Harrison"
        self.root = Builder.load_file('app.kv')
        for each in self.data_list.printed_the_books("r"):
            temp_book = Book(each)
            temp_click = Button(text=each[0])
            temp_click.bind(on_release=self.mark_as_completed)
            temp_click.background_color = temp_book.get_the_color()
            self.root.ids.box_display.add_widget(temp_click)
        pages = self.data_list.get_the_number_of_page("r")
        self.count_the_page = "Total pages to read: {}".format(pages)
        self.information_bar = "Click books to mark them as completed"
        self.root.ids.req_book.state = 'down'
        self.root.ids.comp_book.state = 'normal'
        return self.root

    def clear(self):
        """
        This function is to clear all the available widgets and the TextInput on the BoxLayout
        :return: none
        """
        self.root.ids.title_input.text = ""
        self.root.ids.author_input.text = ""
        self.root.ids.pages_input.text = ""
        self.root.ids.box_display.clear_widgets()

    def list_req(self):
        """
        This function is to giving information about the required books and it will be displayed as button on the BoxLayout
        :return: none
        """
        self.root.ids.box_display.clear_widgets()
        for each in self.data_list.printed_the_books("r"):
            temp_book = Book(each)
            temp_click = Button(text=each[0])
            temp_click.bind(on_release=self.mark_as_completed)
            temp_click.background_color = temp_book.get_the_color()
            self.root.ids.box_display.add_widget(temp_click)
        pages = self.data_list.get_the_number_of_page("r")
        self.count_the_page = "Total pages to read: {}".format(pages)
        self.root.ids.req_book.state = 'down'
        self.root.ids.comp_book.state = 'normal'

    def list_comp(self):
        """
        This function is showing the books which is completed to be displayed as buttons on the BoxLayout
        :return:
        """
        self.root.ids.box_display.clear_widgets()
        for each in self.data_list.printed_the_books("c"):
            temp_click = Button(text=each[0])
            temp_click.bind(on_release=self.comp_books)
            self.root.ids.box_display.add_widget(temp_click)
        pages = self.data_list.get_the_number_of_page("c")
        self.count_the_page = "Total pages completed: {}".format(pages)
        self.root.ids.req_book.state = 'normal'
        self.root.ids.comp_book.state = 'down'

    def mark_as_completed(self,instance):
        """
        This function will be run when a book from required list is clicked
        mark the book as completed
        :param instance:
        :return:
        """
        title = instance.text
        self.data_list.mark_as_completed(title)
        self.information_bar = "{} has been marked completed".format(title)
        self.list_req()

    def add_book(self): #This function to add books
        title = self.root.ids.title_input.text
        author = self.root.ids.author_input.text
        try:
            pages = int(self.root.ids.pages_input.text)
            if title == "" or author == "" or pages == "":
                self.information_bar = "All field must be completed"
            elif pages <= 0:
                self.information_bar = "Invalid page input"
            else:
                self.data_list.add_book(title, author, pages)
                self.information_bar = "{} has been added.".format(title)

        except ValueError: #value error
            self.information_bar = "Invalid page input"
        self.root.ids.title_input.text = ""
        self.root.ids.author_input.text = ""
        self.root.ids.pages_input.text = ""
        self.list_req()

    def comp_books(self,instance):
        title = instance.text
        for each in self.data_list.printed_the_books("c"):
            if each[0] == title:
                self.information_bar = "{} by {}, {} pages(completed)".format(each[0],each[1],each[2])

    def on_stop(self):
        self.data_list.save_new_book()

test = ReadingListApp()
test.run()