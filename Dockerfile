## Start from this Docker image (The NVIDIA container image for PyTorch, release 22.02, is available on NGC.)
FROM nvcr.io/nvidia/pytorch:21.05-py3

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
