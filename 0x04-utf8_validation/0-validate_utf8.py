#!/usr/bin/python3
"""
A method that determines if a given data set
represents a valid UTF-8 encoding.
    """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding
    """
    n_bytes_left = 0
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for byte in data:
        # Check if it's the start of a multi-byte character
        if n_bytes_left == 0:
            # Count leading 1s
            count_ones = 0
            temp_byte = byte
            while temp_byte & 0b10000000:
                count_ones += 1
                temp_byte >>= 1

            if count_ones == 0:
                continue  # Single-byte character

            if count_ones > 4:
                return False  # Illegal leading byte

            n_bytes_left = count_ones - 1

        # Check subsequent bytes for valid UTF-8 sequence
        if n_bytes_left > 0:
            if byte >> 6 != 0b10:
                return False  # Invalid continuation byte
            n_bytes_left -= 1

        # Reset count for next character
        if n_bytes_left == 0:
            continue

    # Check if there are any remaining bytes left
    if n_bytes_left > 0:
        return False

    return True
