from circle import Circle
from cube import Cube
from sphere import Sphere
from square import Square

figures = []
exit = False

def create_figure():
    while exit == False:
        option = int(input(
            """
            Choose the figure you want to create:
            =========
            Figures 2D:
            1. Circle
            2. Square
            =========
            Figure 3D:
            3. Sphere
            4. Square
            =========
            5. Print Figures
            6. Back
            """
            ))
        
        if option == 1:
            radius = int(input("Write the circle's radius: "))
            circle = Circle(radius)
            print(circle.info())
            figures.append(circle)
        if option == 2:
                side = int(input("Write the square's side: "))
                square = Square(side)
                print(square.info())
                figures.append(square)
        if option == 3:
                radius = int(input("Write the sphere's radius: "))
                sphere = Sphere(radius)
                print(sphere.info())
                figures.append(sphere)
        if option == 4:
                side = int(input("Write the cube's side: "))
                cube = cube(side)
                print(cube.info())
                figures.append(cube)
        elif option == 5:
            for i in range(len(figures)):
                print(figures[i].__str__())
        elif option == 6:
            exit = True
        else:
            print("Write a correct option...")
        
create_figure()