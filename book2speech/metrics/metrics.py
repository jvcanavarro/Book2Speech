import jiwer


def generate_metrics(ground_truth, hypothesis, verbose):
    metrics = jiwer.compute_measures(ground_truth, hypothesis)

    # print()
    # print("WER: {:.2f}%".format(metrics["wer"] * 100))
    # print("CER: {:.2f}%".format(metrics["mer"] * 100))
    # print("WIL: {:.2f}%".format(metrics["wil"] * 100))
    # print("WIP: {:.2f}%".format(metrics["wip"] * 100))
    # print("-" * 15)
    # print("Hits: {}".format(metrics["hits"]))
    # print("Substitutions: {}".format(metrics["substitutions"]))
    # print("Deletions: {}".format(metrics["deletions"]))
    # print("Insertions: {}".format(metrics["insertions"]))
    # if verbose:
    #     print("-" * 15)
    #     print("Truth: {}".format(metrics["truth"]))
    #     print()
    #     print("Hypothesis: {}".format(metrics["hypothesis"]))
        # print()
        # print("Edit Operations: {}".format(metrics["editops"]))
    # print()

    return metrics
