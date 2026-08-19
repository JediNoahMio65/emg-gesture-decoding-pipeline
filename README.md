# Robust EMG Gesture Decoding and Signal-Quality Analysis

A Python-based neural-engineering project that analyzes public surface electromyography (sEMG) recordings to classify hand gestures and evaluate model robustness across trials within a selected recording.

## Goal

Build a reproducible workflow to:

- Load and visualize EMG recordings
- Preprocess and segment biosignal data
- Extract interpretable time-domain features
- Train an LDA gesture-classification baseline
- Evaluate random-window and trial-held-out performance
- Analyze feature importance and classification errors

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

Core analysis is complete for one selected recording. Current results include data exploration, preprocessing, windowing, time-domain feature extraction, LDA classification, trial-held-out evaluation, and permutation feature-importance analysis.

Planned next steps include refactoring notebook functions into reusable Python modules and evaluating additional participants or recording sessions.

## Evaluation Protocols

### Exploratory Within-Recording Baseline

- Seven classes: rest plus six active gestures
- Class-balanced feature table
- Stratified 75/25 random window split
- 50% overlapping windows
- Purpose: initial baseline only; correlated windows may appear across training and test sets

### Trial-Held-Out Active-Gesture Evaluation

- Six active gestures; rest excluded
- Training set: first continuous trial of each gesture
- Test set: second continuous trial of each gesture
- Purpose: reduce overlap-related leakage by keeping each continuous trial wholly in either training or testing

## Results

### Exploratory Within-Recording Baseline

A class-balanced seven-class Linear Discriminant Analysis (LDA) baseline was evaluated using a stratified random window split.

- Accuracy: 0.681
- Macro F1: 0.668
- Input features: 32 time-domain features across eight EMG channels
- Classes: rest plus six active gesture classes

Because adjacent windows overlap by 50%, this result is exploratory and may include correlated windows across training and test sets.

### Trial-Held-Out Active-Gesture Evaluation

A second evaluation trained on the first continuous trial of each active gesture and tested on the second continuous trial.

- Accuracy: 0.792
- Macro F1: 0.785
- Training windows: 494
- Test windows: 501
- Classes: six active gesture classes; rest excluded
- Model: standardized Linear Discriminant Analysis (LDA)

This evaluation prevents individual trials from appearing in both training and test sets. It represents cross-trial performance within one recording, not cross-user, cross-session, real-time, or clinical performance.

### Feature Importance

Permutation importance was calculated on the held-out trial using macro F1 as the scoring metric.

| Feature family | Summed decrease in macro F1 |
|---|---:|
| RMS | 1.563 |
| Mean absolute value | 0.657 |
| Waveform length | 0.504 |
| Zero crossings | 0.048 |

RMS features from channels 5, 8, 3, 1, and 6 were the strongest individual predictors in the trial-held-out LDA experiment. Channel 5 RMS was the highest-ranked individual feature.

## Data Access

This project uses the UCI EMG Data for Gestures dataset, which contains recordings acquired with an eight-channel Myo armband.

Raw data are not included in this repository. Download the dataset from the UCI Machine Learning Repository and upload one raw `.txt` recording when prompted by the notebooks.

The project uses the following dataset-specific assumptions:

- Sampling rate: 200 Hz
- Eight EMG channels
- Gesture labels 0–6
- Raw data are excluded from version control

### Dataset Citation

Krilova, N., Kastalskiy, I., Kazantsev, V., Makarov, V., & Lobov, S. (2018). *EMG Data for Gestures* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5ZP5C

## Reproducibility

The notebooks use a fixed random seed of 42 for class balancing, the exploratory train/test split, and permutation-importance analysis.

To reproduce the current workflow:

1. Download the UCI EMG Data for Gestures dataset.
2. Open the notebooks in numerical order.
3. Upload one raw `.txt` recording when prompted.
4. Run all cells in each notebook from top to bottom.

Raw data are intentionally excluded from version control.

## Repository Structure

```text
notebooks/   Exploratory analysis, preprocessing, feature extraction, and modeling
src/         Reusable preprocessing and time-domain feature functions
reports/     Results documentation and model card
```

The reusable implementation is in `src/extract_features.py`. The notebooks demonstrate the full end-to-end workflow.

## Limitations

- Results are based on one selected recording.
- The project does not include cross-user validation.
- The project does not include cross-session validation.
- The trial-held-out evaluation uses two trials per active gesture.
- Results do not establish real-time, clinical, diagnostic, or therapeutic performance.
- Preprocessing and sampling-rate assumptions are specific to this dataset and recording configuration.

## Disclaimer

This repository is for educational and research demonstration purposes only. It is not validated for diagnosis, treatment, clinical use, or safety-critical control.
