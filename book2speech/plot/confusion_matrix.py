import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import confusion_matrix


def generate_confusion_matrix(metrics, verbose):
    truth = metrics["truth"]
    hypothesis = metrics["hypothesis"]

    # print(truth)
    # print()
    # print(hypothesis)
    aux = list(truth)

    true = []
    pred = []

    for edit in metrics["editops"]:
        print(edit)
        if edit[0] == "insert":
            print(f"Insert {truth[edit[1]]}")
            true.append(truth[edit[1]])
            pred.append("_")

        elif edit[0] == "replace":
            print(f"Replace {hypothesis[edit[2]]}")
            print(f"with {truth[edit[1]]}")

            true.append(truth[edit[1]])
            pred.append(hypothesis[edit[2]])
            aux.pop(edit[2])

        elif edit[0] == "delete":
            print(f"Delete {hypothesis[edit[2]]}")

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

    index = sorted(set(truth + hypothesis + ""))
    cmatrix = confusion_matrix(true, pred, normalize="pred")

    # df = pd.DataFrame(cmatrix, index=index, columns=index)

    # plt.figure(figsize=(10, 10))
    # sn.heatmap(df) 
    # plt.show()
