#!/usr/bin/env bash

# Read name
VENV_NAME=$(head -n 1 ./binder/venv_name.txt | cut -f2 -d ' ')

# Create venv with conda
conda create -y --name ${VENV_NAME} python=3.6.5


# Replicate binder build process
conda activate ${VENV_NAME}
sh -c "./binder/postBuild --local-build"
conda deactivate


# Cleaning steps
#jupyter kernelspec uninstall ${VENV_NAME}
#conda env remove -n ${VENV_NAME}
