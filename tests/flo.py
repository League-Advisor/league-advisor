import builtins
import difflib
import sys
import re

def diff(start_func, path=""):
    """runs a given methods function and compares output with contents of given simulation

    Args:
    ---

    start_func (function): function that start the program.

    path (str): File path to a simulation text tile. Defaults to "".

    Returns: list: Reports for any lines that differ
    """

    text = ""
    expected_lines = _parse_expected_lines(path)
    responses = _extract_responses(expected_lines)


    # inner function to mock print functionality
    def mock_print(*args):
        nonlocal text
        text += "".join(args) + "\n"
        text = re.sub(r'\x1b(\[.*?[@-~]|\].*?(\x07|\x1b\\))', '', text)


    # # inner function to mock input functionality
    def mock_input(*args):
        nonlocal text
        if not responses:
            sys.exit(1)
        response = responses.pop(0)
        text += "".join(args) + response + "\n"

        return response


    # # store the "real" print & input so we can restore them later
    real_print = builtins.print
    real_input = builtins.input


    # # mock the built in print & input
    builtins.print = mock_print
    builtins.input = mock_input


    try:
        start_func()
    except SystemExit:
        real_print("No problem. System exits are allowed in this app.")


    # # restore the "real" print and output functions
    builtins.print = real_print
    builtins.input = real_input

    return _find_differences(text, expected_lines)


# functions "private" to the module use leading underscore convention
# WARNING: they are not TRULY private, which is truly pythonic
def _parse_expected_lines(path):
    if path:
        with open(path) as f:
            expected_lines = f.read().splitlines()
    return expected_lines

def _extract_responses(lines):
    responses = []
    for line in lines:
        if line.startswith(">"):
            response = line.replace("> ", "").strip()
            responses.append(response)

    return responses


def _find_differences(text, expected_lines):
    
    actual_lines = text.splitlines()
    diffed = difflib.unified_diff(actual_lines, expected_lines)

    return "\n".join(diffed)
