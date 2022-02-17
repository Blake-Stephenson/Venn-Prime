import turtle
from diagram import DData as Diag


class DVenn:
    size = 0

    def __init__(self, d: Diag):
        self.size = len(d.getLabels())
        if self.size == 2:
            self.venn = Venn2(d)
        elif self.size == 3:
            self.venn = Venn3(d)

    def show(self):
        self.venn.printDiag()


class Venn2:
    boxes = [[]]
    labels = []
    data = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()
        self.t = d.getT()

    def printDiag(self):
        lens = [len(i) for i in self.boxes]
        x = max(lens)
        r = 40 + 3 * x
        hx = -r / 2
        hy = -r / 2

        t = self.t
        t.penup()
        t.goto(hx, hy)
        t.pendown()
        t.color('black')
        t.speed(20)
        t.circle(r)
        t.color('blue')
        t.penup()
        t.forward(r)
        t.pendown()
        t.circle(r)
        t.penup()
        self.printTextLeft(r, (hx, hy))
        self.printTextRight(r, (hx, hy))
        self.printTextMid(r, (hx, hy))
        self.printOther(r, (hx, hy))

    def printTextLeft(self, r: int, home: (int, int)):
        nums = self.boxes[0][:]
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        turtle.TurtleScreen._RUNNING = True
        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0], home[1] + 2 * r + 5)
        t.write(self.labels[0])
        # Print nums
        t.goto(home[0] - r / 3, home[1] + r + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printTextRight(self, r: int, home: (int, int)):
        nums = self.boxes[1][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r, home[1] + 2 * r + 5)
        t.write(self.labels[1])
        # Print nums
        t.goto(home[0] + r * 5 / 4, home[1] + r + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printTextMid(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                if i == j:
                    nums.append(i)
        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r / 2 - 5, home[1] + r + (5 * (len(nums)-1)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printOther(self, r: int, home: (int, int)):
        nums = self.data[:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        t = self.t
        t.right(90)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(home[0], home[1] - 20)
        t.write("Other: %s" % nums)


class Venn3:
    boxes = [[]]
    labels = []
    data = []

    def __init__(self, d: Diag):
        self.boxes = d.getBoxes()
        self.labels = d.getLabels()
        self.data = d.getData()
        self.t = d.getT()

    def printDiag(self):
        lens = [len(i) for i in self.boxes]
        x = max(lens)
        r = 40 + 4 * x
        hx = -r / 2
        hy = -r / 2

        t = self.t
        t.penup()
        t.goto(hx, hy)
        t.pendown()
        t.color('black')
        t.speed(20)
        t.circle(r)
        t.color('blue')
        t.penup()
        t.forward(r)
        t.pendown()
        t.circle(r)
        t.penup()
        t.back(r / 2)
        t.left(90)
        t.back(0.87 * r)
        t.right(90)
        t.pendown()
        t.circle(r)
        t.penup()
        self.printA(r, (hx, hy))
        self.printB(r, (hx, hy))
        self.printC(r, (hx, hy))
        self.printAB(r, (hx, hy))
        self.printAC(r, (hx, hy))
        self.printBC(r, (hx, hy))
        self.printABC(r, (hx, hy))
        self.printOther(r, (hx, hy))

    def printA(self, r: int, home: (int, int)):
        nums = self.boxes[0][:]
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0], home[1] + 2 * r + 5)
        t.write(self.labels[0])
        # Print nums
        t.goto(home[0] - r / 3, home[1] + r * 1.2 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printB(self, r: int, home: (int, int)):
        nums = self.boxes[1][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r, home[1] + 2 * r + 5)
        t.write(self.labels[1])
        # Print nums
        t.goto(home[0] + r * 4 / 3, home[1] + r * 1.2 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printC(self, r: int, home: (int, int)):
        nums = self.boxes[2][:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print label
        t.goto(home[0] + r / 2, home[1] - r - 10)
        t.write(self.labels[2])
        # Print nums
        t.goto(home[0] + r / 2, home[1] - r * 0.6 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAB(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r / 2, home[1] + r * 1.38 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printAC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        t.speed(10)
        # Print nums
        t.goto(home[0] - r / 5, home[1] + r * 0.25 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printBC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[1]:
            for j in self.boxes[2]:
                if i == j:
                    nums.append(i)
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r * 1.05, home[1] + r * 0.25 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printABC(self, r: int, home: (int, int)):
        nums = []
        for i in self.boxes[0]:
            for j in self.boxes[1]:
                for k in self.boxes[2]:
                    if i == j and i == k:
                        nums.append(i)

        t = self.t
        t.setheading(270)
        t.penup()
        # Print nums
        t.goto(home[0] + r / 2 - 5, home[1] + r * 0.5 + (5 * len(nums)))
        for i in nums:
            t.write(i)
            t.fd(10)

    def printOther(self, r: int, home: (int, int)):
        nums = self.data[:]
        for i in self.boxes[0]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[1]:
            if i in nums:
                nums.remove(i)
        for i in self.boxes[2]:
            if i in nums:
                nums.remove(i)
        t = self.t
        t.right(90)
        t.penup()
        # Print nums
        t.goto(home[0], home[1] - r - 30)
        t.write("Other: %s" % nums)