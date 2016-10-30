from pyspark import SparkContext
from pyspark.mllib.random import RandomRDDs
from math import hypot
import sys

sc = SparkContext()

# Project Euler Problem 1

print (sc.range(1000).filter(lambda candidate: candidate%3==0 or candidate%5==0).sum())

# Approximating Pi using Monte Carlo integration

radius = 1
def dist(p):
	return hypot(p[0], p[1])

num_samples = int(sys.argv[1])
unit_square = RandomRDDs.uniformVectorRDD(sc, num_samples, 2)
hit = unit_square.map(dist).filter(lambda d: d < radius).count()
fraction = hit / num_samples

print (fraction * (2*radius)**2)