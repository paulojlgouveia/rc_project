
#from time import *

import time
import math
import pylab

import networkx as nx
from matplotlib.pyplot import pause

draw = 1

def circular_pos(n, N):
	r = 10000
	alpha = (2 * math.pi) / N
	return (r * math.cos(alpha * n), r * math.sin(alpha * n))

def draw_setup():
	pylab.ion()

def draw_set(mode):
	global draw
	draw = mode

def draw_set_pos(G, u, N):
	if draw:
		r = 100
		alpha = (2 * math.pi) / N
		G.node[u]["Position"] = (r * math.cos(alpha * u), r * math.sin(alpha * u))

def draw_update(G):
	if draw:
		nx.draw(G, pos=nx.get_node_attributes(G,'Position'))
		pause(0.001)

def draw_clear():
	if draw:
		pylab.clf()

def draw_wait(t):
	if draw:
		pause(t)
	
def draw_close():
	if draw:
		pylab.close()
	
	