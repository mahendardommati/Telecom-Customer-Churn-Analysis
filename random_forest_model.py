from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import sys
import logging

logger = logging.getLogger()


def train_random_forest(X_train, X_test, y_train, y_test):
    try:
        logger.info("Random Forest training started")

        rf_model = RandomForestClassifier(
            n_estimators=200,
            max_depth=10,
            random_state=42
        )

        rf_model.fit(X_train, y_train)

        y_pred = rf_model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)

        logger.info(f"Random Forest Accuracy: {acc}")
        logger.info(f"Random Forest Classification Report:\n{report}")

        logger.info("Random Forest training completed successfully")

        return rf_model

    except Exception as e:
        er_ty, er_msg, er_line = sys.exc_info()
        logger.error(f"Error in line {er_line.tb_lineno} due to {er_msg}")