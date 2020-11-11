class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author

    @property
    def id(self):
        """
        Function to return the id of the book.
        :return: integer, ID of the book.
        """
        return self.__book_id

    @id.setter
    def id(self, book_id):
        """
        Function to set the id of the book to the given parameter.
        :param book_id: integer, ID of the book to be set as.
        """
        self.__book_id = book_id

    @property
    def title(self):
        """
        Function to return the title of the book.
        :return: string, title of the book.
        """
        return self.__title

    @title.setter
    def title(self, title):
        """
        Function to set the title of the book to the given parameter.
        :param title: string, title of the book to be set as.
        """
        self.__title = title

    @property
    def author(self):
        """
        Function to return the author of the book.
        :return: string, author of the book.
        """
        return self.__author

    @author.setter
    def author(self, author):
        """
        Function to set the author of the book to the given parameter.
        :param author: string, author of the book to be set as.
        """
        self.__author = author


class Client:
    def __init__(self, client_id, name):
        self.__client_id = client_id
        self.__name = name

    @property
    def id(self):
        """
        Function to return the id of the client.
        :return: integer, ID of the client.
        """
        return self.__client_id

    @id.setter
    def id(self, client_id):
        """
        Function to set the id of the client to the given parameter.
        :param client_id: integer, ID of the client to be set as.
        """
        self.__client_id = client_id

    @property
    def name(self):
        """
        Function to return the name of the client.
        :return: string, name of the client.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Function to set the name of the client to the given parameter.
        :param name: string, name of the client to be set as.
        """
        self.__name = name


class Rental:
    def __init__(self, rental_id, book_id, client_id, rented_date, returned_date):
        self.__rental_id = rental_id
        self.__book_id = book_id
        self.__client_id = client_id
        self.__rented_date = rented_date
        self.__returned_date = returned_date

    @property
    def id(self):
        """
        Function to return the id of the rental.
        :return: integer, ID of the rental.
        """
        return self.__rental_id

    @id.setter
    def id(self, rental_id):
        """
        Function to set the ID of the rental to the given parameter.
        :param rental_id: string, ID of the rental to be set as.
        """
        self.__rental_id = rental_id

    @property
    def book_id(self):
        """
        Function to return the ID of the book.
        :return: integer, ID of the book.
        """
        return self.__book_id

    @book_id.setter
    def book_id(self, book_id):
        """
        Function to set the ID of the client to the given parameter.
        :param book_id: integer, ID of the book to be set as.
        """
        self.__book_id = book_id

    @property
    def client_id(self):
        """
        Function to return the ID of the client.
        :return: integer, ID of the client.
        """
        return self.__client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Function to set the ID of the client to the given parameter.
        :param client_id: integer, ID of the client to be set as.
        """
        self.__client_id = client_id

    @property
    def rented_date(self):
        """
        Function to return the date of the rental.
        :return: date, date of the rental.
        """
        return self.__rented_date

    @rented_date.setter
    def rented_date(self, rented_date):
        """
        Function to set the date of the client to the given parameter.
        :param rented_date: date, date of the rental to be set as.
        """
        self.__rented_date = rented_date

    @property
    def returned_date(self):
        """
        Function to return the returned date of the rental.
        :return: date, returned date of the rental.
        """
        return self.__returned_date

    @returned_date.setter
    def returned_date(self, returned_date):
        """
        Function to set the returned date of the rental to the given parameter.
        :param returned_date: date, date of the rental's return to be set as.
        """
        self.__returned_date = returned_date
