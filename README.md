# Coursework materials

<!--ts-->
   
* [Completing in a cloud without installation](#completing-in-a-cloud-without-installation)
* [Completing on your personal computer](#completing-on-your-personal-computer)
* [Reporting problems and issues](#reporting-problems-and-issues)

<!-- Added by: Ilya Kisil, at: 2019-02-19T18:19+00:00 -->

<!--te-->


## Completing in a cloud without installation 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/IlyaKisil/dpm-coursework/master?urlpath=lab/tree/notebooks/0_Table_of_contents.ipynb)

This is as simple as clicking on the `binder` badge above and requires to be connected to internet. Although, this option comes at the cost of lower computational resources being available to you, but it will be sufficient to successfully complete all assignments.

> **Note:** It may take a couple of minutes to launch a `binder` server. If it takes longer then that, try to refresh the web page before [reporting this issue](#reporting-problems-and-issues).  

## Completing on your personal computer
 
1.  Install Anaconda - [installation file](https://www.anaconda.com/download/) (use `python 3.7`).

2.  Install JupyterLab in the base environment - [instructions](https://github.com/jupyterlab/jupyterlab#installation). Normally, it comes with Anaconda installation by default.

3.  Get source files.

    Preferred option is to clone this repository using [git](https://git-scm.com/downloads).
    ```bash
    git clone https://github.com/IlyaKisil/dpm-coursework.git
    ```
    If this is the first time you hear about `git`, it is recommended to watch one of many introductory videos about it, for example [on YouTube](https://www.youtube.com/results?search_query=git+basics).
    
    Alternatively, you can download a ZIP folder with all materials for this assignment by using the `Clone or Download` button (in green color) at the top of this page. 
    
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

Please use one of [these forms](https://github.com/IlyaKisil/dpm-coursework/issues/new/choose) which supports `markdown` text formatting. It would also be helpful if you include as much relevant information as possible. This could include screenshots, code snippets etc.
