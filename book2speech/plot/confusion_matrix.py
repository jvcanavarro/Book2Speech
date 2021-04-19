import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix


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

    true += aux
    pred += aux

    if verbose verbose:
        print(metrics["editops"])
        print()
        print("".join(true))
        print("".join(pred))

    index = sorted(set(truth + hypothesis + ""))
    cmatrix = confusion_matrix(true, pred, normalize="pred")

    df = pd.DataFrame(cmatrix, index=index, columns=index)

    plt.figure(figsize=(10, 10))
    sn.heatmap(df) 
    plt.show()
