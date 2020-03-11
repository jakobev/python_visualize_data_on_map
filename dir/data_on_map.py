import numbers
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("corona_german.csv")

g_map = plt.imread('germany.png')




BBox = ((df.longitude.min(),   df.longitude.max(),      
         df.latitude.min(), df.latitude.max()))
print(BBox)

fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(df.longitude, df.latitude, color='red', zorder=1, alpha= 1, s=40)
ax.set_title('Corona Infizierte in Deutschland')
ax.set_xlim(BBox[0],BBox[1])
ax.set_ylim(BBox[2],BBox[3])
ax.imshow(g_map, zorder=0, extent = BBox, aspect= 'equal')
plt.show()