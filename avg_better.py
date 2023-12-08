from numpy import average

def better_than_average(class_points, your_points):
    return your_points > average(class_points)

points_list = [100, 40, 34, 57, 29, 72, 57, 88]
my_points = 75
print(better_than_average(points_list, my_points))