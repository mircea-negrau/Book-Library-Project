from src.domain.repository import BookRepository, ClientRepository, RentalRepository
from src.errors.validators import BookValidator, ClientValidator, RentalValidator
from src.services.service import BookService, ClientService, RentalService
from src.services.tests import populate_book_repository, populate_client_repository, populate_rental_repository
from src.ui.console import Console

book_repository = BookRepository()
client_repository = ClientRepository()
rental_repository = RentalRepository()

book_validator = BookValidator()
client_validator = ClientValidator()
rental_validator = RentalValidator()

book_service = BookService(book_repository, book_validator)
client_service = ClientService(client_repository, client_validator)
rental_service = RentalService(book_repository, client_service, rental_repository,
                               book_validator, client_validator, rental_validator)

populate_book_repository(book_service)
populate_client_repository(client_service)
populate_rental_repository(rental_service)

ui = Console(book_service, client_service, rental_service)
ui.run_console()

"""    gui = GUI(book_service, client_service, rental_service)
    gui.run()"""

# todo: ADD TO ENTITY UPDATE THE OPTION TO UPDATE AN ENTITY FOUND BY ID
