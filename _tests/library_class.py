class Library:
  def __init__(self, name):
    self.name = name
    self.books = []

  def show_books(self):
    return list(enumerate(self.books))
  
  def add_book(self, book):
    self.books.append(book)


class Book:
  def __init__(self, name:str, text:list):
    self.current_page = 0
    self.name = name
    self.text = text
  
  def next_page(self):
    if self.current_page < len(self.text - 1):
      self.current_page += 1
    return self.text[self.current_page]

  def prev_page(self):
    if self.current_page > 0:
      self.current_page -= 1

    return self.text[self.current_page]
  
  def read(self):
    return self.text[self.current_page]
    

new_library = Library('Best Library')
new_library.add_book('Lord of the Rings')
print(new_library.show_books())
  
