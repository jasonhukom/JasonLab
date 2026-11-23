# Make Pastcraft Coordinates formatter

line = "=" * 64
location_name = []
coordinates_x = []
coordinates_y = []
coordinates_z = []

loop_time = int(input("How many coordinates? "))
for i in range(loop_time):
    location_name_variable = input("Location name: ")
    x = input("X: ")
    y = input("Y: ")
    z = input("Z: ")
    location_name.append(location_name_variable)
    coordinates_x.append(x)
    coordinates_y.append(y)
    coordinates_z.append(z)

for j in range(loop_time):
    print(f"""## {line}
# {location_name[j]}
### ```{coordinates_x[j]} {coordinates_y[j]} {coordinates_z[j]}```""")