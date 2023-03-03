"<stdin>",
import datetime
import os
class LMS :
    def __init__(self,list_of_books,library_name):
        self.name = "LMS"
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        ID = 101
        with open(self.list_of_books) as bk:   #file hanlding
            content = bk.readlines()
            for line in content: 
                self.books_dict.update({str(ID): {"books_title": line.replace("\n",""),"lender_name":"","issue_date":"","status":"Available"}})
                ID = ID + 1
        
    def display_books(self):
        print("--------------------------------List of books--------------------------------")
        print("Book Id","\t","Title")
        print("-----------------------------------------------------------------------------")
        for key,value in self.books_dict.items():
            
            print(key,"\t\t", value.get("books_title"), "- [", value.get("status"),"]")

    def Issue_books(self):
        books_id = input("Enter Books ID")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["status"] =="Available":
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} \
                on {self.books_dict[books_id]['issue_date']}")
                return self.Issue_books
            elif self.books_dict[books_id]["status"] =="Available":
                your_name = input("Enter your name:")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['issue_date'] = current_date
                self.books_dict[books_id]['status'] = "Issued"
                print("book issued successfully")
            else:
                print("This book is not available")
    def Add_books(self):
        new_books = input("Enter Book title")
        if new_books == "" :
            return self.Add_books
        elif len(new_books) > 25 :
            print("Please enter book title containing 20 characters")
            return self.Add_books
        else :
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':'','issue_date':'', 'status':'Available'}})
                print(f"the book {new_books} has been added successfully")
    
    def Return_books(self):
        books_id = input("Enter Books ID")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if self.books_dict[books_id]["status"] =="Available":
                print("you entered the wrong id this is already in library")
                return self.Return_books
            elif not self.books_dict[books_id]["status"] =="Available":
                
                self.books_dict[books_id]['lender_name'] = "" 
                self.books_dict[books_id]['issue_date'] = ""
                self.books_dict[books_id]['status'] = "Available"
                print("book returned successfully")
            else:
                print("This book is not available")
    

    def Delete_books(self):
        # # delete_book = input("Enter Books name you want to delete: ")

        # # if delete_book == "" :
        # #     return self.Delete_books()
        # # else :
        # with open(self,list_of_books) as bk1:
        #          a = bk1.readlines()
        #          del a[id - 1]
        #          with open(self.list_of_books,"w") as bk1 :
        #              for line in a:
        #                  bk1.writelines(line) 
                      
                 
    # delete_book=input("book_title:")
    # delete_id_numbers=int(input("id :"))

     
    



l= LMS("List_of_books.txt","Python,s Library")
print(l.Delete_books())    

