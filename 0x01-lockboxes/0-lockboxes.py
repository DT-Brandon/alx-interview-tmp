#!/usr/bin/python3
"""
Defines function that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Checks if it is possible to unlock all boxes.

    Args:
        boxes (list): A list of lists representing the boxes and their keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    num_boxes = len(boxes)
    unlocked_set = set([0])  # Set to keep track of unlocked boxes
    keys = boxes[0]  # Keys in the first box

    while keys:
        key = keys.pop(0)
        if key < num_boxes and key not in unlocked_set:
            unlocked_set.add(key)
            keys += boxes[key]

    return len(unlocked_set) == num_boxes
