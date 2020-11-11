import datetime

from src.errors.exceptions import ValidError, RepoError
from src.services.service import exit_application


class Console:
    def __init__(self, book_service, client_service, rental_service):
        self._book_service = book_service
        self._client_service = client_service
        self._rental_service = rental_service
        self._main_menu_commands = {
            1: {"description": "Manage entities", "function_name": self.__ui_get_clients_or_books_for_manage_command},
            2: {"description": "Manage rentals", "function_name": self.__ui_get_rental_option},
            3: {"description": "List entities", "function_name": self.__ui_get_option_for_list_command},
            4: {"description": "Search entities", "function_name": self.__ui_get_option_for_search_command},
            5: {"description": "Create statistics", "function_name": self.__ui_get_option_for_search_option},
            0: {"description": "Exit application", "function_name": exit_application}
        }

    def __ui_get_option_for_search_option(self):
        statistics_commands = {
            1: {"description": "Most rented books", "function_name": self.__ui_get_most_rented_books},
            2: {"description": "Most active clients", "function_name": self.__ui_get_most_active_clients},
            3: {"description": "Most rented authors", "function_name": self.__ui_get_most_rented_authors},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      MANAGE ")
        self.__ui_print_menu_commands_of(statistics_commands)
        self.__ui_get_command_from(statistics_commands)

    def __ui_get_most_active_clients(self):
        rentals_list = self._rental_service.get_all_rentals()
        list_of_clients_and_rental_days = []
        for rental in rentals_list:
            is_in_list = False
            for client in list_of_clients_and_rental_days:
                if client["ID"] == rental.client_id:
                    is_in_list = True
                    rented_date = rental.rented_date
                    returned_date = rental.returned_date
                    if returned_date is None:
                        returned_date = datetime.date.today()
                    rental_time_elapsed = returned_date - rented_date
                    client["Rental days"] += int(rental_time_elapsed.days) + 1
                    break
            if not is_in_list:
                list_of_clients_and_rental_days.append({"ID": rental.client_id, "Rental days": 1})
        list_of_clients_and_rental_days = sorted(list_of_clients_and_rental_days, key=lambda client_rental: client_rental["Rental days"], reverse=True)
        for client in list_of_clients_and_rental_days:
            print(client["ID"], client["Rental days"])

    def __ui_get_most_rented_books(self):
        rentals_list = self._rental_service.get_all_rentals()
        list_of_books_and_rentals_amount = []
        for rental in rentals_list:
            is_in_list = False
            for book in list_of_books_and_rentals_amount:
                if book["ID"] == rental.book_id:
                    is_in_list = True
                    book["Rental amount"] += 1
                    break
            if not is_in_list:
                list_of_books_and_rentals_amount.append({"ID": rental.book_id, "Rental amount": 1})
        list_of_books_and_rentals_amount = sorted(list_of_books_and_rentals_amount,
                                                  key=lambda book_rental: book_rental["Rental amount"], reverse=True)
        for book in list_of_books_and_rentals_amount:
            print(book["ID"], book["Rental amount"])

    def __ui_get_most_rented_authors(self):
        rentals_list = self._rental_service.get_all_rentals()
        list_of_authors_and_rentals_amount = []
        for rental in rentals_list:
            rented_book = self._book_service.get_book_by_book_id(rental.book_id)
            rented_author = rented_book.author
            is_in_list = False
            for author in list_of_authors_and_rentals_amount:
                if author["name"] == rented_author:
                    is_in_list = True
                    author["Rental amount"] += 1
                    break
            if not is_in_list:
                list_of_authors_and_rentals_amount.append({"name": rented_author, "Rental amount": 1})
        list_of_authors_and_rentals_amount = sorted(list_of_authors_and_rentals_amount,
                                                  key=lambda author_rental: author_rental["Rental amount"], reverse=True)
        for author in list_of_authors_and_rentals_amount:
            print(author["name"], author["Rental amount"])

    def __ui_get_clients_or_books_for_manage_command(self):
        manage_commands = {
            1: {"description": "Clients", "function_name": self.__ui_get_client_option},
            2: {"description": "Books", "function_name": self.__ui_get_book_option},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      MANAGE ")
        self.__ui_print_menu_commands_of(manage_commands)
        self.__ui_get_command_from(manage_commands)

    def __ui_get_option_for_list_command(self):
        list_commands = {
            1: {"description": "Clients", "function_name": self.__ui_list_clients},
            2: {"description": "Books", "function_name": self.__ui_list_books},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      LIST")
        self.__ui_print_menu_commands_of(list_commands)
        self.__ui_get_command_from(list_commands)

    def __ui_get_option_for_search_command(self):
        search_commands = {
            1: {"description": "Clients", "function_name": self.__ui_search_client},
            2: {"description": "Books", "function_name": self.__ui_search_book},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      SEARCH ")
        self.__ui_print_menu_commands_of(search_commands)
        self.__ui_get_command_from(search_commands)

    def __ui_search_client(self):
        search_commands = {
            1: {"description": "ID", "function_name": self.__ui_search_client_by_id},
            2: {"description": "Name", "function_name": self.__ui_search_client_by_name},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      SEARCH BY ")
        self.__ui_print_menu_commands_of(search_commands)
        self.__ui_get_command_from(search_commands)

    def __ui_search_book(self):
        search_commands = {
            1: {"description": "ID", "function_name": self.__ui_search_book_by_id},
            2: {"description": "Title", "function_name": self.__ui_search_book_by_title},
            3: {"description": "Author", "function_name": self.__ui_search_book_by_author},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      SEARCH BY ")
        self.__ui_print_menu_commands_of(search_commands)
        self.__ui_get_command_from(search_commands)

    def __ui_search_client_by_id(self):
        client_id = input("Client ID=")
        try:
            client_id = int(client_id)
        except ValueError:
            raise ValueError("Client ID must have a natural integer value.")

        list_of_matching_clients = self._client_service.find_all_clients_matching_id(client_id)
        number_of_matching_clients = len(list_of_matching_clients)

        if number_of_matching_clients == 0:
            raise RepoError(f"No clients found by ID: {client_id}")

        for client in list_of_matching_clients:
            client_current_rentals = self._rental_service.get_client_active_rentals(client.id)
            print(f"{client.id} - {client.name}: {client_current_rentals}")

    def __ui_search_client_by_name(self):
        client_name = input("Client name=")
        list_of_matching_clients = self._client_service.find_all_clients_matching_name(client_name.lower())

        number_of_matching_clients = len(list_of_matching_clients)
        if number_of_matching_clients == 0:
            raise RepoError(f"No clients found by name: {client_name}")

        for client in list_of_matching_clients:
            client_current_rentals = self._rental_service.get_client_active_rentals(client.id)
            print(f"{client.id} - {client.name}: {client_current_rentals}")

    def __ui_search_book_by_id(self):
        book_id = input("Book ID=")
        try:
            book_id = int(book_id)
        except ValueError:
            raise ValueError("Book ID must have a natural integer value.")

        list_of_matching_books = self._book_service.find_all_books_matching_id(book_id)

        number_of_matching_books = len(list_of_matching_books)
        if number_of_matching_books == 0:
            raise RepoError(f"No books found by ID: {book_id}")

        for book in list_of_matching_books:
            book_currently_rented = self._rental_service.get_book_rental_status(book.id)
            print(f"{book.id} - '{book.title}' by {book.author}: ", end="")
            if book_currently_rented is None:
                book_currently_rented = "AVAILABLE"
                print_green(book_currently_rented, "\n")
            else:
                book_currently_rented = "UNAVAILABLE"
                print_red(book_currently_rented, "\n")

    def __ui_search_book_by_title(self):
        book_title = input("Book title=")
        list_of_matching_books = self._book_service.find_all_books_matching_title(book_title.lower())

        number_of_matching_books = len(list_of_matching_books)
        if number_of_matching_books == 0:
            raise RepoError(f"No books found by title: {book_title}")

        for book in list_of_matching_books:
            book_currently_rented = self._rental_service.get_book_rental_status(book.id)
            print(f"{book.id} - '{book.title}' by {book.author}: ", end="")
            if book_currently_rented is None:
                book_currently_rented = "AVAILABLE"
                print_green(book_currently_rented, "\n")
            else:
                book_currently_rented = "UNAVAILABLE"
                print_red(book_currently_rented, "\n")

    def __ui_search_book_by_author(self):
        book_author = input("Book author=")
        list_of_matching_books = self._book_service.find_all_books_matching_author(book_author.lower())

        number_of_matching_books = len(list_of_matching_books)
        if number_of_matching_books == 0:
            raise RepoError(f"No books found by title: {book_author}")

        for book in list_of_matching_books:
            book_currently_rented = self._rental_service.get_book_rental_status(book.id)
            print(f"{book.id} - '{book.title}' by {book.author}: ", end="")
            if book_currently_rented is None:
                book_currently_rented = "AVAILABLE"
                print_green(book_currently_rented, "\n")
            else:
                book_currently_rented = "UNAVAILABLE"
                print_red(book_currently_rented, "\n")

    def __ui_get_client_option(self):
        client_commands = {
            1: {"description": "Add", "function_name": self.__ui_add_client},
            2: {"description": "Update", "function_name": self.__ui_update_client},
            3: {"description": "Remove", "function_name": self.__ui_remove_client},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      CLIENTS")
        self.__ui_print_menu_commands_of(client_commands)
        self.__ui_get_command_from(client_commands)

    def __ui_add_client(self):
        name = input("      Name:")
        self._client_service.add_client(name)
        print_successful("Client successfully added.", "\n")

    def __ui_update_client(self):
        name = input("      Name:")
        new_name = input("      New name:")
        self._client_service.update_client_by_name(name, new_name)
        print_successful("Client successfully updated.", "\n")

    def __ui_remove_client(self):
        name = input("      Name:")
        self._client_service.remove_client_by_name(name)
        print_successful("Client successfully removed.", "\n")

    def __ui_list_clients(self):
        clients_list = self._client_service.get_all_clients()
        for client in clients_list:
            client_current_rentals = self._rental_service.get_client_active_rentals(client.id)
            print(f"{client.id} - {client.name}: {client_current_rentals}")

    def __ui_get_book_option(self):
        book_commands = {
            1: {"description": "Add", "function_name": self.__ui_add_book},
            2: {"description": "Update", "function_name": self.__ui_update_book},
            3: {"description": "Remove", "function_name": self.__ui_remove_book},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("      BOOKS")
        self.__ui_print_menu_commands_of(book_commands)
        self.__ui_get_command_from(book_commands)

    def __ui_add_book(self):
        title = input("      Title:")
        author = input("      Author:")
        self._book_service.add_book(title, author)
        print_successful("Book successfully added.", "\n")

    def __ui_update_book(self):
        title = input("      Title:")
        author = input("      Author:")
        new_title = input("      New title:")
        new_author = input("      New author:")
        self._book_service.update_book(title, author, new_title, new_author)
        print_successful("Book successfully updated.", "\n")

    def __ui_remove_book(self):
        title = input("      Title:")
        author = input("      Author:")
        self._book_service.remove_book_by_title_and_author(title, author)
        print_successful("Book successfully removed.", "\n")

    def __ui_list_books(self):
        books_list = self._book_service.get_all_books()
        for book in books_list:
            book_currently_rented = self._rental_service.get_book_rental_status(book.id)
            print(f"{book.id} - '{book.title}' by {book.author}: ", end="")
            if book_currently_rented is None:
                book_currently_rented = "AVAILABLE"
                print_green(book_currently_rented, "\n")
            else:
                book_currently_rented = "UNAVAILABLE"
                print_red(book_currently_rented, "\n")

    def __ui_get_rental_option(self):
        rental_menu_commands = {
            1: {"description": "Rent a book", "function_name": self.__ui_rental_rent},
            2: {"description": "Return a book", "function_name": self.__ui_rental_return},
            0: {"description": "Back to main menu", "function_name": self.__ui_get_back_to_main_menu}
        }
        print("    RENTALS")
        self.__ui_print_menu_commands_of(rental_menu_commands)
        self.__ui_get_command_from(rental_menu_commands)

    def __ui_rental_rent(self):
        book_id = input("   Book ID: ").strip()
        client_id = input("   Client ID: ").strip()
        self._rental_service.add_rental(book_id, client_id)
        print_successful("Book successfully rented.", "\n")

    def __ui_rental_return(self):
        book_id = input("   Book ID:").strip()
        self._rental_service.return_rental_by_book_id(book_id)
        print_successful("Book successfully returned.", "\n")

    def __get_all_rentals(self):
        rentals_list = self._rental_service.get_all_rentals()
        for index, rental in enumerate(rentals_list):
            print(rental.book_id, rental.client_id, rental.rented_date, rental.returned_date)

    @staticmethod
    def __ui_print_menu_commands_of(current_menu):
        for key in current_menu:
            print(key, current_menu[key]["description"])

    @staticmethod
    def __ui_get_command_from(current_menu):
        input_from_console = int(input(">"))
        try:
            command_key = int(input_from_console)
            if command_key in current_menu:
                command = current_menu[command_key]["function_name"]
                command()
            else:
                raise ValueError("Invalid menu option.")
        except ValueError:
            raise ValueError("Invalid menu option.")

    def __ui_get_back_to_main_menu(self):
        pass

    def run_console(self):
        while True:
            print("    MAIN MENU")
            self.__ui_print_menu_commands_of(self._main_menu_commands)
            try:
                self.__ui_get_command_from(self._main_menu_commands)
            except ValueError as value_error:
                print_error(value_error, "\n")
            except TypeError as type_error:
                print_error(type_error, "\n")
            except ValidError as valid_error:
                print_error(valid_error, "\n")
            except RepoError as repo_error:
                print_error(repo_error, "\n")
            print()
            print("===================================")
            print()