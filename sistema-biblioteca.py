#Sistema de Gestión de Biblioteca

#Gestión del inventario
book_list = []

class Libro:
   def __init__(self, titulo, autor, isbn):
      self.titulo = titulo
      self.autor = autor
      self.isbn = isbn
      self.disponible = True

   ## add new book
   def agregar(titulo, autor, isnb):
      libro = Libro(titulo, autor, isnb)
      book_list.append(libro)
      print("Libro agregado con éxito.")
   
   # borrow a book
   def prestar(isbn):
      for book in book_list:
         if book.isbn == isbn:
            if book.disponible == False:
               print("El libro con ISBN: {} no está disponible".format(isbn))
               return
            else:
               book.disponible = False
               print("Libro prestado con éxito.")
               return
      
      print("No encuentro el libro con ISBN: {}".format(isbn))
      
      
   def devolver(isbn):
      for book in book_list:
         if book.isbn == isbn:
            book.disponible = True
      print("Libro devolvedo con éxito.")
      
   # return list of all books in the library
   def mostrar():
      for book in book_list:
         disponible = ""
         if book.disponible == True:
            disponible = "Sí"
         else:
            disponible = "No"
         print("- {} ({}) - ISBN: {} - Disponible: {}".format(book.titulo, book.autor, book.isbn, disponible))

   # search a book by ISBN
   def buscar(isbn):
      for book in book_list:
         if book.isbn == isbn:
            disponible = ""
            if book.disponible == True:
               disponible = "Sí"
            else:
               disponible = "No"
            print("- {} ({}) - ISBN: {} - Disponible: {}".format(book.titulo, book.autor, book.isbn, disponible))
            return

      print("No encuentro el libro con ISBN: {}".format(isbn))
      

print("Bienvenido al Sistema de Gestión de Biblioteca")
print("1. Agregar libro")
print("2. Prestar libro")
print("3. Devolver libro")
print("4. Mostrar libros")
print("5. Buscar")
print("6. Salir")

is_exit = False

while not is_exit:
   option = int(input("Elige una opción:"))

   while option < 1 or option > 6:
      option = int(input("Esa opción no esta disponible, Por favor. Elige una opción:"))

   if option == 1:
      # add new book
      titulo = input("Título:")
      autor = input("Autor:")
      isbn = input("ISBN:")
      Libro.agregar(titulo, autor, isbn)
   elif option == 2:
      # borrow a book
      isbn = input("Ingresa el ISBN:")
      Libro.prestar(isbn)
   elif option == 3:
      # return a book by ISBN
      isbn = input("Ingresa el ISBN:")
      Libro.devolver(isbn)
   elif option == 4:
      # show all books in library
      Libro.mostrar()
   elif option == 5:
      # search a book by ISBN
      isbn = input("Ingresa el ISBN:")
      Libro.buscar(isbn)
   else:
      #exit
      is_exit = True
      exit(1)
   
      
