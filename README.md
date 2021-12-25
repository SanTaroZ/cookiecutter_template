## Before installing cookiecutter using anaconda

``` bash
conda config --add channels conda-forge
```

## Installing cookiecutter in a virtual environment using anaconda

``` bash
conda create --name env_name cookiecutter=1.7.3
```

## Normal installation cookiecutter

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

## Create a new project


In the directory where you want to save you new project:

```bash
cookiecutter https://github.com/SanTaroZ/cookiecutter_template
```


## Directory structure

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-ecardenas-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the environment.
        │
        └── README.md          <- The top-level README for developers using this project.

---



THIS TEMPLATE WAS CREATED THANKS TO PLATZI COURSE "ENTORNO AVANZADO DS"
