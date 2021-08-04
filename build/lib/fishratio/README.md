### 1. Author Information
[Author: benben-miao](https://github.com/benben-miao)

[Email: benben.miao@outlook.com](benben.miao@outlook.com)

### 2. Developement
**Click**: Used for building terminal command interaction.

[Click website: https://github.com/pallets/click](https://github.com/pallets/click)

**Setuptools**: Used for building Python module.

[Setuptools website: https://github.com/pypa/setuptools](https://github.com/pypa/setuptools)

### 3. Install from PYPI for Python using PIP
**FishRatio PYPI:** Calculate the ratio and logarithmic value of species contained in several genus of a family to all species in this family.

[https://pypi.org/project/fishratio](https://pypi.org/project/fishratio)

```shell
pip install fishratio
```

### 4. Fish Ratio Usage
> Calculate the ratio and logarithmic value of species contained in several genus of a family to all species in this family

```shell
fishratio --help
Usage: fishratio [OPTIONS]

     Description:

     Calculate the ratio and logarithmic value of species contained in
     several genus of a family to all species in this family.

     Examples:

     1. Get options and parameters help:

     FishRatio --help

     2. Sample command with all default parameters:

     FishRatio --input input.xlsx     or

     FishRatio --input input.xlsx --ratio true --ln_ratio true --neg_ratio
     true --output output.xlsx

     3. Only calculate (species number of genus) / (species number of
     family):

     FishRatio --input input.xlsx --ratio true --ln_ratio false --neg_ratio
     false --output output.xlsx

Options:
  --input TEXT        Full name (path + name + extension) of input file.
                      default="input.xlsx"

  --ratio BOOLEAN     Formula: (species number of genus) / (species number of
                      family) ratio value. default=True

  --ln_ratio BOOLEAN  Formula: Log(e)(ratio value). default=True
  --neg_mul BOOLEAN   Formula: -(ratio x Log(e)(ratio value)). default=True
  --output TEXT       Full name (path + name + extension) of output file.
                      default="output.xlsx"

  --help              Show this message and exit.
```

### 5. Examples
Examples folder: `path to miniconda: ./miniconda3/lib/site-packages/fishratio/examples/`
```shell
# Sample command with all default parameters:

FishRatio --input input.xlsx
# or
FishRatio --input input.xlsx --ratio true --ln_ratio true --neg_ratio
true --output output.xlsx
```

> **input.xlsx**

| Family         | Genus           | Species |
|----------------|-----------------|---------|
| Myxinidae      | Eptatretus      | 3       |
| Chimaeridae    | Chimaera        | 1       |
| Chimaeridae    | Hydrolagus      | 1       |
| Scyliorhinidae | Apristurus      | 2       |
| Scyliorhinidae | Atelomycterus   | 1       |
| Scyliorhinidae | Cephaloscyllium | 3       |
| Scyliorhinidae | Galeus          | 1       |
| Scyliorhinidae | Halaelurus      | 1       |
| Scyliorhinidae | Parmaturus      | 1       |

> **output.xlsx**

| Family         | Genus           | Species | Ratios      | LnRatio      | NegMul      |
|----------------|-----------------|---------|-------------|--------------|-------------|
| Chimaeridae    | Chimaera        | 1       | 0.5         | -0.693147181 | 0.34657359  |
| Chimaeridae    | Hydrolagus      | 1       | 0.5         | -0.693147181 | 0.34657359  |
| Myxinidae      | Eptatretus      | 3       | 1           | 0            | 0           |
| Scyliorhinidae | Apristurus      | 2       | 0.222222222 | -1.504077397 | 0.334239422 |
| Scyliorhinidae | Atelomycterus   | 1       | 0.111111111 | -2.197224577 | 0.244136064 |
| Scyliorhinidae | Cephaloscyllium | 3       | 0.333333333 | -1.098612289 | 0.366204096 |
| Scyliorhinidae | Galeus          | 1       | 0.111111111 | -2.197224577 | 0.244136064 |
| Scyliorhinidae | Halaelurus      | 1       | 0.111111111 | -2.197224577 | 0.244136064 |
| Scyliorhinidae | Parmaturus      | 1       | 0.111111111 | -2.197224577 | 0.244136064 |