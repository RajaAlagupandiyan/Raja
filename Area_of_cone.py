#Area of cone

#User input

radius=int(input("Enter the value of Radius(int value)="))
height=int(input("Enter the value of Height(int value)="))

#area forumala of cone

area_of_cone=0.33*3.14*(radius**2)*height

#output

print("The Radius Value is=",radius)
print("The Height value is=",height)
print("The area of cone is",area_of_cone)

#Formatted output 1

print(f"The Radius value is= {radius} and The Height value is= {height} and the area of cone is= {area_of_cone}")

#Formatted output 2

print("The Radius value is= {} and The Height value is= {} and the area of cone is= {}".format(radius,height,area_of_cone))
