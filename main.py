class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return "Too big for picture."
        picture = ""
        row = "".ljust(self.width, "*") + "\n"
        i = 0
        while i < self.height:
            picture += row
            i += 1
        return picture

    def get_amount_inside(self, shape):
        amount = self.get_area() / shape.get_area()
        return int(amount)

    def __str__(self):
        string = f"Rectangle(width={self.width}, height={self.height})"
        return string


class Square(Rectangle):
    def __init__(self, width):
        self.width = width
        self.height = self.width

    def set_side(self, width):
        self.width = width
        self.height = width

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        string = f"Square(side={self.width})"
        return string
