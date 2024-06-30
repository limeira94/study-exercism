"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ['A', 'B', 'C', 'D']
    for i in range(number):
        yield seats[i % 4]
    

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seats = ['A', 'B', 'C', 'D']
    row = 1
    seat_count = 0
    
    while seat_count < number:
        if row == 13:
            row += 1
        for seat in seats:
            if seat_count < number:
                yield f"{row}{seat}"
                seat_count += 1
            else:
                break
        row += 1
        

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers))
    return {passenger: next(seats) for passenger in passengers}
    

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for seat in seat_numbers:
        padding_lenght = 12 - len(seat) - len(flight_id)
        yield f"{seat}{flight_id}{'0' * padding_lenght}"
        

if __name__ == '__main__':
    seat_numbers = ["1A", "17D"]
    flight_id = "CO1234"
    tickets_id = generate_codes(seat_numbers, flight_id)
    
    print(next(tickets_id))
    print(next(tickets_id))