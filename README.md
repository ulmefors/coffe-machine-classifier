# coffee-machine-classifier

Classify coffee machines using fastai (pytorch). Create dataset using Bing Image Search API.

## Install

```shell
$ conda create -n coffee python=3.6
$ conda activate coffee
$ conda install -c fastai -c pytorch fastai jupyterlab path
```

## Data

Download data using Bing Image Search API. Create account and set API subscription key

```shell
export AZURE_SEARCH_KEY=<my_key>
```

## Run

```shell
$ jupyter lab
```

Open `model.ipynb`

