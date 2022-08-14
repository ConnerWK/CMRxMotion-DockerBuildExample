## Start from this Docker image (The NVIDIA container image for PyTorch, release 21.05, is available on NGC.)
FROM nvcr.io/nvidia/pytorch:21.05-py3

## Alternative start from a lightweight CUDA image
# FROM nvidia/cuda:11.3.0-base-ubuntu20.04

## Set workdir in Docker Container
# set default workdir in your docker container
# In other words your scripts will run from this directory
WORKDIR /workdir

## Copy all your files of the current folder into Docker Container
COPY ./ /workdir
RUN chmod a+x /workdir/inference.py

## Install requirements
RUN pip3 install -r requirements.txt

## Make Docker container executable
ENTRYPOINT ["/opt/conda/bin/python", "inference.py"]
