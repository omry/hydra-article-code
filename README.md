# hydra-article-code

This repo contains a few examples from [Hydra — A fresh look at configuration for machine learning projects](http://bit.ly/2Sdq2B3).

Check out the repo, and install hydra with `pip install hydra-core`.

You can then run those examples.
See the [article](https://medium.com/@pytorch/50583186b710) or the [Hydra website](https://hydra.cc) for more info.
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
