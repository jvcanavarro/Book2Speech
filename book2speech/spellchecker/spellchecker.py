from itertools import islice
from symspellpy import SymSpell, Verbosity


def correct_spelling(text, dictionary_path, mode):
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    sym_spell.load_dictionary(dictionary_path, 0, 1)
    correct_text = list()

    if mode == "simple":
        for word in text:
            suggestions = sym_spell.lookup(
                word, Verbosity.TOP, max_edit_distance=2, include_unknown=True
            )
            correct_text.append(suggestions[0].term)
    elif mode == "compound":
        pass
    elif mode == "segmentation":
        pass

    return correct_text
