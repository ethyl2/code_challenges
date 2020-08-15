import math
'''
Class Circle has a radius, diameter, area, and a __repr__().
'''


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    # Because the tests also expect this format for __str__(), no __str() needed here.
    def __repr__(self):
        return f"Circle({self.radius})"

    # Defining the radius as a property allows us to add the value check whenever the user wants to update the radius.
    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        if new_radius <= 0:
            raise ValueError("Radius cannot be negative")
        else:
            self.__radius = new_radius

    # Defining the diameter in this way updates the radius whenever the diameter is updated.
    # And updates the diameter when the radius is updated.
    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, new_diameter):
        self.radius = new_diameter / 2

    # Defining the area this way updates the area whenever the radius is updated.
    # On purpose, we don't have a @propery.setter, so that attempting to update the area will raise an AttributeError
    @property
    def area(self):
        return self.radius ** 2 * math.pi


if __name__ == "__main__":
    c = Circle()
    print(c)
    c.radius = 2
    print(c)
    print(c.diameter)
    print(c.area)
    # c.radius = -2
    print(c)
    # c.area = 10
    c.diameter = 10
    print(c)
    print(c.area)
