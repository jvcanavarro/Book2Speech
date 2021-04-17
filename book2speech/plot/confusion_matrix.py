import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix


def generate_confusion_matrix(metrics, verbose):
    truth = metrics["truth"]
    hypothesis = metrics["hypothesis"]
    aux = list(truth)

    true = []
    pred = []

    for edit in metrics["editops"]:
        if edit[0] == "insert":
            true.append(truth[edit[1]])
            pred.append("_")

        elif edit[0] == "replace":
            true.append(truth[edit[1]])
            pred.append(hypothesis[edit[2]])
            aux.pop(edit[2])

        elif edit[0] == "delete":
            true.append("_")
            pred.append(hypothesis[edit[2]])
            aux.pop(edit[2])

    true += aux
    pred += aux

    if not verbose:
        print(metrics["editops"])
        print()
        print("".join(true))
        print("".join(pred))

    cmatrix = confusion_matrix(true, pred, normalize='all')
    print("\n", cmatrix)
    index = sorted(set(truth + hypothesis + "_"))
    df_cm = pd.DataFrame(cmatrix, index=index, columns=index)
    plt.figure(figsize=(10, 7))
    sn.heatmap(df_cm, annot=True)
    plt.show()
