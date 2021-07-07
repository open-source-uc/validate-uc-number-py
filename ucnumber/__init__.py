# coding=utf-8


def validate(identifier):
    """Validates a student id from the Pontifical Catholic University of Chile

    Args:
        identifier: student identifier (string or number)
    Returns:
        True if it is valid, False otherwise
    """

    if not identifier:
        return False

    identifier = str(identifier)
    student_number = identifier[:-1]
    given_digit = identifier[-1].upper()

    counter = 2
    total = 0
    for char in reversed(student_number):
        if not char.isdigit():
            return False

        total += int(char) * counter
        counter += 1
        counter = 2 if counter > 8 else counter

    digit = str(11 - total % 11) if (11 - total % 11 != 10) else 'J'
    digit = '0' if digit == '11' else digit
    return given_digit == digit
