import argparse

import hydra
from dotmap import DotMap
from omegaconf import DictConfig, OmegaConf

from predict import Predictor


def patch_argparse_for_hydra() -> None:
    """Allow Hydra 1.3 lazy help objects under Python 3.14 argparse."""
    original_check_help = argparse.ArgumentParser._check_help

    def check_help(self, action):
        if action.help is not None and not isinstance(action.help, str):
            action.help = repr(action.help)
        return original_check_help(self, action)

    argparse.ArgumentParser._check_help = check_help


patch_argparse_for_hydra()


@hydra.main(version_base=None, config_path="conf", config_name="config")
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    predictor = Predictor(DotMap(OmegaConf.to_container(cfg, resolve=True)))
    predictor.train()


if __name__ == "__main__":
    main()
