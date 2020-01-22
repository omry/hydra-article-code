# hydra-article-code

This repo contains a few examples from the Hydra article.

Check out the repo, and install hydra with `pip install hydra-core`.

You can then run those examples.
See the article or the [Hydra website](https://hydra.cc) for more info.
```yaml
$ python basic/my_app.py 
dataset:
  name: imagenet
  path: /datasets/imagenet

$ python composition/my_app.py 
dataset:
  name: cifar10
  path: /datasets/cifar10

$ python composition2/my_app.py 
dataset:
  name: cifar10
  path: /datasets/cifar10
optimizer:
  beta: 0.01
  lr: 0.1
  type: adam
```
