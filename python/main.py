import cv2
import matplotlib.pyplot as plt
import numpy as np

row_iter = 2
col_iter = 2

if __name__ == "__main__":
    img = cv2.imread('./mapa_calor1.png', 0)
    plt.imshow(img, cmap='gray')
    height, width = img.shape
    map_created = []
    mesh = []
    for height_iter in range(0, height, col_iter):
        row_created = []
        for width_iter in range(0, width, row_iter):
            data = img[height_iter:height_iter+col_iter, width_iter:width_iter+row_iter]
            sum_data = 0.0
            for val_i in data:
                for val_j in val_i:
                    sum_data += val_j
            row_created.append([height_iter, width_iter, (sum_data / (row_iter*col_iter))])
            pass
        map_created.append(row_created)
        pass
    pass

    for i in range(len(map_created)-1):
        for j in range(len(map_created[i])-1):
            x = np.array(map_created[i][j])
            y = np.array(map_created[i][j+1])
            z = np.array(map_created[i+1][j+1])
            p1 = y - x
            p2 = z - x
            c_prod = np.cross(p1, p2)

            x = np.append(x, c_prod)
            y = np.append(y, c_prod)
            z = np.append(z, c_prod)
            mesh.append(x)
            mesh.append(y)
            mesh.append(z)

            x = np.array(map_created[i][j])
            y = np.array(map_created[i+1][j+1])
            z = np.array(map_created[i+1][j])
            p1 = y - x
            p2 = z - x
            c_prod = np.cross(p1, p2)

            x = np.append(x, c_prod)
            y = np.append(y, c_prod)
            z = np.append(z, c_prod)
            mesh.append(x)
            mesh.append(y)
            mesh.append(z)

    fopen = open("./points.csv", 'w')
    for i in range(len(map_created)):
        for j in range(len(map_created[i])):
            fopen.write(str((i+1)/4) + ", " + str((j+1)/4) + ", " + str(map_created[i][j][2]/255*30) + "\n")

    fopen = open("C:/Users/LAPTOP1/Documents/GitHub/CG-Rasterizacion/resources/models/mesh.csv", 'w')
    for i in range(len(mesh)):
        fopen.write(str(mesh[i][0]/4) + ", " + str(30-(mesh[i][2]/255*40)) + ", " + str(mesh[i][1]/4) + ", " +
                    str(mesh[i][3]) + ", " + str(mesh[i][5]) + ", " + str(mesh[i][4]) + "\n")

    print(len(map_created))
    print(len(map_created[1]))
