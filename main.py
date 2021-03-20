import sys
from rich import *
from rich.table import Table
from rich.console import Console
from formulas import *
import inspect
from trigFuncs import *
import os



def main():

    classes = [CircleSphere, SquareRect, CubeRect, Trapezoid, Cone, Cylinder, NthPolygon, sin, cos, tan, arcsin, arccos, arctan]

    ex = False

    while not ex:

        selection_table = Table(title="\nSelect which calculator you would like to use")

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
        selection_table.add_row("8", "Sine")
        selection_table.add_row("9", "Cosine")
        selection_table.add_row("10", "Tangent")
        selection_table.add_row("11", "Arcsin")
        selection_table.add_row("12", "Arccos")
        selection_table.add_row("13", "Arctan")

        console = Console()
        console.print(selection_table)

        while True:
            try:
                index = int(input("Type the number of which calculator you want: "))-1
                choice = classes[index]
                break
            except:
                print("That is not a valid input, please try again")

        params = inspect.signature(choice)
        params = list(str(params).replace(")","").replace("(","").split(", "))
        

        ps = []

        inval = False

        for i in params:
            try:
                if choice in classes[7:] and i == "measure":
                    ps.append(input("What is the measure type, degrees, or radians (deg, rad): "))

                    if "deg" not in ps and "rad" not in ps:
                      print("Invalid Input")
                      inval = True
                      break
                else:
                    ps.append(float(input(f"What is the {i}: ")))
            except:
                print("Invalid Input")
                inval = True
                break

        if inval:
          continue

        try:
          obj = choice(*ps)

          print("\n"+str(obj)+"\n")
        except:
          print("Your inputs could not be calculated.")

        t = input("Type 'return' to go back to the home page and anything else to quit: ")
        if t!='return':
            quit(0)

        os.system("clear")

if __name__ == '__main__':
    main()