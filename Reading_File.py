import mne
import numpy as np
import pandas as pd


class FileReader:
    def __init__(self, path=None):
        if path == None:
            import tkinter as tk
            from tkinter import filedialog
            root = tk.Tk()
            path = filedialog.askopenfilename()
            root.withdraw()
        if path.endswith('.edf'):
            self._mne_raw = mne.io.read_raw_edf(path, preload=True)
        elif path.endswith('.vhdr'):
            self._mne_raw = mne.io.read_raw_brainvision(path, preload=True)
            self._array_of_time_stimulus, self._dict_of_stimulus = mne.events_from_annotations(self._mne_raw)
        elif path.endswith('.Poly5'):
            from Poly5_Reader import Poly5Reader, Channel
            data = Poly5Reader(path)
            info = mne.create_info(data.num_channels, sfreq=data.sample_rate)
            self._mne_raw = mne.io.RawArray(data.samples, info)
        else:
            print("Unsupported data format")

    def mne_raw(self):
        return self._mne_raw

    def show_stimulus(self):
        self._list_of_st = []
        for i in self._dict_of_stimulus:
            self._list_of_st.append(self._dict_of_stimulus[i])
        return self._list_of_st

    def show_time(self):
        for i in self._array_of_time_stimulus:
            print(i[0])

    def plot_graf(self):
        print(f"Choose event from {self.show_stimulus()[1]} to {self.show_stimulus()[-1]}")
        x = int(input())
        df = pd.DataFrame(self.show_stimulus(), columns=["col1", "col2", "col3"])
        print(df)
