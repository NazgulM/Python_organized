class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):

        try:
            for side in self.sides:
                if side > 0:
                    sorted_sides = list(sorted(self.sides))
                    if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                        return 'Woohoo, we can create a triangle'
                    return 'Unfortunately, we cannot create a triangle'
                elif side < 0:
                    return 'With negative numbers nothing can create'
        except Exception:
            return "You should enter only numbers"


triangle1 = TriangleChecker([2, 3, 4])
triangle1.is_triangle()
print(triangle1.is_triangle())

triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())

triangle3 = TriangleChecker([77, 3, 'Side 3'])
print(triangle3.is_triangle())

triangle4 = TriangleChecker([-77, 3, 4])
print(triangle4.is_triangle())
