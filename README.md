# Build an ML Pipeline for Short-Term Rental Prices in NYC

In this project we have built an ML pipeline to predict Short-Term Rental prices in NYC. This pipeline consists of the following steps takes in the data and performs EDA, cleans the data, performs a train-test-split,
and trains a random forest model.

The output artifacts to this project are saved in the following Weights & Biases link: https://wandb.ai/humayun-r971/nyc_airbnb/

# File Structure

The file ```main.py``` is the main entry point to the pipeline and this script links all the steps of the pipeline together.

The files called ```conda.yaml``` defines the environment for a given part of a pipeline and installs necerssary dependencies.

The files called ```run.py``` contain the scripts that performs the tasks associated with a part of a pipeline.

The files called ```MLProject``` contain the overall structure to the MLFlow project.

The files called ```config.yaml``` contain all the hyperparameters.


# Pre-requisites

This codebase can be cloned to your local machine by running the following git command to your terminal

```git clone https://github.com/MohammedHRashid/build-ml-pipeline-for-short-term-rental-prices.git```

A conda environment has to be created in order to use the pipeline. This environment can be created by running the following command

```conda env create -f environment.yml```

After creating an environment it can be activated using

```conda activate nyc_airbnb_dev```

# Linking to Weights & Biases

To link the pipeline to your Weights & Biases account you can run the following command in the terminal

```wandb login [your API key]```

# Running the pipeline

The entire pipeline can be ran by using the command

```mlflow run .```


