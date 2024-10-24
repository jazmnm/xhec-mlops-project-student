def train_model(
    X_train: np.ndarray, 
    y_train: np.ndarray
    ):

    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', LinearRegression())
    ])

    pipeline.fit(X_train, y_train)
    return pipeline