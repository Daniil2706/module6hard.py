class Figure:
    def __init__(self, color, *sides):
        self.__sides = list(1 for _ in range(self.sides_count))
        self.filled = False
        self.__color = color
    if self.__is_valid_sides(*sides):
            self.set_sides(*sides)
    
    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.__sides[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * (self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        semi_perimeter = sum(self.__sides) / 2
        return (semi_perimeter * (semi_perimeter - self.__sides[0]) * (semi_perimeter - self.__sides[1]) * (semi_perimeter - self.__sides[2])) ** 0.5

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color, *[side_length] * self.sides_count)

    def get_volume(self):
        return self.__sides[0] ** 3

