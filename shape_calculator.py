# Scientific Computing with Python
# Polygon Area Calculator
# shape_calculator.py
class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        areaInt = self.width * self.height
        return areaInt

    def get_perimeter(self):
        perimeterLength = 2 * self.width + 2 * self.height
        return perimeterLength

    def get_picture(self):
        strShape = "Rectangle "
        areaInt = self.width * self.height
        if (self.width == self.height):
            strShape = "Square "
            areaStr = strShape + "(side=" + str(self.width) + ")"
        else:
            areaStr = strShape + "(width=" + str(self.width) + ", height=" + str(self.height) + ")"
        if ((self.width * self.height) > 50):
            print("Too big for picture.")
            pass
        else:
            printLine = ""
            for i in range(self.height):
                for j in range(self.width):
                    printLine = printLine + "*"
                printLine = printLine + "\n"

            return(areaStr + "\n" + printLine)

    def get_diagonal(self):
        intDiagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return intDiagonal

    def get_amount_inside(self, sq):
        insideAmt = self.width * self.height / sq.width ** 2
        return insideAmt

class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side
        self.side = side
        Rectangle.__init__(self, side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

    def get_diagonal(self):
        intDiagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return intDiagonal

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def main():
    rect = Rectangle(width=10, height=5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

if __name__ == "__main__":
    main()
