from .circle import Circle
from .cube import Cube
from .sphere import Sphere
from .square import Square
from factories.geometry_factory import GeometryFactory

created_figures = []
FIGURES = {
    1: ("radius", Circle),
    2: ("side", Square),
    3: ("radius", Sphere),
    4: ("side", Cube)
}

def display_options() -> int:
    while True:
        try: 
            option = int(input(
                """
                Choose the figure you want to create:
                ================
                1. Circle
                2. Square
                3. Sphere
                4. Cube
                ================
                5. Print Figures
                6. Exit
                ================
                """
                ))
            return option
        except ValueError:
            print("Write a valid integer.")
        
def run_geometry_module():
    running = True
    while running:
        option = display_options()
        if option == 5:
            for figure in created_figures:
                print(figure)
            continue
        elif option == 6:
            print("bye bye...")
            break
        elif option not in FIGURES:
            print("Write a Valid Option")
            continue
        label, figure_option = FIGURES[option]
        value = float(input(f"Write the {label}: "))
        figure = GeometryFactory.create(figure_option, value)
        print(figure.info())
        created_figures.append(figure)