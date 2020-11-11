from datetime import date
from src.domain.entity import Book, Client, Rental
from src.errors.exceptions import ValidError, RepoError


class BookService:
    def __init__(self, book_repository, book_validator):
        self._book_repository = book_repository
        self._book_validator = book_validator

    def add_book(self, title_as_string, author_name_as_string):
        """
        Function to add a book to the book repository with the title and author name given by the parameters. The
        function creates a new 'Book' entity which then passes through the 'BookValidator'. In case any of the book's
        parameters are incorrect, the book is not added but an error is raised instead. Otherwise, the book is added
        to the book repository.
        :param title_as_string: string, holds the title for the book to be added; it should be between 1 and
        25 characters.
        :param author_name_as_string: string, holds the name of the author for the book to be added; it should be
        between 1 and 25 characters.
        """
        current_book_id = self._book_repository.get_next_book_id()
        current_book = Book(current_book_id, title_as_string, author_name_as_string)
        self._book_validator.validate_book(current_book)
        self._book_repository.add_book(current_book)

    def remove_book_by_title_and_author(self, title_as_string, author_name_as_string):
        """
        Function to remove from the book repository the book having the title and author name as the given parameters.
        If such a book is not found when trying to find it, no book is removed but an error is raised instead.
        :param title_as_string: string, holds the old_title_as_string of the book to be removed.
        :param author_name_as_string: string, holds the name of the old_author_name_as_string of the book to be removed.
        """
        book_index, _ = self.find_book_by_title_and_author(title_as_string, author_name_as_string)
        self._book_repository.remove_book_by_index(book_index)

    def find_book_by_title_and_author(self, title_as_string, author_name_as_string):
        """
        Function to search for a book in the book repository that has the title and author name as the parameters given.
        The title and author name go through a validator. If the book fails the validator, no book is found, but an
        error is raised instead. Otherwise, if the book is found in the book repository, the function returns the book's
        positional index in the repository as well as the 'book' object. If no book is found in the repository, the
        function returns None values for both the index and the 'book' object.
        :param title_as_string: string, holds the title of the book to be found.
        :param author_name_as_string: string, holds the name of the author of the book to be found.
        :return: If book is found, returns the positional index and the 'book' object of the book. Otherwise, returns
        None and None.
        """
        book_to_validate = Book(1, title_as_string, author_name_as_string)
        self._book_validator.validate_book(book_to_validate)
        del book_to_validate

        books_list = self.get_all_books()
        for index, book in enumerate(books_list):
            if book.title == title_as_string and book.author == author_name_as_string:
                return index, book
        return None, None

    def find_all_books_matching_id(self, book_id):
        book_to_validate = Book(book_id, "Narnia", "C.S.Lewis")
        self._book_validator.validate_book(book_to_validate)
        del book_to_validate

        books_list = self.get_all_books()
        list_of_matching_books = []
        for book in books_list:
            if str(book_id) in str(book.id):
                list_of_matching_books.append(book)
        return list_of_matching_books

    def find_all_books_matching_title(self, book_name_as_string):
        book_to_validate = Book(1, book_name_as_string, "Best Author")
        self._book_validator.validate_book(book_to_validate)
        del book_to_validate

        books_list = self.get_all_books()
        list_of_matching_books = []
        for book in books_list:
            if book_name_as_string in book.title.lower():
                list_of_matching_books.append(book)
        return list_of_matching_books

    def find_all_books_matching_author(self, book_author_as_string):
        book_to_validate = Book(1, "Best Title", book_author_as_string)
        self._book_validator.validate_book(book_to_validate)
        del book_to_validate

        books_list = self.get_all_books()
        list_of_matching_books = []
        for book in books_list:
            if book_author_as_string in book.author.lower():
                list_of_matching_books.append(book)
        return list_of_matching_books

    def update_book(self, old_title_as_string, old_author_name_as_string, new_title_as_string,
                    new_author_name_as_string):
        """
        Function to update the details of an already existing book from the book repository that has the title and
        author name as the given parameters. The book is checked if it exists in the book repository. If no book is
        found, then no book updates but an error is raised instead. Otherwise, the updated book goes through a book
        validator. If it does not pass the validation, no book is updated but an error is raised instead. Otherwise,
        the book gets updated in the book repository.
        :param old_title_as_string: string, holds the title of the book to be updated.
        :param old_author_name_as_string: string, holds the name of the author of the book to be updated
        :param new_title_as_string: string, holds the new title the book will be updated with.
        :param new_author_name_as_string: holds the new author name the book will be updated with.
        """
        book_index, book_to_update = self.find_book_by_title_and_author(old_title_as_string, old_author_name_as_string)
        if book_to_update is None:
            raise RepoError("Book not found. ")
        book_id = book_to_update.id
        updated_book = Book(book_id, new_title_as_string, new_author_name_as_string)
        self._book_validator.validate_book(updated_book)
        self._book_repository.update_book(book_index, updated_book)

    def get_book_by_book_id(self, book_id):
        books_list = self._book_repository.get_all_books()
        for book in books_list:
            if book.id == book_id:
                return book
        return None

    def get_all_books(self):
        """
        Function to return all the books found in the book repository, in a list.
        :return: list, containing all the books found in the book repository.
        """
        books_list = self._book_repository.get_all_books()
        return books_list[:]


