"""Reusable preprocessing and time-domain feature functions for sEMG analysis."""

import numpy as np
from scipy.signal import butter, filtfilt


def bandpass_filter(signal, fs=200, lowcut=20, highcut=80, order=4):
    """Apply a zero-phase Butterworth band-pass filter to a 1D signal."""
    signal = np.asarray(signal, dtype=float)
    nyquist = fs / 2

    if lowcut <= 0 or highcut >= nyquist or lowcut >= highcut:
        raise ValueError(
            "Cutoffs must satisfy 0 < lowcut < highcut < Nyquist frequency."
        )

    b, a = butter(
        order,
        [lowcut / nyquist, highcut / nyquist],
        btype="bandpass",
    )
    return filtfilt(b, a, signal)


def root_mean_square(signal):
    """Return the root-mean-square amplitude of a 1D signal."""
    signal = np.asarray(signal, dtype=float)
    return np.sqrt(np.mean(np.square(signal)))


def mean_absolute_value(signal):
    """Return the mean absolute value of a 1D signal."""
    signal = np.asarray(signal, dtype=float)
    return np.mean(np.abs(signal))


def waveform_length(signal):
    """Return the cumulative absolute difference between adjacent samples."""
    signal = np.asarray(signal, dtype=float)
    return np.sum(np.abs(np.diff(signal)))


def zero_crossings(signal, threshold=1e-7):
    """Count mean-centered sign changes that exceed an amplitude threshold."""
    signal = np.asarray(signal, dtype=float)
    centered = signal - np.mean(signal)
    crossings = np.diff(np.signbit(centered))
    amplitude_change = np.abs(np.diff(centered)) >= threshold
    return int(np.sum(crossings & amplitude_change))
