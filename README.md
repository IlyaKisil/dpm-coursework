# Coursework materials

## Completing in a cloud without installation 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IlyaKisil/dpm-coursework/master?urlpath=lab/tree/notebooks/0_Table_of_contents.ipynb)

This is as simple as clicking on the `binder` badge above. This comes at the cost of lower computational resources being available to you. 

## Completing on your personal computer
 
1.  Install Anaconda - [installation file](https://www.anaconda.com/download/) (use `python 3.7`).
2.  Install JupyterLab in the base environment - [instructions](https://github.com/jupyterlab/jupyterlab#installation). Normally, it comes with Anaconda installation by default.
3.  Get source files
    ```bash
    git clone https://github.com/IlyaKisil/dpm-coursework.git
    ```
4.  Bootstrap virtual environment. 
    
    If you are on Unix, then execute in terminal:
    ```bash
    cd dpm-coursework

    ./boostrap-venv.sh
    ```
    
    If you are on Windows, then open Anaconda prompt:
    ```bash
    cd dpm-coursework
    conda create -y --name "dpm-coursework" python=3.6.5
    conda activate "dpm-coursework"
    pip install binder\coursework
    python -m ipykernel install --user --name "dpm-coursework" --display-name "dpm-coursework"    
    ```
    
5.  Start JupyterLab and open a notebook with table of contents (should look like [this](https://github.com/IlyaKisil/dpm-coursework/blob/master/notebooks/0_Table_of_contents.ipynb)). You can find it under the `notebooks` directory. 

## Reporting problems and issues

Please use one of [these forms](https://github.com/IlyaKisil/dpm-coursework/issues/new/choose) which supports `markdown` text formatting. It would also be helpful if you include as much relevant info as possible. This could include screenshots, code snippets etc.
