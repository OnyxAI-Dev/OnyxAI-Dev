class DataPreprocessor:
    @staticmethod
    def clean_data(data):
        """
        Clean input data by trimming strings and removing null values.
        """
        if isinstance(data, dict):
            return {k: v.strip() if isinstance(v, str) else v for k, v in data.items() if v is not None}
        raise ValueError("Data must be a dictionary.")

    @staticmethod
    def validate_schema(data, schema):
        """
        Validate data against a given schema.
        """
        for key, value_type in schema.items():
            if key not in data or not isinstance(data[key], value_type):
                raise ValueError(f"Invalid data: {key} should be of type {value_type}.")
        return True
