import numpy as np
Vector_A = ([1,0,0])
Vector_B = ([0,1,0])
Vector_C = ([0,0,1])
AB = np.cross(Vector_A , Vector_B)
Area = np.dot(Vector_C , AB)
print(Area)