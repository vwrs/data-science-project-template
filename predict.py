import logging
from pathlib import Path
from urllib.parse import urlparse

import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


class Predictor:
    """Predictor class"""

    logging.basicConfig(level=logging.WARN)
    logger = logging.getLogger(__name__)

    def __init__(self, cfg: dict):
        """
        Args:
            cfg (dict): config
        """
        self.cfg = cfg

    def load_dataset(self, csv):
        try:
            return pd.read_csv(csv, sep=";")
        except Exception as e:
            self.logger.exception(
                "Unable to download training & test CSV, "
                "check your internet connection. Error: %s",
                e,
            )
            raise RuntimeError(f"Failed to load dataset from {csv}") from e

    def train(self):
        """Train a model."""
        mlruns_dir = Path(__file__).resolve().parent / "mlruns"
        mlflow.set_tracking_uri(mlruns_dir.as_uri())
        mlflow.set_experiment("wine-quality")

        csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
        data = self.load_dataset(csv_url)
        # Split the data into training and test sets. (0.75, 0.25) split.
        X, y = train_test_split(data)

        X_train = X.drop(["quality"], axis=1)
        X_test = y.drop(["quality"], axis=1)
        y_train = X[["quality"]]
        y_test = y[["quality"]]

        alpha = self.cfg.model.alpha
        l1_ratio = self.cfg.model.l1_ratio
        run_id = f"{self.cfg.model.type}-{alpha}-{l1_ratio}"
        with mlflow.start_run(run_name=run_id):
            lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
            lr.fit(X_train, y_train)

            predicted = lr.predict(X_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, predicted)

            print(
                f"model {self.cfg.model.type} (alpha={alpha:f}, l1_ratio={l1_ratio:f}):"
            )
            print(f"  RMSE: {rmse}")
            print(f"  MAE: {mae}")
            print(f"  R2: {r2}")

            mlflow.log_param("alpha", alpha)
            mlflow.log_param("l1_ratio", l1_ratio)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(
                    lr, name="model", registered_model_name="ElasticnetWineModel"
                )
            else:
                mlflow.sklearn.log_model(lr, name="model")

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
