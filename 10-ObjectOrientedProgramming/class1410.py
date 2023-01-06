class ebook:
    def __init__(self,title,author,number_of_pages,the_current_page_number):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = the_current_page_number
        self.status = False

    def ebook_open(self):
        self.status = True
    def ebook_close(self):
        self.status = False
    def ebook_status(self):
        print(f"title: {self.title}, author: {self.author}, number of pages: {self.number_of_pages}, the current page number {self.current_page}")
    def read(self,number):
        if self.status == True and self.current_page < self.number_of_pages and self.number_of_pages >= (self.current_page+number):
            self.current_page+=number