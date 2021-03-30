import jiwer

def calculate_metrics(ground_truth, hypothesis, extend_transformations=False):
    if extend_transformations:
        transformation = jiwer.Compose([
        jiwer.ToLowerCase(),
        jiwer.RemoveWhiteSpace(replace_by_space=True),
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.SentencesToListOfWords(),
        jiwer.RemoveEmptyStrings()
        ])
    else:
        transformation = jiwer.Compose([
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.SentencesToListOfWords(),
        jiwer.RemoveEmptyStrings()
        ])

    metrics = jiwer.compute_measures(
        ground_truth, 
        hypothesis, 
        truth_transform=transformation, 
        hypothesis_transform=transformation
    )

    print('WER: {:.2f}%'.format(metrics['wer'] * 100))
    print('MER {:.2f}%'.format(metrics['mer'] * 100))
    print('WIL: {:.2f}%'.format(metrics['wil'] * 100))
    print('WIP: {:.2f}%'.format(metrics['wip'] * 100))
    print('-' * 15)
    print('Hits: {}'.format(metrics['hits']))
    print('Substitutions: {}'.format(metrics['substitutions']))
    print('Deletions: {}'.format(metrics['deletions']))
    print('Insertions: {}'.format(metrics['insertions']))
    return metrics 

