#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact.
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    df = pd.read_csv(artifact_local_path)
    logging.info(f'The artifact {args.input_artifact} has been read successfully.')


    # Drop outliers
    idx = df['price'].between(args.min_price, args.max_price)
    df = df[idx].copy()
    logging.info('Outliers have been dropped.')
    
    # Convert last_review to datetime
    df['last_review'] = pd.to_datetime(df['last_review'])
    logging.info("The column last_review has been converted to DateTime format.")
    
    # Save cleaned data to csv
    df.to_csv(args.output_artifact, index=False)
    logging.info(f"The data has been cleaned and saved as {args.output_artifact}.")
    
    # Upload artifact to Weights and Biases
    artifact = wandb.Artifact(
         args.output_artifact,
         type=args.output_type,
         description=args.output_description,
     )
    artifact.add_file(args.output_artifact)
    run.log_artifact(artifact)
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help= "The name of the input data file that you wish to clean.",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type= str,
        help= "The name of the output dataset artifact.",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help= "The type of the output artifact.",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="The description of the output artifact",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help= "The Minimum price that you wish to consider for the data. Any prices below this will be dropped as outliers.",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help= "The Maximum price that you wish to consider for the data. Any prices above this will be dropped as outliers.",
        required=True
    )


    args = parser.parse_args()

    go(args)
