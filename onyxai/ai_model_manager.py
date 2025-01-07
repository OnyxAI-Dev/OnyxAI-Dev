import joblib

class AIModelManager:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None

    def load_model(self):
        """
        Load the AI model from the specified path.
        """
        try:
            self.model = joblib.load(self.model_path)
            print("Model loaded successfully.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Model not found at {self.model_path}.")

    def predict(self, input_data):
        """
        Make predictions using the loaded model.
        """
        if self.model is None:
            raise ValueError("Model is not loaded.")
        return self.model.predict(input_data)
