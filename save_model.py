import pickle
import logging

logger = logging.getLogger()

def save_model(model, filename="model.pkl"):
    try:
        with open(filename, "wb") as file:
            pickle.dump(model, file)
        logger.info("Model saved successfully")
    except Exception as e:
        logger.error(e)