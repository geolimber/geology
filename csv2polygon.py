#!/usr/bin/python
# -*- coding: UTF-8 -*-
# This script converts set of vertices of the mining concession (UTM coordinates) to polygon in *.wkt format (Well Known Text).
import sys


def savePolygon(filename, polygon):
    lineWkt = "1;POLYGON((" + ','.join(polygon) + "))\n"
    newFile = filename[0:-4] + ".wkt"
    outFile = open(newFile, 'w')
    outFile.write("id;wkt\n" + lineWkt)
    print('Conversion completed. File {} was created successfully.'.format(newFile))


def makePolygon(filename):
    try:
        with open(filename) as file:
            csv = file.readlines()
    except Exception as e:
        print(e)
    polygon = []
    for line in csv:
        line = line.rstrip('\n;,\t')
        if line[0].isdigit():
            polygon.append(line.replace(';', ' '))
    polygon.append(polygon[0])
    savePolygon(filename, polygon)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        makePolygon(sys.argv[1])
