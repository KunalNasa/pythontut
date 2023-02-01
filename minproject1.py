from datetime import datetime
class Library:
    def __init__(self, List_of_books, Lib_name):
        self.List_of_books = List_of_books
        self.Lib_name = Lib_name

    def displaybook(self):
        print(f"Welcome to the {self.Lib_name}\nBooks available in Library are listed below:\n")
        sorted_list = sorted(self.List_of_books)
        for i in sorted_list:
            print(i)

    def lendbook(self):
        # inp = input("If you want to lend book, press L.\nIf you don't want to lend any book,press any key.\nThanks.\n")
        # if inp == 'L':
        name = input("Enter your name:\n")
        lending = input("Enter the name of book which you want to lend\n")
        if lending in self.List_of_books:
            self.List_of_books.remove(lending)
            print("Book has been issued to you successfully.\nThe remaining books in Library are:",
                  self.List_of_books, "\n")
            with open("KunalLib.txt", 'a') as f:
                f.write(f"{name} :  {datetime.today()}:  {lending} \n")
        else:
            print(
                "Sorry to tell you that this Book is either not available in our Library or It is issued by someone's else."
                "We will inform you on arrival of this book in our Library.")
            check = input("Press I to check the names of issued books.\nPress any other key to exit.\n")
            if check == 'I':
                k = open("KunalLib.txt")
                print(k.readlines())
                k.close()
            else:
                pass

        # else:
        #     pass

    def addbook(self):
        # adding = input(
        #     "If you want to add any book in our Library Then please press A.\nPress any other key to exit.\nThanks.\n")
        # if adding == 'K':
        print("Books available in our Library are listed below\n", self.List_of_books)
        search = input('Enter the name of book you want to add in our Library.\n')
        if search in self.List_of_books:
            print("The book is already available in our Library.\nThanks for supporting us.")
        else:
            self.List_of_books.append(search)
            print("Updated list of books:\n", self.List_of_books)
        # else:
        #     pass

    def returnbook(self):
        # ret = input("If you want to return issued book please press R.\nOtherwise press any other key to exit.\n")
        # if ret == 'R':
        bookret = input("Enter the name of book you want to return.\n")
        k = open("KunalLib.txt",'r')
        readingfile = str(k.read())
        if bookret in readingfile:
            replace = readingfile.replace(bookret,"")
            print("The book has been returned successfully.\nThanks for using our Library.\n")
            self.List_of_books.append(bookret)
            with open("KunalLib.txt", 'w') as d:
                d.write(replace)
        else:
            print("You have not issued this book before.")
        # else:
        #     pass

