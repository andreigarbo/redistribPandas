from time import time
import geopandas as gpd
from shapely.geometry import Point
import random

def calcCellVal(cellV, radius, ):
    val = 0
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
                    cellV = calcCellVal(cellV, r)
                    outputSurface.append(cellV)
    return outputSurface


