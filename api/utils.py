def load_model(model_path):
    """Loads the given model form the given path"""
    model = None
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    return model