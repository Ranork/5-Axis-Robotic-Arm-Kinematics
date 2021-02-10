import numpy
import math
from scipy import linalg
from math import cos,sin

q1 = 0
q2 = 90
q3 = 0
q4 = 0
q5 = 0

q1rad = math.radians(q1)
q2rad = math.radians(q2)
q3rad = math.radians(q3)
q4rad = math.radians(q4)
q5rad = math.radians(q5)

T1 = numpy.array([[cos(q1rad), -1 * sin(q1rad), 0, 0],
                  [sin(q1rad), cos(q1rad), 0, 0],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])

T2 = numpy.array([[cos(q2rad), 0, -sin(q2rad), 0],
                  [0, 1, 0, 0],
                  [sin(q2rad), 0, cos(q2rad), 231.5],
                  [0, 0, 0, 1]])

T3 = numpy.array([[cos(q3rad), 0, -sin(q3rad), 0],
                  [0, 1, 0, 0],
                  [sin(q3rad), 0, cos(q3rad), 221],
                  [0, 0, 0, 1]])

T4 = numpy.array([[cos(q4rad), -sin(q4rad), 0, 0],
                  [sin(q4rad), cos(q4rad), 0, 0],
                  [0, 0, 1, 129.5],
                  [0, 0, 0, 1]])

T5 = numpy.array([[1, 0, 0, 0],
                  [0, 1, 0, 0],
                  [0, 0, 1, 98],
                  [0, 0, 0, 1]])

T02 = numpy.dot(T1,T2)
T03 = numpy.dot(T02,T3)
T04 = numpy.dot(T03,T4)
T05 = numpy.dot(T04,T5)

print(T05.round(2))
