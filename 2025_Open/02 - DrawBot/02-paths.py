# create a new empty path
path = BezierPath()
# set the first oncurve point
path.moveTo((100, 100))
# line to from the previous point to a new point
path.lineTo((100, 900))
path.lineTo((900, 900))

# curve to a point with two given handles
path.curveTo((430, 778), (686, 100), (100, 100))

# close the path
path.closePath()

fill(0,0,0,.2)
stroke(0)
# draw the path
drawPath(path)

fill(0)
stroke(None)
s = 5
for oc in path.onCurvePoints:
    x,y = oc
    oval(x-s,y-s,s*2,s*2)
    
s = 3
for fc in path.offCurvePoints:
    x,y = fc
    oval(x-s,y-s,s*2,s*2)
    
stroke(0)
for ii, oc in enumerate(path.points):
    if oc in path.offCurvePoints and path.points[ii-1] not in path.offCurvePoints:
        s = oc
        e = path.points[ii-1]
        line(s,e)
    if oc in path.offCurvePoints and path.points[ii+1] not in path.offCurvePoints:
        s = oc
        e = path.points[ii+1]
        line(s,e)
    