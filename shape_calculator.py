# **** --- CREATED BY --- ****
# ->->  Dr. Hafeez Anwar  <-<-
#  -> Date: July 04, 2022  <-
# ****************************
# This code implements problem 4 of the course. The sentences from the problem statements are written on top of python statements to show that they are implemented as per the requirements. 
# 
class Rectangle:
  # it should be initialized with width and height attributes
  def __init__(self,w,h):
    self.width = w
    self.height = h
  # The width function
  def set_width(self,w):
    self.width = w
  # The set_height function
  def set_height(self, h):
    self.height = h
  # Returns area (width * height)
  def get_area(self):
    return self.width * self.height
  # Returns perimeter (2 * width + 2 * height)
  def get_perimeter(self):
    return 2*self.width + 2*self.height
  # Returns diagonal ((width ** 2 + height ** 2) ** .5)
  def get_diagonal(self):
    return ((self.width ** 2 + self.height ** 2) ** .5)
  #Returns a string that represents the shape using lines of "*".
  def get_picture(self):
    # If the width or height is larger than 50, this should
    # return the string: "Too big for picture."
    if self.width>50 or self.height>50:
        return "Too big for picture."
    else:
        shape_str = ''
        # The number of lines should be equal to the height and the number
        # of "*" in each line should be equal to the width.
        for i in range(self.height):
          shape_str = shape_str+'*'*self.width + '\n'

    return shape_str
  # Additionally, if an instance of a Rectangle is represented as a string, it should      look like: Rectangle(width=5, height=10)
  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
    
  # Takes another shape (square or rectangle) as an argument. 
  def get_amount_inside(self,shape):
    # The width and height of the shape to be accomodated
    inside_shape_width = shape.width
    inside_shape_height = shape.height
    # The area of the shape to be accomodated
    inside_shape_area = shape.get_area()
    # The width and height of the main shape
    outside_shape_width = self.width
    outside_shape_height = self.height

    # If the shape could not be accomodated by the main shape, just return 0
    if self.get_area()< inside_shape_area:
      return 0
    else:
      # Ratio of the columns of the main shape and the shape to be accomodated
      num_cols = int(outside_shape_width/inside_shape_width)
      # Ratio of the rows of the main shape and the shape to be accomodated
      num_rows = int(outside_shape_height/inside_shape_height)
      # If none of the ratios are zeros, means that main shape could accomodated            the passed in shape
      if num_cols!=0 and num_rows!=0:
      # Returns the number of times the passed in shape could fit inside the shape        # (with no rotations)
        return num_rows*num_cols
    
# The Square class should be a subclass of Rectangle and inherit methods and attributes.
class Square(Rectangle):
  # When a Square object is created, a single side length is passed in
  def __init__(self,x):
  #The __init__ method should store the side length in both the width
  # and height attributes from the Rectangle class.
    self.width = self.height = x
  # The Square class should be able to access the Rectangle class methods
  # but should also contain a set_side method
  def set_side(self,s):
    self.width = self.height = s
  # If an instance of a Square is represented as a string, it should look
  # like: Square(side=9)
  def __str__(self):
  # Additionally, if an instance of a Rectangle is represented as a string, 
  # it should look like: Rectangle(width=5, height=10)
    return f'Square(side={self.width})'
  
  # Override, the function set_width
  def set_width(self,w):
    self.width = self.height = w
  
   # Override, the function set_height
  def set_height(self,h):
    self.height = self.width = h
