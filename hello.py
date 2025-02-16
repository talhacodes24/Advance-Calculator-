class Vector:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __add__(self, other):
        return Vector(self.X + other.X, self.Y + other.Y)

    def __truediv__(self, other):
        return Vector(self.X / other.X, self.Y / other.Y)

    def __sub__(self, other):
        return Vector(self.X - other.X, self.Y - other.Y)

    def __mul__(self, other):
        return Vector(self.X * other.X, self.Y * other.Y)

    def __repr__(self):
        return f"X: {self.X}, Y: {self.Y}"


# Prompting user for input
x1, y1 = map(int, input("Enter coordinates for the first vector (X Y): ").split())
x2, y2 = map(int, input("Enter coordinates for the second vector (X Y): ").split())

v1 = Vector(x1, y1)
v2 = Vector(x2, y2)

# Perform operations
v_add = v1 + v2
v_sub = v1 - v2
v_mul = v1 * v2
v_div = v1 / v2

# Print results
print(f"Addition: {v_add}")
print(f"Subtraction: {v_sub}")
print(f"Multiplication: {v_mul}")
print(f"Division: {v_div}")