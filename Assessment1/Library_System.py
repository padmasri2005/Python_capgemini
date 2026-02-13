class LibraryBook:
    fine_per_day = 5
    max_days = 10
    def __init__(self,sname,sid):
        self.sname = sname
        self.sid = sid
        # issue_date = False
        # return_date = False
        self.book_issued = False

    def issue_book(self,sid,sname,bookname):
        if self.book_issued == True:
            print("Dear",self.sname,",You already have a book")
            return
        self.book_issued = True
        print("Dear",self.sname,",Book issued successfully")

    def return_book(self,sid,sname,days):
        if self.book_issued == False:
            print("Dear",self.sname,",You have no book to return")
            return
        self.book_issued = False
        LibraryBook.calculate_fine(self,days)
        print("Dear",self.sname,",Book returned successfully")

    def calculate_fine(self,days):
        if(self.book_issued == False):
            print("You have no book to calculate fine")            
            return
        if days > LibraryBook.max_days:
            fine = (days-LibraryBook.max_days)*LibraryBook.fine_per_day
            print("Your fine is:",fine)
        else:
            print("No fine")

    @classmethod
    def update_fine_per_day(cls,new_fine):
        cls.fine_per_day = new_fine
        print("Fine per day updated to:",cls.fine_per_day)


lb1 = LibraryBook("Sri",101)
lb1.issue_book(101,"Sri","Python Programming")

lb2 = LibraryBook("Padma Sri",102)
lb2.issue_book(102,"Padma Sri","Java Programming")

lb1.return_book(101,"Sri",12)
lb1.calculate_fine(28)
lb2.issue_book(102,"Padma Sri","C Programming")
lb2.return_book(102,"Padma Sri",3)    

        
