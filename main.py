import sys
from rich import *
from rich.table import Table
from rich.console import Console



def gui():
    index = 0

    selection_table = Table(title="Select which calculator you would like to use")

    selection_table.add_column("Index", justify="right", style="Red", no_wrap=True)
    selection_table.add_column("Calculator", justify="right", style="cyan", no_wrap=True)

    selection_table.add_row("1", "Sphere")
    selection_table.add_row("2", "Square/Rectangle")
    selection_table.add_row("3", "Cube")
    selection_table.add_row("4", "Trapezoid")
    selection_table.add_row("5", "Cone")
    selection_table.add_row("6", "Cylinder")
    selection_table.add_row("7", "Polygon (n sides)")
    selection_table.add_row("8", "Triangle")
    selection_table.add_row("9", "Sine")
    selection_table.add_row("10", "Cosine")
    selection_table.add_row("11", "Tangent")
    selection_table.add_row("12", "Arcsin")
    selection_table.add_row("13", "Arccos")
    selection_table.add_row("14", "Arctan")

    console = Console()
    console.print(selection_table)

    index = input("Type the index of which calculator you want: ")


def main():
    
    gui()

    while not exit:
        # in here put the main code that will repeat as long as the user wants
        ...
        """
        return and closing logic statements
        
        if user_input = "return":
            continue
        
        elif user_input = "exit":
            exit = True
        
        """

    """
    maybe add final goodbye
    """

if __name__ == '__main__':
    main()