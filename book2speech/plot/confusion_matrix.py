import matplotlib.pyplot as plt
from collections import defaultdict


def calculate_edits(metrics):
    truth = metrics["truth"]
    hypothesis = metrics["hypothesis"]

    true = []
    pred = []
    for edit in metrics["editops"]:

        if edit[0] == "insert":
            # print(edit[0])
            # print(truth[edit[1]])
            # print(hypothesis[edit[2]])
            true.append(truth[edit[1]])
            pred.append("_")

        elif edit[0] == "replace":
            # print(edit[0])
            # print(truth[edit[1]])
            # print(hypothesis[edit[2]])
            true.append(truth[edit[1]])
            pred.append(hypothesis[edit[2]])

        elif edit[0] == "delete":
            # print(edit[0])
            # print(truth[edit[1]])
            # print(hypothesis[edit[2]])
            true.append("_")
            pred.append(hypothesis[edit[2]])

    print(true)
    print(pred)


def generate_confusion_matrix(metrics):
    _ = calculate_edits(metrics)