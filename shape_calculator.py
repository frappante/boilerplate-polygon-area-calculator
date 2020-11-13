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

    perimeter = 2* (self.width + self.height)
    return perimeter


  def get_diagonal(self):
    
    diagonal = (self.width ** 2 + self.height ** 2) ** 0.5
    return diagonal


  def __str__(self):

    output = f"Rectangle(width={self.width}, height={self.height})"
    return output    


  def get_picture(self):

    picture = ""
    if self.width > 50 or self.height > 50:
      return ("Too big for picture.")
    else:
      for i in range(self.height):
        picture += "*" * self.width
        picture += "\n"

    return picture             


  def get_amount_inside(self, shape):

    a = 0
    b = 0
    n = 0
    w = shape.width
    h = shape.height
    a = int(self.width / w)
    b = int(self.height / h)
    if a >= 1 and b >= 1:
      n = a * b
    else:    
      n = 0
    return n  


class Square(Rectangle):

  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, side):
    self.width = side
    self.height = side

  def set_height(self, side):    
    self.width = side
    self.height = side 

  def __str__(self):

    output = f"Square(side={self.width})"
    return output

