"""Create a Python function to multiply all the numbers in the list."""def multiplyList(myList):        result = 1        for x in myList:            result = result * x        return result     list1 = [1, 2, 3]list2 = [3, 2, 4]print(multiplyList(list1))print(multiplyList(list2))""" Create a Python code to calculate the area of a trapezoidNote : A trapezoid is a quadrilateral with two sides parallel. The trapezoid is equivalent to the British definition of the trapezium. An isosceles trapezoid is a trapezoid in which the base angles are equal so."""# Test Data:# Height : 5# Base, first value : 5# Base, second value : 6# Expected Output: Area is : 27.5# write your code bellowaBase = int(input( "Enter A: "))bBase = int(input( "Enter B: "))Height = int(input( "Enter Height: "))print( (aBase + bBase) / 2 * Height)input( "Program End")"""Create a Python software to calculate surface volume and area of a cylinder.Note: A cylinder is one of the most basic curvilinear geometric shapes, the surface formed by the points at a fixed distance from a given straight line, the axis of the cylinder."""# Test Data:# volume : Height (4), Radius(6)# Expected Output:# Volume is : 452.57142857142856# Surface Area is : 377.1428571428571# write your code bellow class Cylinder:        def __init__(self,height=1,radius=1):        self.height = height        self.radius = radius            def volume(self):        return 3.14 * self.radius**2 * self.height        def surface_area(self):        return (2 * 3.14 * self.radius * self.height) + (2 * 3.14 * self.radius**2)     pi=3.142r=float (input("enter value of r ="))h=float (input("enter value of h ="))sa=pi*r*r*(r+h)print(sa) def volumeFormula(radius, height):  # enter radius and height and return them    PI =3.14  Volume = PI * radius**2 * height  return Volumeheight = int(input("Height = "))radius = int(input("Radius = "))if height < 0 or radius < 0:  print("Please input vaild number")else:  volume_print = volumeFormula(radius, height)  print("The volume of cylinder is :" + str(volume_print) +"cm^3")input()