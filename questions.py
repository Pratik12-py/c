# n = input()

# i  = 10

# while i >= 1:
#     print(i) 
#     i = i-1
# l1 = ['1','2','3','4','5','6']
# separator = '-'
# print(separator.join(l1))
# n = input()
# a = n.split()
# a.reverse()
# print(' '.join(a))
# from turtle import *


# Doraemon with Python Turtle
# def ankle(x, y):
#     penup()
#     goto(x, y)
#     pendown()


# def eyes():
#     fillcolor("#ffffff")
#     begin_fill()

#     tracer(False)
#     a = 2.5
#     for i in range(120):
#         if 0 <= i < 30 or 60 <= i < 90:
#             a -= 0.05
#             lt(3)
#             fd(a)
#         else:
#             a += 0.05
#             lt(3)
#             fd(a)
#     tracer(True)
#     end_fill()


# def daari():
#     ankle(-32, 135)
#     seth(165)
#     fd(60)

#     ankle(-32, 125)
#     seth(180)
#     fd(60)

#     ankle(-32, 115)
#     seth(193)
#     fd(60)

#     ankle(37, 135)
#     seth(15)
#     fd(60)

#     ankle(37, 125)
#     seth(0)
#     fd(60)

#     ankle(37, 115)
#     seth(-13)
#     fd(60)


# def mukh():
#     ankle(5, 148)
#     seth(270)
#     fd(100)
#     seth(0)
#     circle(120, 50)
#     seth(230)
#     circle(-120, 100)


# def scarf():
#     fillcolor('#e70010')
#     begin_fill()
#     seth(0)
#     fd(200)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     fd(207)
#     circle(-5, 90)
#     fd(10)
#     circle(-5, 90)
#     end_fill()


# def nose():
#     ankle(-10, 158)
#     seth(315)
#     fillcolor('#e70010')
#     begin_fill()
#     circle(20)
#     end_fill()


# def black_eyes():
#     seth(0)
#     ankle(-20, 195)
#     fillcolor('#000000')
#     begin_fill()
#     circle(13)
#     end_fill()

#     pensize(6)
#     ankle(20, 205)
#     seth(75)
#     circle(-10, 150)
#     pensize(3)

#     ankle(-17, 200)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(5)
#     end_fill()
#     ankle(0, 0)


# def face():
#     fd(183)
#     lt(45)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(120, 100)
#     seth(180)
#     # print(pos())
#     fd(121)
#     pendown()
#     seth(215)
#     circle(120, 100)
#     end_fill()
#     ankle(63.56, 218.24)
#     seth(90)
#     eyes()
#     seth(180)
#     penup()
#     fd(60)
#     pendown()
#     seth(90)
#     eyes()
#     penup()
#     seth(180)
#     fd(64)


# def taauko():
#     penup()
#     circle(150, 40)
#     pendown()
#     fillcolor('#00a0de')
#     begin_fill()
#     circle(150, 280)
#     end_fill()


# def Doraemon():
#     taauko()

#     scarf()

#     face()

#     nose()

#     mukh()

#     daari()

#     ankle(0, 0)

#     seth(0)
#     penup()
#     circle(150, 50)
#     pendown()
#     seth(30)
#     fd(40)
#     seth(70)
#     circle(-30, 270)

#     fillcolor('#00a0de')
#     begin_fill()

#     seth(230)
#     fd(80)
#     seth(90)
#     circle(1000, 1)
#     seth(-89)
#     circle(-1000, 10)

#     # print(pos())

#     seth(180)
#     fd(70)
#     seth(90)
#     circle(30, 180)
#     seth(180)
#     fd(70)

#     # print(pos())
#     seth(100)
#     circle(-1000, 9)

#     seth(-86)
#     circle(1000, 2)
#     seth(230)
#     fd(40)

#     # print(pos())

#     circle(-30, 230)
#     seth(45)
#     fd(81)
#     seth(0)
#     fd(203)
#     circle(5, 90)
#     fd(10)
#     circle(5, 90)
#     fd(7)
#     seth(40)
#     circle(150, 10)
#     seth(30)
#     fd(40)
#     end_fill()

#     seth(70)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(-30)
#     end_fill()

