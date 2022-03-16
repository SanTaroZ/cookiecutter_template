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
conda install -c conda-forge cookiecutter=1.7.3
```

## Create a new project


In the directory where you want to save you new project:

```bash
cookiecutter https://github.com/SanTaroZ/cookiecutter_template
```


## Directory structure

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- The final data sets for modeling & results
        │   └── raw            <- The original data.
        │
        ├── notebooks          <- Jupyter notebooks.
        │
        ├── .gitignore         <- Files to ignore by git.
        │
        ├── requirements.txt    <- The requirements file for reproducing the environment.
        │
        └── README.md          <- README file for developers using this project.

---

## NOTES

To open jupyter notebook write in command line: jupyter notebook

If you want to create an virutal environment through a file named environment.yml, write in command line: conda env create --file environment.yml

If you want to pass all the libraries into a file, write in command line : conda env export --from-history --file environment.yml

If you want to install libraries through a file named requirements.txt, write in command line: pip install -r requirements.txt



THIS TEMPLATE WAS CREATED THANKS TO PLATZI COURSE "ENTORNO AVANZADO DS"

This template serves as initial point for my data projects so i do not have to create a scenario from scratch every time i want to begin a project.
