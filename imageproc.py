from PIL import Image
import matplotlib.pyplot as plt

tempo = plt.imread('Professional Picture 1.jpeg')
hei = len(tempo)
wid = len(tempo[0])

RGB = [[], [], []]

for i in range(hei):
    for j in range(wid):
        if ((hei - 1 > i > 1) and (wid - 1 > j > 1)):
            temp = abs((tempo[i][j][0] - tempo[i + 1][j][0]))
            mean = abs((tempo[i][j][0] + tempo[i + 1][j][0])) / 2
            temp1 = abs((tempo[i][j][1] - tempo[i + 1][j][1]))
            mean1 = abs((tempo[i][j][1] + tempo[i + 1][j][1])) / 2
            temp2 = abs((tempo[i][j][2] - tempo[i + 1][j][2]))
            mean2 = abs((tempo[i][j][2] + tempo[i + 1][j][2])) / 2
            if ((temp > 3 * mean) and (temp1 > 3 * mean1) and (temp2 > 3 * mean2)):
                RGB[i][j][0] = 0
                RGB[i][j][1] = 0
                RGB[i][j][2] = 0
            else:
                RGB = tempo

img1 = Image.fromarray(RGB, 'RGB')
img1.save('my3.jpeg')
img2 = Image.open('my3.jpeg')
img2.convert(mode='L').save('my3_bw.jpeg')
img2.show()