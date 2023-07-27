import mne
import matplotlib.pyplot as plt
import csv
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import numpy as np
from Poly5_Reader import Poly5Reader, Channel
from numpy import genfromtxt
import matplotlib.backends.backend_qt5agg


def define_func(path=None):
    if path == None:
        root = tk.Tk()
        path = filedialog.askopenfilename()
        root.withdraw()

    if path.endswith('.edf'):
        raw = mne.io.read_raw_edf(path, preload=True)
        return raw
    elif path.endswith('.vhdr'):
        raw = mne.io.read_raw_brainvision(path, preload=True)
        return raw
    elif path.endswith('.csv'):
        my_data = genfromtxt(path, delimiter=',')
        data = pd.read_csv(path)
        ch_names = ['CH 1', 'CH 2', 'CH 3', 'CH 4', 'CH 5', 'CH 6', 'CH 7', 'CH 8', 'CH 9']
        sfreq = 2048
        info = mne.create_info(ch_names=ch_names, sfreq=sfreq)
        raw = mne.io.RawArray(my_data, info)
        # raw = pd.read_csv(path)
        return raw
    elif path.endswith('.Poly5'):
        data = Poly5Reader(path)
        ch_names = ['CH 1', 'CH 2', 'CH 3', 'CH 4', 'CH 5', 'CH 6', 'CH 7', 'CH 8', 'CH 9', 'CH 10', 'CH 11', 'CH 12',
                    'CH 13', 'CH 14', 'CH 15', 'CH 16', 'CH 17', 'CH 18']
        info = mne.create_info(data.num_channels, sfreq=data.sample_rate)
        raw = mne.io.RawArray(data.samples, info)
        raw_2 = data.samples
        return raw_2
    else:
        print("Unnown type of file")


if __name__ == '__main__':
    # plt.show(define_func())
    # plt.ion()
    # define_func().plot(n_channels=5)
    # define_func().plot_psd(fmin=1,fmax=45,tmax=60,average=False)

    # print(define_func().plot(n_channels=1,start=563,duration=0.5))
    # define_func().set_montage('standard_1005')
    # print(define_func().info['dig'])
    # raw = define_func()
    # print(define_func().plot())
    # ch = ['CH 1', 'CH 2', 'CH 3', 'CH 4', 'CH 5', 'CH 6', 'CH 7', 'CH 8', 'CH 9']

    # raw = define_func()

    # raw_stim = raw.pick_channels(raw.ch_names)
    # # raw_stim._data = clean_stim(raw_stim._data)
    # print(raw_stim)
    #
    # # define_func().add_channels([raw_stim])
    # # events = mne.find_events(define_func())
    # define_func().plot(n_channels=1,start=5,duration=2)
    w = define_func()