#     ankle(103.74, -182.59)
#     seth(0)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(-15, 180)
#     fd(90)
#     circle(-15, 180)
#     fd(10)
#     end_fill()

#     ankle(-96.26, -182.59)
#     seth(180)
#     fillcolor('#ffffff')
#     begin_fill()
#     fd(15)
#     circle(15, 180)
#     fd(90)
#     circle(15, 180)
#     fd(10)
#     end_fill()

#     ankle(-133.97, -91.81)
#     seth(50)
#     fillcolor('#ffffff')
#     begin_fill()
#     circle(30)
#     end_fill()
#     # Doraemon with Python Turtle

#     ankle(-103.42, 15.09)
#     seth(0)
#     fd(38)
#     seth(230)
#     begin_fill()
#     circle(90, 260)
#     end_fill()

#     ankle(5, -40)
#     seth(0)
#     fd(70)
#     seth(-90)
#     circle(-70, 180)
#     seth(0)
#     fd(70)

#     ankle(-103.42, 15.09)
#     fd(90)
#     seth(70)
#     fillcolor('#ffd200')
#     # print(pos())
#     begin_fill()
#     circle(-20)
#     end_fill()
#     seth(170)
#     fillcolor('#ffd200')
#     begin_fill()
#     circle(-2, 180)
#     seth(10)
#     circle(-100, 22)
#     circle(-2, 180)
#     seth(180 - 10)
#     circle(100, 22)
#     end_fill()
#     goto(-13.42, 15.09)
#     seth(250)
#     circle(20, 110)
#     seth(90)
#     fd(15)
#     dot(10)
#     ankle(0, -150)

#     black_eyes()


# if __name__ == '__main__':
#     screensize(800, 600, "#f0f0f0")
#     pensize(3)
#     speed(9)
#     Doraemon()
#     ankle(100, -300)
#     mainloop()
# import PIL
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D

# # load bluemarble with PIL
# bm = PIL.Image.open('bluemarble.jpg')
# # it's big, so I'll rescale it, convert to array, and divide by 256 to get RGB values that matplotlib accept 
# bm = np.array(bm.resize([d/5 for d in bm.size]))/256.

# # coordinates of the image - don't know if this is entirely accurate, but probably close
# lons = np.linspace(-180, 180, bm.shape[1]) * np.pi/180 
# lats = np.linspace(-90, 90, bm.shape[0])[::-1] * np.pi/180 

# repeat code from one of the examples linked to in the question, except for specifying facecolors:
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# x = np.outer(np.cos(lons), np.cos(lats)).T
# y = np.outer(np.sin(lons), np.cos(lats)).T
# z = np.outer(np.ones(np.size(lons)), np.sin(lats)).T
# ax.plot_surface(x, y, z, rstride=4, cstride=4, facecolors = bm)


# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import imageio
# for i in range(0,330,20):
#     my_map = Basemap(projection='ortho', lat_0=0, lon_0=i, resolution='l', area_thresh=1000.0)
#     my_map.bluemarble()
#     my_map.etopo()
#     name=str(i)
#     path='/path/to/your/directory/'+name
#     plt.savefig(path+'.png')
#     plt.show()
#     plt.clf()
#     plt.cla()
#     plt.close()
#     images = []
# for f in range(0,330,20):
#     images.append(imageio.imread("/path/to/your/directory/"+str(f)+".png"))
#     imageio.mimsave('movie.gif', images, duration=0.5)
# import datetime,matplotlib,time
# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt
# import numpy as np
# from gifly import gif_maker

# plt.ion()
# fig,ax0 = plt.subplots(figsize=(5.3,4))
# ax0.set_position([0.0,0.0,1.0,1.0])

# lat_viewing_angle = [20,20]
# lon_viewing_angle = [-180,180]
# rotation_steps = 150
# lat_vec = np.linspace(lat_viewing_angle[0],lat_viewing_angle[0],rotation_steps)
# lon_vec = np.linspace(lon_viewing_angle[0],lon_viewing_angle[1],rotation_steps)

# m1 = Basemap(projection='ortho', 
#           lat_0=lat_vec[0], lon_0=lon_vec[0],resolution=None)

