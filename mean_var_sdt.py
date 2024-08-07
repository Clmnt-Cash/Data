import numpy as np


def calculate(list):

    if len(list) < 9:
        raise ValueError(
            "list must contain nine numbers"
        )  # on renvoi le message d'error si inférieur à 9

    matrice = np.array(list).reshape(3, 3)  # on met la liste en matrice

    calculations = {
        "mean": [
            matrice.mean(axis=0).tolist(),
            matrice.mean(axis=1).tolist(),
            matrice.mean().item(),
        ],  # la moyenne des colonnes, des lignes et de la matrice
        "variance": [
            matrice.var(axis=0).tolist(),
            matrice.var(axis=1).tolist(),
            matrice.var().item(),
        ],  # la variance des colonnes, des lignes et de la matrice
        "standard deviation": [
            matrice.std(axis=0).tolist(),
            matrice.std(axis=1).tolist(),
            matrice.std().item(),
        ],  # la déviation standard des colonnes, des lignes et de la matrice
        "max": [
            matrice.max(axis=0).tolist(),
            matrice.max(axis=1).tolist(),
            matrice.max().item(),
        ],  # le max des colonnes, des lignes et de la matrice
        "min": [
            matrice.min(axis=0).tolist(),
            matrice.min(axis=1).tolist(),
            matrice.min().item(),
        ],  # le min des colonnes, des lignes et de la matrice
        "sum": [
            matrice.sum(axis=0).tolist(),
            matrice.sum(axis=1).tolist(),
            matrice.sum().item(),
        ],  # la somme des colonnes, des lignes et de la matrice
    }

    return calculations
