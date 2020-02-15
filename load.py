import sys
import scipy.io as sio
from scipy import signal
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

mat_fname = "EEG.mat"
mat_dict = sio.loadmat(mat_fname)

EEGstruct = mat_dict['EEG']
label = EEGstruct['label']
time = EEGstruct['time']
trial = EEGstruct['trial']

cfg = EEGstruct['cfg']
ntrial = cfg.item()['ntrial'][0][0].item()
nelec = cfg.item()['nelec'][0][0].item()
timerange = cfg.item()['timerange'][0].item()
fs = cfg.item()['fsample'][0][0].item()
ts = 1.0/fs
