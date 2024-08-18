#!/usr/bin/python3
# You have n number of locked boxes in front of you.
# Each box is numbered sequentially from 0 to n - 1 and each box\
# may contain keys to the other boxes.
# Write a method that determines if all the boxes can be opened.
# Prototype: def canUnlockAll(boxes)
# boxes is a list of lists
# A key with the same number as a box opens that box.
# You can assume all keys will be positive integers
# There can be keys that do not have boxes
# The first box boxes[0] is unlocked
# Return True if all boxes can be opened, else return False

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.
    """
    opened_boxes = {0}
    total_attempts = len(boxes)

    for _ in range(total_attempts):
        new_keys_found = False
        for i, box in enumerate(boxes):
            if i not in opened_boxes and box:
                for key in box:
                    if key < total_attempts and key not in opened_boxes:
                        opened_boxes.add(key)
                        new_keys_found = True

                opened_boxes.add(i)

        if not new_keys_found:
            break
    return len(opened_boxes) == total_attempts


