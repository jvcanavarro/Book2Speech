import jiwer


def apply_transformations(ground_truth, hypothesis, transformation_type):
    # TODO: select a list of transformations
    transformation = jiwer.Compose([
        jiwer.RemoveMultipleSpaces(),
        jiwer.Strip(),
        jiwer.RemoveEmptyStrings(),
        jiwer.SentencesToListOfWords()
    ])
    if transformation_type == 'reduced':
        transformation = transformation.transforms[-1]

    if transformation_type == 'extended':
        transformation.transforms = [
            jiwer.ToLowerCase(),
            jiwer.RemoveWhiteSpace(replace_by_space=True),
            jiwer.RemovePunctuation()
        ] + transformation.transforms
    return transformation(ground_truth), transformation(hypothesis)
