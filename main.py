import hydra
from omegaconf import DictConfig, OmegaConf
from dotmap import DotMap

from predict import Predictor


@hydra.main(version_base=None, config_path='conf', config_name='config')
def main(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    predictor = Predictor(DotMap(OmegaConf.to_container(cfg, resolve=True)))
    predictor.train()


if __name__ == '__main__':
    main()
