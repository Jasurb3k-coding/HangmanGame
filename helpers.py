from enum import Enum


class Color(Enum):
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'

    BOLD = '\033[1m'
    STRIKE = '\033[9m'
    UNDERLINE = '\033[4m'

    END = '\033[0m'


def paint(text: str, color: Color) -> str:
    return f"{color.value}{text}{Color.END.value}"

def clear_console():
    print("\n" * 50)