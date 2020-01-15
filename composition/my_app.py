import hydra
from omegaconf import DictConfig


@hydra.main(config_path="conf/config.yaml")
def my_app(cfg: DictConfig) -> None:
    print(cfg.pretty())


if __name__ == "__main__":
    my_app()

