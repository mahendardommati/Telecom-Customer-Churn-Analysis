import logging

def setup_logging(script_name): # It should accept with 'script_name'
    logger = logging.getLogger() # logging is a library.
    logger.setLevel(logging.DEBUG) # logger is a object

    # Create a file handler for the script

    handler = logging.FileHandler(f'C:\\Users\\mahen\\Downloads\\Telco_Customer_Churn_Project\\logs\\{script_name}.log ', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

