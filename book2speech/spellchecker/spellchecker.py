from itertools import islice
from symspellpy import SymSpell, Verbosity


def correct_spelling(text, dictionary_path, bigram_path, mode):
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
    sym_spell.load_dictionary(dictionary_path, 0, 1)

    correct_text = []
    if mode == "simple":
        suggestions = sym_spell.lookup(
            " ".join(text),
            verbosity=Verbosity.TOP,
            max_edit_distance=2,
            include_unknown=True,
        )
        correct_text = suggestions[0].term.split()

    elif mode == "segmentation":
        suggestions = sym_spell.word_segmentation(" ".join(text), max_edit_distance=2)
        correct_text = suggestions[0].split()

    elif mode == "compound":
        sym_spell.load_bigram_dictionary(dictionary_path, 0, 1)
        suggestions = sym_spell.lookup_compound(" ".join(text), max_edit_distance=2)
        correct_text = suggestions[0].term.split()

    return correct_text
