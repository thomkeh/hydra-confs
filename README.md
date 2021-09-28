# Configuration classes for various machine learning libraries

Configuration classes enable type-safe configuration for Hydra apps.

Currently included modules:

```yaml
    - name: pytorch_lightning.trainer
      classes:
        - Trainer
    - name: pytorch_lightning.callbacks
      classes:
        - EarlyStopping
        - ModelCheckpoint
        - ProgressBar
    - name: pytorch_lightning.metrics.classification
      classes:
        - Accuracy
        - Precision
    - name: pytorch_lightning.metrics.regression
      classes:
        - ExplainedVariance
        - MeanAbsoluteError
        - MeanSquaredError
        - MeanSquaredLogError
    - name: sklearn.preprocessing
      classes:
        - MinMaxScaler
        - StandardScaler
```