# # add axis for space background effect
# galaxy_image = plt.imread('galaxy_image.png')
# ax0.imshow(galaxy_image)
# ax0.set_axis_off()
# ax1 = fig.add_axes([0.25,0.2,0.5,0.5])

# # define map coordinates from full-scale globe
# map_coords_xy = [m1.llcrnrx,m1.llcrnry,m1.urcrnrx,m1.urcrnry]
# map_coords_geo = [m1.llcrnrlat,m1.llcrnrlon,m1.urcrnrlat,m1.urcrnrlon]

# #zoom proportion and re-plot map 
# zoom_prop = 2.0 # use 1.0 for full-scale map

# gif_indx = 0
# for pp in range(0,len(lat_vec)):

#     ax1.clear()
#     ax1.set_axis_off()
#     m = Basemap(projection='ortho',resolution='l',
#               lat_0=lat_vec[pp],lon_0=lon_vec[pp],llcrnrx=-map_coords_xy[2]/zoom_prop,
#                 llcrnry=-map_coords_xy[3]/zoom_prop,urcrnrx=map_coords_xy[2]/zoom_prop,
#                 urcrnry=map_coords_xy[3]/zoom_prop)

#     m.bluemarble(scale=0.5)
#     m.drawcoastlines()
#     plt.show()
#     plt.pause(0.01)
#     gif_maker('blue_marble_rotating_globe.gif','./png_dir_bluemarble/',gif_indx,len(lat_vec)-1,dpi=90)
#     gif_indx+=1

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,6))

# set perspective angle
lat_viewing_angle = 45.4642
lon_viewing_angle = 9.1900

# define color maps for water and land
ocean_map = (plt.get_cmap('ocean'))(210)
cmap = plt.get_cmap('gist_earth')

# call the basemap and use orthographic projection at viewing angle
m1 = Basemap(projection='ortho',
          lat_0=lat_viewing_angle,lon_0=lon_viewing_angle,resolution=None)

# define map coordinates from full-scale globe
map_coords_xy = [m1.llcrnrx,m1.llcrnry,m1.urcrnrx,m1.urcrnry]
map_coords_geo = [m1.llcrnrlat,m1.llcrnrlon,m1.urcrnrlat,m1.urcrnrlon]

#zoom proportion and re-plot map 
zoom_prop = 7.0 # use 1.0 for full-scale map

m = Basemap(projection='ortho',resolution='l',
          lat_0=lat_viewing_angle,lon_0=lon_viewing_angle,llcrnrx=-map_coords_xy[2]/zoom_prop,
            llcrnry=-map_coords_xy[3]/zoom_prop,urcrnrx=map_coords_xy[2]/zoom_prop,
            urcrnry=map_coords_xy[3]/zoom_prop)

# coastlines, map boundary, fill continents/water, fill ocean, draw countries
m.drawmapboundary(fill_color=ocean_map)
m.fillcontinents(color=cmap(200),lake_color=ocean_map)
m.drawcoastlines()
m.drawcountries()

# latitude/longitude line vectors
lat_line_range = [-90,90]
lat_lines = 8
lat_line_count = (lat_line_range[1]-lat_line_range[0])/lat_lines

merid_range = [-180,180]
merid_lines = 8
merid_count = (merid_range[1]-merid_range[0])/merid_lines

m.drawparallels(np.arange(lat_line_range[0],lat_line_range[1],lat_line_count))
m.drawmeridians(np.arange(merid_range[0],merid_range[1],merid_count))

# scatter to indicate lat/lon point
x,y = m(lon_viewing_angle,lat_viewing_angle)
m.scatter(x,y,marker='o',color='#DDDDDD',s=3000,zorder=10,alpha=0.7,\
          edgecolor='#000000')
m.scatter(x,y,marker='o',color='#000000',s=100,zorder=10,alpha=0.7,\
          edgecolor='#000000')

plt.annotate('Milan, Italy', xy=(x, y),  xycoords='data',
                xytext=(-110, -10), textcoords='offset points',
                color='k',fontsize=12,bbox=dict(facecolor='w', alpha=0.5),
                arrowprops=dict(arrowstyle="fancy", color='k'),
                zorder=20)

# save figure at 150 dpi and show it
plt.savefig('ortho_zoom_example.png',dpi=150,transparent=True)
plt.show()