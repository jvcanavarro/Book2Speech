from itertools import islice
from symspellpy import SymSpell, Verbosity


def correct_spelling(text, dictionary_path, mode):
    sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)

    correct_text = list()
    if mode == "simple":
        sym_spell.load_dictionary(dictionary_path, 0, 1)
        # for word in text:
        #     suggestions = sym_spell.lookup(
        #         word, Verbosity.TOP, max_edit_distance=2, include_unknown=True
        #     )
        suggestions = sym_spell.lookup(
            " ".join(text), verbosity=Verbosity.TOP, max_edit_distance=2, include_unknown=True
        )
        correct_text = suggestions[0].term.split()
        print(correct_text)

    elif mode == "compound":
        sym_spell.load_bigram_dictionary(dictionary_path, 0, 1)
        suggestions = sym_spell.lookup_compound(" ".join(text), max_edit_distance=2)
        correct_text = suggestions[0].term.split()

        counter = 0
        for i in range(len(text)):
            if text[i] != correct_text[i]:
                print(text[i], " -- ", correct_text[i])
                counter += 1

        print("Mismatches: ", counter)

    elif mode == "segmentation":
        sym_spell.load_dictionary(dictionary_path, 0, 1)
        suggestions = sym_spell.word_segmentation(" ".join(text), max_edit_distance=2)
        correct_text = suggestions.corrected_string.split()

    return correct_text
