# Model Card: EMG Gesture Decoding Baseline

## Model Details

- Model type: Linear Discriminant Analysis (LDA)
- Input: 32 time-domain EMG features
- Features per channel: RMS, mean absolute value, waveform length, zero crossings
- Channels: Eight Myo armband EMG channels
- Preprocessing: Fourth-order 20–80 Hz Butterworth band-pass filtering
- Segmentation: 200 ms windows with 50% overlap

## Intended Use

Educational and research demonstration of an interpretable EMG gesture-classification workflow using public data.

## Out of Scope

This model is not a medical device and must not be used for diagnosis, treatment, clinical decision-making, prosthetic control, or safety-critical control.

## Evaluation Data

- Dataset: UCI EMG Data for Gestures
- Evaluation unit: Fixed-duration windows extracted from a single selected recording
- Active gestures: Classes 1–6
- Trial structure: Two continuous trials per active gesture

## Performance

### Exploratory random-window baseline

- Classes: 0–6, including rest
- Accuracy: 0.681
- Macro F1: 0.668
- Limitation: 50% overlapping windows can create correlated training and test examples.

### Trial-held-out evaluation

- Classes: 1–6, active gestures only
- Accuracy: 0.792
- Macro F1: 0.785
- Training windows: 494
- Test windows: 501
- Protocol: Train on the first continuous trial of each gesture; test on the second continuous trial.

## Key Findings

RMS was the highest-importance feature family under permutation importance, followed by mean absolute value and waveform length.

## Limitations

- One selected recording only
- No cross-user validation
- No cross-session validation
- Two trials per active gesture
- Dataset-specific sampling-rate and filter assumptions
- No real-time latency, robustness, or deployment testing
- Results cannot be interpreted as clinical performance

## Ethical and Safety Notes

This work uses public data for educational and research demonstration. It does not make physiological, diagnostic, or therapeutic claims.
