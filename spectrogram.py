# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com. 
https://www.github.com/kyubyong/tacotron
'''
from __future__ import print_function

import copy

import librosa

#from hyperparams import Hyperparams as hp
import numpy as np
#import tensorflow as tf



def spectrogram2wav(spectrogram , phase):
    '''
    spectrogram: [t, f], i.e. [t, nfft // 2 + 1]
    '''
    
    X_t = copy.deepcopy(spectrogram)  # [f, t]
    phasenp = copy.deepcopy(phase)
    print(X_t.shape)
    print(phasenp.shape)
    X_t = X_t*phasenp
    X_t = invert_spectrogram(X_t)
    
    '''
    for i in range(10):
        X_t = invert_spectrogram(X_best)
        est = librosa.stft(X_t, 320, 160, win_length=320)  # [f, t]
        phase = est / np.maximum(1e-8, np.abs(est))  # [f, t]
        phase = np.concatenate((phase, np.ones((161, X_best.shape[0]-161))), axis=1)
        X_best = spectrogram * phase  # [f, t]
    X_t = invert_spectrogram(X_best)
    sp = X_t.shape
    print(sp)   
    ''' 
    
    #X_t = invert_spectrogram(spectrogram)
    return X_t

def invert_spectrogram(spectrogram):
    '''
    spectrogram: [f, t]
    '''
    return librosa.istft(spectrogram,160, win_length=320, window="hamming")


def restore_shape(arry, step, r):
    '''Reduces and adjust the shape and content of `arry` according to r.
    
    Args:
      arry: A 2d array with shape of [T, C]
      step: An int. Overlapping span.
      r: Reduction factor
     
    Returns:
      A 2d array with shape of [-1, C*r]
    '''
    T, C = arry.shape
    sliced = np.split(arry, list(range(step, T, step)), axis=0)
    
    started = False
    for s in sliced:
        if not started:
            restored = np.vstack(np.split(s, r, axis=1))
            started = True
        else:    
            restored = np.vstack((restored, np.vstack(np.split(s, r, axis=1))))
    
    # Trim zero paddings
    restored = restored[:np.count_nonzero(restored.sum(axis=1))]    
    return restored