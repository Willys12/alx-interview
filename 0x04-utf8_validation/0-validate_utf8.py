#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding.
    """


def validUTF8(data):
    """_summary_

    Args:
        data (_type_): _description_

    Returns:
        _type_: _description_
    """
    n_bytes_left = 0

    for byte in data:
        # Check if it's the start of a multi-byte character
        if byte >> 7:
            if n_bytes_left > 0:
                return False  # Invalid sequence
            elif byte >> 6 == 0b11:
                n_bytes_left = 1
            elif byte >> 5 == 0b111:
                n_bytes_left = 2
            elif byte >> 4 == 0b1111:
                n_bytes_left = 3
            else:
                return False  # Invalid start bit pattern

        # Check subsequent bytes for valid UTF-8 sequence
        if n_bytes_left > 0:
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            n_bytes_left -= 1

    # Check if there are any remaining bytes left
    if n_bytes_left > 0:
        return False

    return True
