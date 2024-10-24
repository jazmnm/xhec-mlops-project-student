def pickle_object(obj: Any, path: str) -> None:
    """Pickle an object and save it to a specified path."""
    try:
        with open(path, "wb") as f:
            pickle.dump(obj, f)
        print(f"Object successfully pickled and saved to {path}")
    except Exception as e:
        print(f"Error pickling the object: {e}")

