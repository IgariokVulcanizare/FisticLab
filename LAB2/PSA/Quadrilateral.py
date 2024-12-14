import math
import random

def generating_points():
    angle = random.random() * 2 * math.pi
    x = math.cos(angle)
    y = math.sin(angle)#because radius is 1
    return [x,y,angle]

def angle_between_points(p1,p2,p3):
    vec_1 = [p1[0]-p2[0],p1[1]-p2[1]]
    vec_2 = [p3[0]-p2[0],p3[1]-p2[1]]

    magnitude_vec_1 = math.sqrt(vec_1[0]**2+vec_1[1]**2)
    magnitude_vec_2 = math.sqrt(vec_2[0] ** 2 + vec_2[1] ** 2)
    dot_product = vec_1[0]*vec_2[0] + vec_1[1]*vec_2[1]

    angle_between = dot_product/(magnitude_vec_1*magnitude_vec_2)

    return math.acos(angle_between)

win = 0
nr_exp = 100000
for i in range(nr_exp):
    quadrilateral = []
    for i in range(4):
        quadrilateral.append(generating_points())

    points_sorted = sorted(quadrilateral, key=lambda p: p[2])
    convex_quadrilateral = []
    for p in points_sorted:
        convex_quadrilateral.append(p[:2])
    perm_1 = convex_quadrilateral[:-1]
    perm_2 = (convex_quadrilateral[1:]+convex_quadrilateral[:1])[:-1]
    perm_3 = (convex_quadrilateral[2:] + convex_quadrilateral[:2])[:-1]
    perm_4 = (convex_quadrilateral[3:] + convex_quadrilateral[:3])[:-1]

    angle_1 = angle_between_points(perm_1[0], perm_1[1], perm_1[2])
    angle_2 = angle_between_points(perm_2[0], perm_2[1], perm_2[2])
    angle_3 = angle_between_points(perm_3[0], perm_3[1], perm_3[2])
    angle_4 = angle_between_points(perm_4[0], perm_4[1], perm_4[2])

    k = 2*math.pi/3
    if angle_1 < k and angle_2 < k and angle_3 < k and angle_4 < k:
        win += 1
print(win/nr_exp)