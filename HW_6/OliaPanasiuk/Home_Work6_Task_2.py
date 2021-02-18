def calculate_area(name):
  # converting all characters 
  # into lower cases 
  name = name.lower() 
  # check for the conditions 
  if name == "rectangle": 
    l = int(input("Enter rectangle's length: ")) 
    b = int(input("Enter rectangle's breadth: ")) 
      
    # calculate area of rectangel 
    rect_area = l * b 
    print("The area of rectangle is {}".format(round(rect_area,2))) 
    
  elif name == "square": 
    s = int(input("Enter square's side length: ")) 
        
    # calculate area of square 
    sqt_area = s * s 
    print("The area of square is {}".format(round(sqt_area,2))) 
  
  elif name == "triangle": 
    h = int(input("Enter triangle's height length: ")) 
    b = int(input("Enter triangle's breadth length: ")) 
        
    # calculate area of triangle 
    tri_area = 0.5 * b * h 
    print("The area of triangle is {}".format(round(tri_area,2))) 
  
  elif name == "circle": 
    r = int(input("Enter circle's radius length: ")) 
    pi = 3.14
          
    # calculate area of circle 
    circ_area = pi * r * r 
    print("The area of triangle is {}".format(round(circ_area,2))) 
      
  else: 
    print("Sorry! This shape is not availabel") 
  
# driver code 
if __name__ == "__main__" : 
    
  print("Calculate Shape Area") 
  shape_name = input("Enter the name of shape whose area you want to find: ") 
    
  # function calling 
  calculate_area(shape_name)