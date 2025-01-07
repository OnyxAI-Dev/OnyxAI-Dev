def validate_data(data):
    print("Validating data...")
    if not isinstance(data, dict):
        raise ValueError("Data must be a dictionary.")
    return True

def transform_data(data):
    print("Transforming data for processing...")
    return {key.upper(): value for key, value in data.items()}
