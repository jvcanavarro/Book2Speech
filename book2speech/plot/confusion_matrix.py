import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix


def plot_matrix(cmatrix, index):
    df = pd.DataFrame(cmatrix, index=index, columns=index)

    plt.figure(figsize=(10, 10))
    sn.heatmap(df, cmap="Pastel1_r", linewidths=0.5)
    plt.show()


def generate_confusion_matrix(metrics, verbose):
    truth = metrics["truth"]
    hypothesis = metrics["hypothesis"]

    aux = list(hypothesis)
    true = []
    pred = []

    for edit in metrics["editops"]:
        if edit[0] == "insert":
            true.append(truth[edit[2]])
            pred.append("_")

        elif edit[0] == "replace":
            true.append(truth[edit[2]])
            pred.append(hypothesis[edit[1]])
            aux.pop(edit[2])

        elif edit[0] == "delete":
            true.append("_")
            pred.append(hypothesis[edit[1]])
            aux.pop(edit[2])

    if verbose:
        print(f"True: {''.join(true)}")
        print(f"Pred: {''.join(pred)}")

    true += aux
    pred += aux

    cmatrix = confusion_matrix(true, pred, normalize="pred")
    index = sorted(set(truth + hypothesis + "_"))

    plot_matrix(cmatrix, index)

    return cmatrix
