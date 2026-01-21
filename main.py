import pandas as pd
from sklearn.model_selection import train_test_split
from src.missing_values import MissingValueHandler
from src.encoding import Encoder
from src.transformation import Transformer
from src.outliers import OutlierHandler
from src.feature_selection import FeatureSelector
from src.model_training import ModelTrainer

class TelcoChurnPipeline:

    def __init__(self, file_path):
        self.file_path = file_path

    def run_pipeline(self):
        try:
            # Load data
            df = pd.read_csv(self.file_path)
            print("✅ Data loaded successfully")

            # Separate target
            X = df.drop("Churn", axis=1)
            y = df["Churn"]

            # Handle missing values
            missing_handler = MissingValueHandler()
            X = missing_handler.handle_missing(X)
            print("✅ Missing values handled")

            # Encode categorical variables
            encoder = Encoder()
            X = encoder.encode_categorical(X)
            print("✅ Encoding completed")

            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )

            # Train & evaluate model
            trainer = ModelTrainer()
            model = trainer.train(X_train, y_train)
            accuracy = trainer.evaluate(model, X_test, y_test)

            print(f"🎯 Model Accuracy: {accuracy:.4f}")

        except Exception as e:
            print(f"❌ Pipeline failed: {e}")


if __name__ == "__main__":
    pipeline = TelcoChurnPipeline("WA_Fn-UseC_-Telco-Customer-Churn.csv")
    pipeline.run_pipeline()
