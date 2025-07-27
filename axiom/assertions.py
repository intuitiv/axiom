import re
import logging

logger = logging.getLogger(__name__)

def contains_substring(target: str | list[str], substring: str) -> bool:
    """
    Returns True if the target string OR any string in the target list
    contains the given substring (case-insensitive).
    """
    try:
        if isinstance(target, str):
            return substring.lower() in target.lower()
        if isinstance(target, list):
            return any(substring.lower() in str(item).lower() for item in target)
        # If it's another type, convert to string and check
        return substring.lower() in str(target).lower()
    except Exception as e:
        logger.error(f"Error in contains_substring: {e}")
        return False


def is_in_range(value: float, min_val: float, max_val: float) -> bool:
    """
    Returns True if the value is between min_val (inclusive) and max_val (inclusive).
    """
    try:
        return min_val <= float(value) <= max_val
    except (ValueError, TypeError):
        return False


def length_is(items: list, operator: str, expected_length: int) -> bool:
    """
    Compares the length of a list against an expected length.
    Valid operators: '==', '!=', '<', '<=', '>', '>='
    """
    if not hasattr(items, '__len__'):
        return False

    actual_length = len(items)
    op_map = {
        '==': actual_length == expected_length, '!=': actual_length != expected_length,
        '<': actual_length < expected_length, '<=': actual_length <= expected_length,
        '>': actual_length > expected_length, '>=': actual_length >= expected_length,
    }
    if operator not in op_map:
        logger.error(f"Invalid operator '{operator}' for length_is assertion.")
        return False
    return op_map[operator]


def matches_regex(text: str, pattern: str) -> bool:
    """
    Returns True if the text matches the given regular expression.
    """
    try:
        return re.search(pattern, str(text)) is not None
    except re.error as e:
        logger.error(f"Invalid regex in matches_regex: {e}")
        return False


# This is the dictionary that the SDK will import and inject.
assertion_helpers = {
    "contains_substring": contains_substring,
    "is_in_range": is_in_range,
    "length_is": length_is,
    "matches_regex": matches_regex,
}