from enum import Enum


class Color(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def paint(text: str, color: Color) -> str:
    return f"{color.value}{text}{Color.ENDC.value}"

def clear_console():
    print("\n" * 50)