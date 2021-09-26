# Generated by configen, do not edit.
# See https://github.com/facebookresearch/hydra/tree/master/tools/configen
# fmt: off
# isort:skip_file
# flake8: noqa

from dataclasses import dataclass, field
from typing import Any
from typing import Optional


@dataclass
class EarlyStoppingConf:
    _target_: str = "pytorch_lightning.callbacks.EarlyStopping"
    monitor: Optional[str] = None
    min_delta: float = 0.0
    patience: int = 3
    verbose: bool = False
    mode: str = "min"
    strict: bool = True
    check_finite: bool = True
    stopping_threshold: Optional[float] = None
    divergence_threshold: Optional[float] = None
    check_on_train_epoch_end: Optional[bool] = None


@dataclass
class ModelCheckpointConf:
    _target_: str = "pytorch_lightning.callbacks.ModelCheckpoint"
    dirpath: Any = None  # Union[str, Path, NoneType]
    filename: Optional[str] = None
    monitor: Optional[str] = None
    verbose: bool = False
    save_last: Optional[bool] = None
    save_top_k: int = 1
    save_weights_only: bool = False
    mode: str = "min"
    auto_insert_metric_name: bool = True
    every_n_train_steps: Optional[int] = None
    train_time_interval: Any = None  # Optional[timedelta]
    every_n_epochs: Optional[int] = None
    save_on_train_epoch_end: Optional[bool] = None
    period: Optional[int] = None
    every_n_val_epochs: Optional[int] = None


@dataclass
class ProgressBarConf:
    _target_: str = "pytorch_lightning.callbacks.ProgressBar"
    refresh_rate: int = 1
    process_position: int = 0
