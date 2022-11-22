# Cebuano-Syllable-Decoder
Cebuano Syllable-Decoder

## Installation
* `pip install cebsyldec` or
* inside the folder run `python setup.py install`

## Requirements
* `python>=2.7`

## Functions
* syllabicate(word='')
   - Accepts a Cebuano word and returns the syllables of the word
   - Default Output: List of syllables
      ```
        VC+CVC etc.
      ```
   
## How to Use
```
from cebsyllabicator import syllabicator

syllabicator.syllabicate('kaonon')

Output: 
   ka + o + non
   CV + V + CVC

## References

* https://www.youtube.com/watch?v=ZULS0evRLHg