Kunal = Library(['"To Kill a Mockingbird" by Harper Lee\n', '"Pride and Prejudice" by Jane Austen\n', '"The Diary of Anne Frank" by Anne Frank\n', '"1984" by George Orwell\n', 'Harry Potter and the Sorcerer\'s Stone" by J.K. Rowling\n', '"The Lord of the Rings" (1-3) by J.R.R. Tolkien\n', '"The Great Gatsby" by F. Scott Fitzgerald\n', '"Charlotte\'s Web" by E.B. White\n', '"The Hobbit" by J.R.R. Tolkien\n', '"Little Women" by Louisa May Alcott\n', '"Fahrenheit 451" by Ray Bradbury\n', '"Jane Eyre" by Charlotte Bronte\n', '"Animal Farm" by George Orwell\n', '"Gone with the Wind" by Margaret Mitchell\n', '"The Catcher in the Rye" by J.D. Salinger\n', '"The Book Thief" by Markus Zusak\n', '"The Adventures of Huckleberry Finn" by Mark Twain\n', '"The Hunger Games" by Suzanne Collins\n', '"The Help" by Kathryn Stockett\n', '"The Lion, the Witch, and the Wadrobe" by C.S. Lewis\n', '"The Grapes of Wrath" by John Steinbeck\n', '"The Lord of the Flies" by William Golding\n', '"The Kite Runner" by Khaled Hosseini\n', '"Night" by Elie Wiesel\n', '"Hamlet" by William Shakespeare\n', '"A Wrinkle in Time" by Madeleine L\'Engle\n', '"Of Mice and Men" by John Steinbeck\n', '"A Tale of Two Cities" by Charles Dickens\n', '"Romeo and Juliet" by William Shakespeare\n', '"The Hitchhikers Guide to the Galaxy" by Douglas Adams\n', '"The Secret Garden" by Frances Hodgson Burnett\n', '"A Christmas Carol" by Charles Dickens\n', '"The Little Prince" by Antoine de Saint-Exupéry\n', '"Brave New World" by Aldous Huxley\n', '"Harry Potter and the Deathly Hallows" by J.K. Rowling\n', '"The Giver" by Lois Lowry\n', '"The Handmaid\'s Tale" by Margaret Atwood\n', '"Where the Sidewalk Ends" by Shel Silverstein\n', '"Wuthering Heights" Emily Bronte\n', '"The Fault in Our Stars" by John Green\n', '"Anne of Green Gables" by L.M. Montgomery\n', '"The Adventures of Tom Sawyer" by Mark Twain\n', '"Macbeth" by William Shakespeare\n', '"The Girl with a Dragon Tattoo" by Stieg Larrson\n', '"Frankenstein" by Mary Shelley\n', '"The Holy Bible: King James Version"\n', '"The Color Purple" by Alice Walker\n', '"The Count of Monte Cristo" by Alexandre Dumas\n', '"A Tree Grows in Brooklyn" by Betty Smith\n', '"East of Eden" by John Steinbeck\n', '"Alice in Wonderland" by Lewis Carroll\n', '"In Cold Blood" by Truman Capote\n', '"Catch-22" by Joseph Heller\n', '"The Stand" by Stephen King\n', '"Outlander" by Diana Gabaldon\n', '"Harry Potter and the Prisoner of Azkaban" by J.K. Rowling\n', '"Enders Game" by Orson Scott Card\n', '"Anna Karenina" by Leo Tolstoy\n', '"Watership Down" by Richard Adams\n', '"Memoirs of a Geisha" by Arthur Golden\n', '"Rebecca" by Daphne du Maurier\n', '"A Game of Thrones" by George R.R. Martin\n', '"Great Expectations" by Charles Dickens\n', '"The Old Man and the Sea" by Ernest Hemingway\n', '"The Adventures of Sherlock Holmes" (#3) by Arthur Conan Doyle\n', '"Les Misérables" by Victor Hugo\n', '"Harry Potter and the Half-Blood Prince" by J.K. Rowling\n', '"Life of Pi" by Yann Martel\n', '"The Scarlet Letter" by Nathaniel Hawthorne\n', '"Celebrating Silence: Excerpts from Five Years of Weekly Knowledge" by Sri Sri Ravi Shankar\n', '"The Chronicles of Narnia" by C.S. Lewis\n', '"The Pillars of the Earth" by Ken Follett\n', '"Catching Fire" by Suzanne Collins\n', '"Charlie and the Chocolate Factory" by Roald Dahl\n', '"Dracula" by Bram Stoker\n', '"The Princess Bride" by William Goldman\n', '"Water for Elephants" by Sara Gruen\n', '"The Raven" by Edgar Allan Poe\n', '"The Secret Life of Bees" by Sue Monk Kidd\n', '"The Poisonwood Bible: A Novel" by Barbara Kingsolver\n', '"One Hundred Years of Solitude" by Gabriel Garcí\xada Márquez\n', '"The Time Traveler\'s Wife" by Audrey Niffenegger\n', '"The Odyssey" by Homer\n', '"The Good Earth (House of Earth #1)" by Pearl S. Buck\n', '"Mockingjay (Hunger Games #3)" by Suzanne Collins\n', '"And Then There Were None" by Agatha Christie\n', '"The Thorn Birds" by Colleen McCullough\n', '"A Prayer for Owen Meany" by John Irving\n', '"The Glass Castle" by Jeannette Walls\n', '"The Immortal Life of Henrietta Lacks" by Rebecca Skloot\n', '"Crime and Punishment" by Fyodor Dostoyevsky\n', '"The Road" by Cormac McCarthy\n', '"The Things They Carried" by Tim O\'Brien\n', '"Siddhartha" by Hermann Hesse\n', '"Beloved" by Toni Morrison\n', '"Slaughterhouse-Five" by Kurt Vonnegut\n', '"Cutting For Stone" by Abraham Verghese\n', '"The Phantom Tollbooth" by Norton Juster\n', '"The Brothers Karamazov" by Fyodor Dostoyevsky\n', '"The Story of My Life" by Helen Keller'], "Kunal's Library")

if __name__ == '__main__':
    while True:
        l = input("Enter 1 for book list.\nEnter 2 for lending book.\nEnter 3 for adding book in libray.\n"
                  "Enter 4 for returning book.\n")
        if l == '1':
            Kunal.displaybook()
        elif l == '2':
            Kunal.lendbook()
        elif l =='3':
            Kunal.addbook()
        elif l == '4':
            Kunal.returnbook()
        else:
            print("You have entered invalid input\nPlease enter the valid input.\n")
            continue
        x = input("Press 'q' to quit and any other key to continue\n")
        if x == 'q':
            exit()
        else:
            continue