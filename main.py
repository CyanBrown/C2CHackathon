import sys
from rich import *
from rich.table import Table
from rich.console import Console
from formulas import *
import inspect




def main():

    classes = [CircleSphere, SquareRect, CubeRect, Trapezoid, Cone, Cylinder, NthPolygon]

    ex = False

    while not ex:
        selection_table = Table(title="Select which calculator you would like to use")

        selection_table.add_column("Index", justify="right", style="Red", no_wrap=True)
        selection_table.add_column("Calculator", justify="right", style="cyan", no_wrap=True)

        selection_table.add_row("1", "Circle/Sphere")
        selection_table.add_row("2", "Square/Rectangle")
        selection_table.add_row("3", "Cube/Rectangular Prism")
        selection_table.add_row("4", "Trapezoid")
        selection_table.add_row("5", "Cone")
        selection_table.add_row("6", "Cylinder")
        selection_table.add_row("7", "Polygon (n sides)")
        # selection_table.add_row("8", "Triangle")
        # selection_table.add_row("9", "Sine")
        # selection_table.add_row("10", "Cosine")
        # selection_table.add_row("11", "Tangent")
        # selection_table.add_row("12", "Arcsin")
        # selection_table.add_row("13", "Arccos")
        # selection_table.add_row("14", "Arctan")

        console = Console()
        console.print(selection_table)

        while True:
            try:
                index = int(input("Type the number of which calculator you want: "))-1
                choice = classes[index]
                break
            except:
                print("That is not a valid input, please try again")

        params = inspect.signature(choice.__init__)
        params = list(str(params).replace(")","").split(", "))[1:]

        ps = []

        for i in params:
            try:
                ps.append(float(input(f"What are the {i}: ")))
            except:
                print("Invalid Input")
                continue

        obj = choice(*ps)

        print(obj)

        t = input("Type 'return' to go back to the home page and anything else to quit: ")
        if t!='return':
            quit(0)

if __name__ == '__main__':
    main()