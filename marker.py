import mne

mne.set_log_level('error')

import numpy as np
import matplotlib.pyplot as plt
import glob

raw = mne.io.read_raw_brainvision(
    r'D:\ЗАГРУЗКИ\BrainProducts\BrainProducts\ERP\Exp_AO_5013201_1_1_tfix32\Exp_AO_5013201_1_1_tfix32.vhdr',
    preload=True)
print(len(raw.info['ch_names']))
print(raw._data.shape)
raw.plot(n_channels=10, start=138, duration=2)
print(mne.events_from_annotations(raw)[0])
print(mne.events_from_annotations(raw)[1])
