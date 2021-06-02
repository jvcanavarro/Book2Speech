# Book2Speech 📚

B2S is a stand-alone reading machine to recognize and convert the textual content of books and derivatives into audible feedback via synthesized speech. Based on the Raspberry Pi 3 equipped with the Pi NoIR camera module, Book2Speech is a machine that besides performing the image acquisition and the Optical Character Recognition and Text-to-Speech procedures, has modules for image and text processing aiming to improve the representativeness of the synthesized voice, reproduced through an external speaker.

## Requirements

* Tesseract ≥ 4.0
> By default, Tesseract only supports English. Hence, if you want to use Book2Speech to recognized non-English texts its necessary to install its referring language packages following the [official documentation](https://github.com/tesseract-ocr/tessdata).
* Python ≥ 3.5

## Installation

```bash
$ git clone https://github.com/jvcanavarro/Book2Speech
$ cd Book2Speech/
$ pip install -r requirements.txt
```

## Folders

`book2speech` : B2S modules and argument parser implementation.\
`data` : Sample images and its referring ground-truth texts.\
`results` : Results obtained by applying a variety of image and text processing pipelines whitin Book2Speech.\
`scripts` : Bash scripts utilized to prepare the dataset and generate the results.\
`utils` : Other useful resources utilized during my Undergrate Thesis writing.

## Usage

```
Usage:
  python core.py [PARAMETERS] [FLAGS]

Basic Parameters:
  -i   --image              path to a previous captured image
  -t   --text               path to the reference text, required if the metrics module is enabled
  -m   --monogram           path to the monogram dictionary to be used in text correction
  -b   --bigram             path to the bigram dictionary to be used in text correction
  -o   --output             path to store the resulting text

Flags:
       --dewarp             enable page dewarping submodule
       --play-audio         play the resulting audio
       --disable-tts        disable the TTS module
       --improve-image      enable the image processing module
       --confusion-matrix   plot a confusion matrix referring to the missrecognized characters
       --calculate-metrics  calculate and display the CER, WER, WIL and WIP error rate metrics
  -s   --save-results       save the resulting processed image
  -v   --verbose            shows program messages in terminal
       --debug              save resulting metrics and runtime in a separate file
       --help               show this message

Advanced Parameters:
       --lang               [eng, por]
       --correction-mode    [direct,  compound, segmentation]
       --transform-mode     [reduced, default, extended]
       --blur-mode          [average, median, gaussian, bilateral, disable]
       --thresh-mode        [global, otsu, mean, gaussian, disable]
       --optimizer          [Nelder-Mead, Powell, CG, BFGS, Newton-CG, L-BFGS-B, TNC, COBYLA, SLSQP,
                                 trust-constr, dogleg, trust-ncg, trust-exact, trust-krylov, disable]
```

### Examples

```bash
$ python book2speech/core.py --image data/images/book.png --text data/texts/book.txt \
--calculate-metrics
```

```bash
$ python book2speech/core.py --image data/images/book.png --text data/texts/book.txt \
--bigram dicts/en_bi.txt --improve-image --correction-mode=segmentation --transform-mode=extended \
--blur-mode=gaussian --thresh-mode=otsu --dewarp --optimizer=l-bfgs-b --calculate-metrics
```

## Additional Resources

### English Mono & Bigram Frequency Dictionaries

```bash
$ mkdir dicts/ && cd dicts/
$ curl -Lo en_mono.txt https://github.com/wolfgarbe/SymSpell/blob/master/SymSpell/frequency_dictionary_en_82_765.txt
$ curl -Lo en_bi.txt https://github.com/wolfgarbe/SymSpell/blob/master/SymSpell/frequency_bigramdictionary_en_243_342.txt
```

### ICDAR2015 Document-Image Dataset
```bash
$ curl -Lo icdar2015.zip "https://zenodo.org/record/2572929/files/sampleDataset.zip?download=1"
$ unzip icdar2015.zip
```
