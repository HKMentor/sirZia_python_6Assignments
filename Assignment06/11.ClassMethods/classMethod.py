# Assignment 11:
'''Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.'''
class Book:
    
    total_books = 0
    
    @classmethod
    def increament_book_count(cls):
        
        cls.total_books += 1
    
        
Book.increament_book_count()
Book.increament_book_count()
Book.increament_book_count()
Book.increament_book_count()
Book.increament_book_count()
Book.increament_book_count()


print(f"Total Books: {Book.total_books}")        
        