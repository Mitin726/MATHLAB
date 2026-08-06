from .circle import Circle
from .cube import Cube
from .sphere import Sphere
from .square import Square
from .figure2D import Figure2D
from .figure3D import Figure3D
from factories.geometry_factory import GeometryFactory

class GeometryModule():
    
    FIGURES = {
            1: ("radius", Circle),
            2: ("side", Square),
            3: ("radius", Sphere),
            4: ("side", Cube)
        }
    
    def __init__(self):
        self.created_figures = []

    def display_options(self) -> int:
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
            
    def run(self):
        running = True
        while running:
            option = self.display_options()
            if option == 5:
                for figure in self.created_figures:
                    print(figure)
                continue
            elif option == 6:
                print("bye bye...")
                break
            elif option not in self.FIGURES:
                print("Write a Valid Option")
                continue
            label, figure_option = self.FIGURES[option]
            value = float(input(f"Write the {label}: "))
            figure = GeometryFactory.create(figure_option, value)
            print(figure.info())
            self.created_figures.append(figure)