# create your BookList class in this file

from operator import itemgetter

class Booklist():
    def __init__(self):
        self.book_list = []

    def get_books(self): #to get book from book.csv
        open_file = open("books.csv", "r") #open file from book.csv
        for every in open_file.readlines():
            every = every.strip()
            file = every.split(",")
            self.book_list.append(file)
            self.book_list.sort(key=itemgetter(1, 2))
        open_file.close()
        return self.book_list

    def printed_the_books(self,mark): #to print the books
        data_list = []
        if mark == "r":
            for each in self.book_list:
                if each[3] == "r":
                    data_list.append(each)
        elif mark == "c":
            for index, each in enumerate(self.book_list):
                if each[3] == "c":
                    data_list.append(each)
        return data_list

    def mark_as_completed(self,title): #to mark book as completed
        for i in self.book_list:
            if i[0] == title:
                i[3] = "c"
        return self.book_list

    def add_book(self,title,author,pages): #function to add new book
        data_list = []
        data_list.append(title)
        data_list.append(author)
        data_list.append(pages)
        data_list.append("r")
        self.book_list.append(data_list)
        self.book_list.sort(key=itemgetter(1, 2))
        return self.book_list

    def count_the_pages(self,mark): #to count the page
        int = 0
        for i in self.book_list:
            if mark == "r":
                if i[3] == "r":
                    int += int(i[2])
            elif mark == "c":
                if i[3] == "c":
                    int += int(i[2])
        return int

    def get_the_number_of_page(self,count): #for getting the page
        pages = 0
        for e in self.book_list:
            if count == "r":
                if e[3] == "r":
                    pages += int(e[2])
            if count == "c":
                if e[3] == "c":
                    pages += int(e[2])
        return pages

    def save_new_book(self): #function to save new book
        openfile = open("books.csv","w") #open file in books.csv and write new book to the books.csv
        for each in self.book_list:
            save = "{},{},{},{}".format(each[0],each[1],each[2],each[3])
            openfile.write(save)
        openfile.close()