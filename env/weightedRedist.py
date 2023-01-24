from time import time
import geopandas as gpd
from shapely.geometry import Point
import random
import numpy as np

def calcCellVal(cellV, radius, point):
    val = 0
    val = 1 - np.sqrt((point.x - cellV.x) * (point.x - cellV.x) + (point.y - cellV.y) * (point.y - cellV.y))/radius
    return val

def weightedRedist(w, s, pointData, weightingSurface, administrativeAreas):
    outputSurface = []
    n = 10
    maxV = 0
    for level in administrativeAreas:
        for admin in level:
            centroid = admin.geometry.centroid
            br = admin.geometry.bounding_box.buffer(0.01).envelope
            points = pointData[pointData.within(admin.geometry)]
            for p in points:
                for i in range(n):
                    while not p.within(admin.geometry):
                        p = Point(random.uniform(br.bounds[0],br.bounds[2], random.uniform(br.bounds[1], br.bounds[3])))
                    value = weightingSurface[p.x][p.y]
                    if value > maxV:
                        maxV = i
                point = p[maxV]
                r = (w * admin.area) / s
                for cell in point.buffer(r):
                    cellV = calcCellVal(cellV, r, point)
                    outputSurface.append(cellV)
    return outputSurface


