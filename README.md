# Robust EMG Gesture Decoding and Signal-Quality Analysis

A Python-based neural-engineering project that analyzes public surface electromyography (sEMG) recordings to classify hand gestures and evaluate model robustness across participants and recording sessions.

## Goal

Build a reproducible workflow to:

- Load and visualize EMG recordings
- Preprocess and segment biosignal data
- Extract interpretable time- and frequency-domain features
- Train a baseline gesture-classification model
- Evaluate performance across participants and sessions
- Visualize signal quality and classification errors

## Background

This project extends my prior work with EMG biofeedback, real-time signal visualization, and muscle-activation classification for a phantom-limb-pain rehabilitation prototype. This independent project uses public data and is intended for educational and research purposes only; it is not a medical device or clinical decision-support tool.

## Tools

- Python
- NumPy and pandas
- SciPy
- scikit-learn
- Matplotlib and Seaborn
- Jupyter Notebook

## Status

In development. Current milestone: load a public EMG dataset and generate correctly labeled raw-signal plots.

## Planned Evaluation

The project will compare:

1. A standard random train/test split
2. Participant-held-out validation
3. Session-held-out validation

## Repository Structure

```text
notebooks/   Exploratory analysis
src/         Reusable processing and modeling code
figures/     Generated plots
reports/     Results and technical documentation
```

## Disclaimer

This repository is for educational and research demonstration purposes only. It is not validated for diagnosis, treatment, or clinical use.
