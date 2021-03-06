# utils
import numpy as np
import random

import math
from data_structure import *
import matplotlib.pyplot as plot

def init_board_gauss(N, K):
    n = float(N) / K
    X = list()
    for index in range(K):
        mu    = (random.uniform(-1, 1), random.uniform(-1, 1))
        sigma = random.uniform(0.05, 0.5)
        x = list()
        while len(x) < n:
            a, b = np.array([ np.random.normal(mu[0], sigma), np.random.normal(mu[1], sigma) ])
            if abs(a) < 1 and abs(b) < 1:
                x.append([a, b])
        X.extend(x)
    X = np.array(X)[:N]
    return X

def init_board_half_moon(N, radius = 6, offset = 1):
    n_samples_out = N // 2
    n_samples_in  = N - n_samples_out
    outer_circ_x  = np.cos(np.linspace(0, np.pi, n_samples_out)) + np.random.normal(0, 0.1, n_samples_out)
    outer_circ_y  = np.sin(np.linspace(0, np.pi, n_samples_out)) + np.random.normal(0, 0.1, n_samples_out)
    inner_circ_x  = 1 - np.cos(np.linspace(0, np.pi, n_samples_in))  + np.random.normal(0, 0.1, n_samples_out)
    inner_circ_y  = offset / 2 - np.sin(np.linspace(0, np.pi, n_samples_in)) + np.random.normal(0, 0.1, n_samples_out)

    return np.array( zip(radius * outer_circ_x, radius * outer_circ_y) + zip(radius * inner_circ_x, radius * inner_circ_y) )

def visualize(clusters, msg = None):
    colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]
    for cluster_id, cluster in enumerate(clusters):
        x = [ point.x for point in cluster.points ]
        y = [ point.y for point in cluster.points ]
        plot.scatter(x, y, c=colors[cluster_id], label="Cluster %d" % (cluster_id))
    if msg:
        plot.title(msg)
    plot.legend()
    plot.show()
