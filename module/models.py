from cmath import log
from unittest import result
import numpy 
import librosa
import glob
import pandas as pd
import csv
from .helpers import get_freq_from_HPS

class Saron:

    expected_bilah = ""
    audio_path = ""

    def __init__(self, expected_bilah, audio_path):
        self.expected_bilah = expected_bilah
        self.audio_path = audio_path

    def predict_bilah(self):
        if self.expected_bilah.find("pelog") == 0:
            dataset=pd.read_csv('content/dataset_saron_pelog.csv', index_col=False)
            data_nama=pd.read_csv('content/dataset_saron_pelog.csv', index_col=False)
        else:
            dataset=pd.read_csv('content/dataset_saron_slendro.csv', index_col=False)
            data_nama=pd.read_csv('content/dataset_saron_slendro.csv', index_col=False)

        dataset = dataset[dataset.columns[1:2]]
        number_of_rows,number_of_cols = dataset.shape

        data_nama = data_nama[data_nama.columns[2:3]]
        number_of_rows,number_of_cols = data_nama.shape

        data_nama_value = numpy.array(data_nama)
        dataset_value = numpy.array(dataset)

        # main

        # databaru ini nantinya berisikan path dari android inputan user
        databaru = glob.glob(self.audio_path)

        hasil_freq = []
        value_freq = float()

        for a in databaru:
            x, sr = librosa.load(a)
            value = get_freq_from_HPS(x,sr)
            value_freq = value

        selisih = []

        for j in dataset_value:
            coba = abs(float(j)-float(value_freq))
            selisih.append(coba)
        
        pilihan_terbaik = selisih.index(min(selisih))
        jawaban = data_nama_value[pilihan_terbaik]
        

        return str(jawaban).replace('\'', '').replace('[', '').replace(']', '')