# python lms short project
"<stdin>",
import datetime
import os
class LMS :
    def __init__(self,list_of_books,library_name):
        self.name = "LMS"
        self.list_of_books = "List_of_books.txt"
        self.list_of_users = "List_of_users.txt"
        self.library_name = library_name
        self.books_dict = {}
        self.users_dict = {}
        ID = 1
        UID = 1
        with open(self.list_of_books) as bk:   #file hanlding
            content = bk.readlines()
            for line in content: 
                self.books_dict.update({str(ID): {'books_title': line.replace("\n",""),'lender_name':'','issue_date':'','status':'Available'}})
                ID = ID + 1
        with open(self.list_of_users) as usr:   #file hanlding
            content = usr.readlines()
            for l in content: 
                self.users_dict.update({str(UID): {'user_name': l.replace("\n","")}})
                UID = UID + 1
        
    def display_books(self):
        print("--------------------------------List of books--------------------------------")
        print("Book Id","\t""\t","Title","\t""\t","STATUS")
        print("-----------------------------------------------------------------------------")
        for key,value in self.books_dict.items():
            
            print(key,"\t\t", value.get("books_title"), "- ""\t", value.get("status"),"")
    def display_user(self):
        print("---------------------------books_user-----List of users--------------------------------")
        print("User Id","\t""\t","Name")
        print("-----------------------------------------------------------------------------")
        for key,value in self.users_dict.items():
            print(key,"\t\t", value.get("user_name"))
            

    def Issue_books(self):
        books_id = input("Enter Books ID")
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['status'] =='Available':
                print(f"This book is already issued to {self.books_dict[books_id]['lender_name']} \
                on {self.books_dict[books_id]['issue_date']}")
                return self.Issue_books
            elif self.books_dict[books_id]['status'] =='Available':
                your_name = input("Enter your name:")
                self.books_dict[books_id]['lender_name'] = your_name
                self.books_dict[books_id]['issue_date'] = current_date
                self.books_dict[books_id]['status'] = 'Issued'
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
                
    def Add_users(self):
        new_user = input("Enter User name")
        if new_user == "" :
            return self.Add_users
        elif len(new_user) > 25 :
            print("Please enter user name containing 20 characters")
            return self.Add_users
        else :
            with open(self.list_of_users,"a") as usr:
                usr.writelines(f"{new_user}\n")
                self.users_dict.update({str(int(max(self.users_dict))+1):{'user_name':new_user}})
                print(f"the user {new_user} has been added successfully")
                
    
    
    def return_books(self):
      books_id = input("Enter Books ID : ")
      if books_id in self.books_dict.keys():
            if self.books_dict[books_id]['status'] == 'Available':
                print("This book is already available in library. Please check book id. !!! ")
                return self.return_books()
            elif not self.books_dict[books_id]['status'] == 'Available':
                self.books_dict[books_id]['lender_name'] = ''
                self.books_dict[books_id]['lend_date'] = ''
                self.books_dict[books_id]['status']= 'Available'
                print("Successfully Updated !!!\n")
      else:
            print("Book ID Not Found !!!")
    

    def Delete_books(self):
        # if element_to_delete == "" :
        #     return self.Delete_books()
        # else :
         element_id = input("Enter ID of book you want to delete: ")
         element_to_delete = element_id
         with open(self.list_of_books,"r") as bk1:
            a = bk1.readlines()
            element_to_delete = 19
            del a[element_to_delete-1]
            print("item deleted Successfully")
            with open(self.list_of_books,"w") as bk1 :
                for line in a:
                    bk1.writelines(line)
            bk1.close()
    def Delete_users(self):
        
         element_id = input("Enter ID of user you want to delete: ")
         element_to_delete = element_id
         with open(self.list_of_users,"r") as usr1:
            a = usr1.readlines()
            element_to_delete = 3
            del a[element_to_delete-1]
            print("item deleted Successfully")
            with open(self.list_of_users,"w") as usr1 :
                for line in a:
                    usr1.writelines(line)

         
if __name__ == "__main__":
    try:
         mylms= LMS("List_of_books.txt","Python,s Library")
         press_key_list = {"D": "Display Books", "I": "Issue Books", "A": "Add Books","S" : "Add User" ,"T":"Delete User","R": "Return Books", "C": "Delete Books" , "U": "Display User","Q": "Quit"}    
        
         key_press = False
         while not (key_press == "q"):
            print(f"\n----------Welcome To {mylms.library_name}'s Library Management System---------\n")
            for key, value in press_key_list.items():
                print("Press", key, "To", value)
            key_press = input("Press Key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                mylms.Issue_books()
                
            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                mylms.Add_books()
            elif key_press == "s":
                print("\nCurrent Selection : ADD USER\n")
                mylms.Add_users()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                mylms.display_books()
            
            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                mylms.return_books()
            elif key_press == "c":
                print("\nCurrent Selection : DELETE BOOK\n")
                mylms.Delete_books()
            elif key_press == "t":
                print("\nCurrent Selection : DELETE USER\n")
                mylms.Delete_users()
            elif key_press == "u":
                print("\nCurrent Selection : DISPLAY USERS\n")
                mylms.display_user()
                
            elif key_press == "q":
                break
            else:
                continue
    except Exception as e:
        
        print("Something went wrong. Please check. !!!")




