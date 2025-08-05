import mlflow
import os
import pandas as pd

# === 🧠 Stored Execution Rules ===
# - Logs each run with strategy name, parameters, metrics
# - Automatically uses environment variable MLFLOW_TRACKING_URI
# - Creates experiment if not present
# - Stores result CSVs in /logs/
# - Run this module inside tuner or notebook for full pipeline logging

# Set MLflow tracking URI (local folder by default)
mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "file:./ml/mlruns"))

def start_run(strategy_name, params: dict, metrics: dict, tags: dict = None):
    """
    Starts an MLflow run and logs strategy parameters and metrics.
    """
    mlflow.set_experiment(strategy_name)

    with mlflow.start_run():
        if tags:
            mlflow.set_tags(tags)

        mlflow.log_params(params)
        mlflow.log_metrics(metrics)

        print(f"✅ MLflow logged run for {strategy_name}")


def log_dataframe_as_artifact(df: pd.DataFrame, name="results.csv"):
    """
    Saves a DataFrame to /logs/ and logs it as an MLflow artifact.
    """
    path = f"logs/{name}"
    os.makedirs("logs", exist_ok=True)
    df.to_csv(path, index=False)
    mlflow.log_artifact(path)
