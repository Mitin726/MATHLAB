class GeometryFactory:
    @staticmethod
    def create(figure_class, *args):
        return figure_class(*args)