class ClientService:
    def __init__(self, client_repository, client_validator):
        self._client_repository = client_repository
        self._client_validator = client_validator

    def add_client(self, client_name_as_string):
        """
        Function to add a client to the client repository with the name given by the parameter. The function creates a
        new 'Client' entity which then passes through the 'ClientValidator'. In case any of the client's parameters are
        incorrect, the client is not added but an error is raised instead. Otherwise, the client is added to the
        client repository.
        :param client_name_as_string: string, holds the name for the client to be added; it should be
        between 1 and 25 characters.
        """
        client_id = self._client_repository.get_next_client_id()
        client = Client(client_id, client_name_as_string)
        self._client_validator.validate_client(client)
        self._client_repository.add_client(client)

    def remove_client_by_name(self, client_name_as_string):
        """
        Function to remove the client from the client repository with the name given by the parameter. The function
        tries to find the positional index of the client in the repository. If no client is found, no client is removed
        but an error is raised instead. Otherwise, the client is removed from the client repository.
        :param client_name_as_string: string, holds the name of the client to be removed from the repository.
        """
        client_index, _ = self.find_client_by_name(client_name_as_string)
        if client_index is None:
            raise RepoError("Name not found. ")
        self._client_repository.remove_client_by_index(client_index)

    def find_client_by_name(self, client_name_as_string):
        """
        Function to find a client in the client repository that has the name given by the parameter. The function tries
        to validate the client to be searched for. If the client fails the validation, no client is returned but an
        error is raised instead. Otherwise, the client is looked for in the client repository. If the client is found,
        the function returns the client's positional index and the 'client' object. Otherwise, the function returns
        None and None.
        :param client_name_as_string: string, holds the name of the client to be searched for.
        :return: If client is found, returns the positional index and the 'client' object from the client repository.
        Otherwise, the function returns None for both values.
        """
        client_to_validate = Client(1, client_name_as_string)
        self._client_validator.validate_client(client_to_validate)
        del client_to_validate

        clients_list = self.get_all_clients()
        for index, client in enumerate(clients_list):
            if client.name == client_name_as_string:
                return index, client
        return None, None

    def find_all_clients_matching_name(self, client_name_as_string):
        client_to_validate = Client(1, client_name_as_string)
        self._client_validator.validate_client(client_to_validate)
        del client_to_validate

        clients_list = self.get_all_clients()
        list_of_matching_clients = []
        for client in clients_list:
            if client_name_as_string in client.name.lower():
                list_of_matching_clients.append(client)
        return list_of_matching_clients

    def find_all_clients_matching_id(self, client_id):
        client_to_validate = Client(client_id, "Mark")
        self._client_validator.validate_client(client_to_validate)
        del client_to_validate

        clients_list = self.get_all_clients()
        list_of_matching_clients = []
        for client in clients_list:
            if str(client_id) in str(client.id):
                list_of_matching_clients.append(client)
        return list_of_matching_clients

    def update_client_by_name(self, old_name_as_string, new_name_as_string):
        """
        Function to update the details of an already existing client from the client repository. The function tries to
        find the client in the client repository. If no client is found, no client is updated but an error is raised
        instead. Otherwise, the client's new details are passed through a 'ClientValidator'. If the validation fails,
        no client is updated but an error is raised instead. Otherwise, the client is updated with the new details.
        :param old_name_as_string: string, holds the name of the client to be updated in the repository.
        :param new_name_as_string: string, holds the name the client will be updated with.
        """
        client_index, client = self.find_client_by_name(old_name_as_string)
        if client is None:
            raise RepoError("Name not found. ")
        client_id = client.id
        new_client = Client(client_id, new_name_as_string)
        self._client_validator.validate_client(new_client)
        self._client_repository.update_client_by_name(client_index, new_client)

    def get_all_clients(self):
        """
        Function to return all the clients found in the client repository, in a list.
        :return: list, containing all the clients found in the client repository.
        """
        clients_list = self._client_repository.get_all_clients()
        return clients_list[:]


