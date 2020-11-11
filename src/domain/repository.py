from datetime import date


class BookRepository(object):
    def __init__(self):
        self.__books_list = []
        self.__last_book_id = 0

    def add_book(self, book):
        """
        Function to add a book to the book repository.
        :param book: object, contains the book object to be appended to the repository.
        """
        self.__books_list.append(book)

    def remove_book_by_index(self, index):
        """
        Function to remove a book from the book repository.
        :param index: integer, holds the value of the positional index of the book to be removed from the repository.
        """
        del self.__books_list[index]
        return

    def update_book(self, index, new_book):
        """
        Function to update the details of a book found in the book repository.
        :param index: integer, holds the value of the positional index of the book to be updated from the repository.
        :param new_book: object, contains the updated book object to replace the one found at index in the repository.
        """
        self.__books_list[index] = new_book

    def get_next_book_id(self):
        """
        Function to return the next valid ID for a book in the repository.
        :return: integer, next valid ID for a book.
        """
        self.increment_last_book_id()
        return self.__last_book_id

    def increment_last_book_id(self):
        """
        Function to increment the last used book ID in the repository.
        """
        self.__last_book_id += 1

    def get_all_books(self):
        """
        Function to return the full list of books found in the repository.
        :return: list, containing the full list of books.
        """
        return self.__books_list


class ClientRepository(object):
    def __init__(self):
        self.__clients = []
        self.__last_client_id = 0

    def add_client(self, client):
        """
        Function to add a client to the client repository.
        :param client: object, contains the client object to be appended to the repository.
        """
        self.__clients.append(client)

    def remove_client_by_index(self, index):
        """
        Function to remove a client from the client repository.
        :param index: integer, holds the value of the positional index of the client to be removed from the repository.
        """
        del self.__clients[index]
        return

    def update_client(self, index, new_client):
        """
        Function to update the details of a client found in the client repository.
        :param index: integer, holds the value of the positional index of the client to be updated from the repository.
        :param new_client: object, contains the updated client object to replace the one found at index in the
        repository.
        """
        self.__clients[index] = new_client

    def get_next_client_id(self):
        """
        Function to return the next valid ID for a client in the repository.
        :return: integer, next valid ID for a client.
        """
        self.increment_last_client_id()
        return self.__last_client_id

    def increment_last_client_id(self):
        """
        Function to increment the last used client ID in the repository.
        """
        self.__last_client_id += 1

    def get_all_clients(self):
        """
        Function to return the full list of client found in the repository.
        :return: list, containing the full list of clients.
        """
        return self.__clients


class RentalRepository(object):
    def __init__(self):
        self.__rentals = []
        self.__last_rental_id = 0

    def add_rental(self, rental):
        """
        Function to add a rental to the rental repository.
        :param rental: object, contains the rental object to be appended to the repository.
        """
        self.__rentals.append(rental)

    def return_rental_by_index(self, index):
        """
        Function to remove a rental from the rental repository.
        :param index: integer, holds the value of the positional index of the rental to be removed from the repository.
        """
        rental = self.__rentals[index]
        rental.returned_date = date.today()

    def get_next_rental_id(self):
        """
        Function to return the next valid ID for a rental in the repository.
        :return: integer, next valid ID for a rental.
        """
        self.increment_last_rental_id()
        return self.__last_rental_id

    def increment_last_rental_id(self):
        """
        Function to increment the last used rental ID in the repository.
        """
        self.__last_rental_id += 1

    def get_all_rentals(self):
        """
        Function to return the full list of rental found in the repository.
        :return: list, containing the full list of rentals.
        """
        return self.__rentals
