import numpy as np

def train_neuron(
    features: np.ndarray,
    labels: np.ndarray,
    initial_weights: np.ndarray,
    initial_bias: float,
    learning_rate: float,
    epochs: int
) -> (np.ndarray, float, list[float]):

    weights = initial_weights.copy()
    bias = initial_bias
    mse_values = []

    for _ in range(epochs):

        # Forward pass
        z = features @ weights + bias
        predictions = 1 / (1 + np.exp(-z))

        # MSE before update
        mse = np.mean((predictions - labels) ** 2)
        mse_values.append(mse)

        # Backpropagation
        error = 2 * (predictions - labels) * predictions * (1 - predictions)

        gradient_weights = (features.T @ error) / len(labels)
        gradient_bias = np.mean(error)

        # Gradient descent update
        weights -= learning_rate * gradient_weights
        bias -= learning_rate * gradient_bias

    updated_weights = np.round(weights, 4)
    updated_bias = round(float(bias), 4)
    mse_values = [round(float(mse), 4) for mse in mse_values]

    return updated_weights, updated_bias, mse_values