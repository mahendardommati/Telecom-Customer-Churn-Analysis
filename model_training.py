from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

class ModelTrainer:

    def train(self, X_train, y_train):
        try:
            model = RandomForestClassifier(random_state=42)
            model.fit(X_train, y_train)
            return model
        except Exception as e:
            raise Exception(f"Model training error: {e}")

    def evaluate(self, model, X_test, y_test):
        try:
            preds = model.predict(X_test)
            return accuracy_score(y_test, preds)
        except Exception as e:
            raise Exception(f"Evaluation error: {e}")
