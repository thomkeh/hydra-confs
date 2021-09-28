"""Test config classes for sklearn."""

from omegaconf import OmegaConf
from hydra.utils import instantiate
from sklearn.preprocessing import StandardScaler

from hydra_confs.sklearn.preprocessing import StandardScalerConf

def test_standard_scaler() -> None:
    settings = OmegaConf.structured(StandardScalerConf)
    settings.with_mean = False
    scaler = instantiate(settings)
    assert isinstance(scaler, StandardScaler)