class RentalService:
    def __init__(self, book_repository, client_repository, rental_repository,
                 book_validator, client_validator, rental_validator):
        self._book_repository = book_repository
        self._client_repository = client_repository
        self._rental_repository = rental_repository

        self._book_validator = book_validator
        self._client_validator = client_validator
        self._rental_validator = rental_validator

    def add_rental(self, book_id, client_id):
        """
        Function to add a rental to the rental repository with the book and client IDs given by the parameters. The
        function creates a new 'Rental' entity which then passes through the 'RentalValidator'. In case any of the
        rental's parameters are incorrect, the rental is not added but an error is raised instead. Otherwise, the
        function checks whether the book is available for rent. If it is not, then no rental is added but an error is
        raised instead. Otherwise, the rental is added to the rental repository.
        :param book_id: integer, holds the ID value of the book that is rented.
        :param client_id: integer, holds the ID value of the client that rents the book.
        """
        self._rental_validator.validate_book_and_client_ids(book_id, client_id)

        book_id = int(book_id)
        client_id = int(client_id)

        is_valid_book = self.is_book_id_in_repository(book_id)
        if is_valid_book:
            is_valid_client = self.is_client_id_in_repository(client_id)
            if is_valid_client:
                is_book_available = self.is_book_available_by_book_id(book_id)
                if is_book_available:
                    rental_id = self._rental_repository.get_next_rental_id()
                    rented_date = date.today()
                    returned_date = None
                    rental = Rental(rental_id, book_id, client_id, rented_date, returned_date)
                    self._rental_validator.validate_rental(rental)
                    self._rental_repository.add_rental(rental)
                else:
                    raise RepoError("Book is currently rented. ")
            else:
                raise RepoError("Client ID not found. ")
        else:
            raise RepoError("Book ID not found. ")

    def return_rental_by_id(self, rental_id):
        """
        Function to return a rental by the 'rental_id'. The function verifies if the 'rental_id' is valid. If it is not,
        then no rental is returned but an error is raised instead. Otherwise, the function searches for the rental in
        the rental repository. If no rental is found, no rental is returned but an error is raised instead. Otherwise,
        the rental is marked as returned with the current date as the 'returned_date'.
        :param rental_id: integer, holds the ID of the rental to be returned.
        """
        try:
            rental_id = int(rental_id)
        except ValueError:
            raise ValidError("Rental ID must have natural number value. ")
        rental_index = self.find_rental_index_by_id(rental_id)
        if rental_index is None:
            raise RepoError("Rental ID not found. ")
        self._rental_repository.return_rental_by_index(rental_index)

    def return_rental_by_book_id(self, book_id):
        """
        Function to return the rental by the 'book_id'. The function verifies if the 'book_id' is valid. If it is not,
        then no rental is returned but an error is raised instead. Otherwise, the function searches for the book in the
        book repository. If no book is found, no rental is returned but an error is raised instead. Otherwise, the ID of
        rental of the book is looked for. If no rental ID is found active for the book at the moment, no rental is
        returned but an error is raised instead. Otherwise, the rental is marked as returned with the 'returned_date' of
        today.
        :param book_id: integer, holds the ID of the book whose rental will be returned.
        """
        self._rental_validator.validate_book_and_client_ids(book_id, 5)
        book_id = int(book_id)

        is_valid_book = self.is_book_id_in_repository(book_id)
        if not is_valid_book:
            raise RepoError("Book ID not found. ")

        rental_id = self.find_rental_id_by_book_id(book_id)
        if rental_id is None:
            raise RepoError("Book is not rented. ")

        self.return_rental_by_id(rental_id)

    def find_rental_id_by_book_id(self, book_id):
        """
        Function to search for a 'rental_id' being given the 'book_id' of the rental. If the active rental having the
        'book_id' value as the given parameter is found, the function returns the ID of the rental. Otherwise, it
        returns None.
        :param book_id: integer, holds the ID value of the rental's 'book_id'.
        :return: If rental is found, it returns the rental's ID. Otherwise, it returns None.
        """
        rentals_list = self.get_all_rentals()
        for rental in rentals_list:
            if rental.book_id == book_id:
                return rental.id
        return None

    def find_rental_index_by_id(self, rental_id):
        """
        Function to search for the index of the rental being given the 'book_id' of it. If the active rental having the
        'rental_id' value as the given parameter is found, the function returns the index of the rental. Otherwise, it
        returns None.
        :param rental_id: integer, holds the ID value of the rental.
        :return: If rental is found, it returns the rental's index. Otherwise, it returns None.
        """
        rentals_list = self.get_all_rentals()
        for index, rental in enumerate(rentals_list):
            if rental.id == rental_id:
                return index
        return None

    def is_book_available_by_book_id(self, book_id):
        """
        Function to return whether or not a book from the book repository is currently available for rent or not.
        If a book having the book_id value as the given parameter is found having the 'returned_date' as None, it means
        that the book is currently rented already, so the function returns that the book's availability is False.
        Otherwise, it returns True.
        :param book_id: integer, holds the ID value of the book to be checked if available in the book repository.
        :return: True/False, whether or not the book having the 'book_id' given by the parameter is available or not.
        """
        rentals_list = self.get_all_rentals()
        for rental in rentals_list:
            if rental.book_id == book_id and rental.returned_date is None:
                return False
        return True

    def is_book_id_in_repository(self, book_id):
        """
        Function to return whether or not a book having the 'book_id' as the given parameter is found in the book
        repository.
        :param book_id: integer, holds the ID value of the book to be looked for in the repository.
        :return: True/False, whether or not the book having the 'book_id' given by the parameter is found or not.
        """
        books_list = self._book_repository.get_all_books()
        for book in books_list:
            if book.id == book_id:
                return True
        return False

    def is_client_id_in_repository(self, client_id):
        """
        Function to return whether or not a book having the 'client_id' as the given parameter is found in the book
        repository.
        :param client_id: integer, holds the ID value of the client to be looked for in the repository.
        :return: True/False, whether or not the book having the 'client_id' given by the parameter is found or not.
        """
        clients_list = self._client_repository.get_all_clients()
        for client in clients_list:
            if client.id == client_id:
                return True
        return False

    def get_all_rentals(self):
        """
        Function to get the full list of rentals found in the rental repository.
        :return: list, all the rentals found in the rental repository.
        """
        rentals_list = self._rental_repository.get_all_rentals()
        return rentals_list[:]

    def get_client_active_rentals(self, client_id):
        """
        Function to get the full list of active rentals found in the rental repository appointed to the client holding
        the 'client_id' as the given parameter.
        :param client_id: integer, holds the ID value of the client whose active rentals will be searched for.
        :return: list, all the active rentals found in the rental repository appointed to the given client.
        """
        rentals_list = self._rental_repository.get_all_rentals()
        client_active_rentals_list = []
        for rental in rentals_list:
            if rental.client_id == client_id and rental.returned_date is None:
                client_active_rentals_list.append(rental.book_id)
        return client_active_rentals_list[:]

    def get_book_rental_status(self, book_id):
        """
        Function to return the ID of the client that currently rents the book having the 'book_id' as the given
        parameter. If no rental is found, the function returns None. Otherwise, the function returns the ID of the
        client.
        :param book_id: integer, holds the ID value of the book to be looked for in the active rentals from the
        rentals repository.
        :return: the ID of the client that currently rents the book, otherwise None
        """
        rentals_list = self._rental_repository.get_all_rentals()
        for rental in rentals_list:
            if rental.book_id == book_id and rental.returned_date is None:
                return rental.client_id
        return None


def exit_application():
    exit()