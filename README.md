# Cebuano-Syllable-Decoder
Cebuano Syllable Decoder

## Installation
* `pip install cebsyldec` or
* inside the folder run `python setup.py install`

## Requirements
* `python>=2.7`

## Functions
* get_syllables(word)
   - Accepts a Cebuano word and returns the syllables of the word
   - Default Output: List of syllables
   - Ex. get_syllables("nangaon")
      ```
        ['na', 'nga', 'on']
      ```
* get_syllable_sequence(word)
   - Accepts a Cebuano word and returns the syllable sequence of the word
   - Default Output: Syllable sequence of the word
   - Ex. get_syllable_sequence("nangaon")
      ```
        'CV-CV-VC'
      ```   
## How to Use
```
from cebsyldec import syllabledecoder

syllabledecoder.get_syllables("nangaon")

Output: 
   ['na', 'nga', 'on']


syllabledecoder.get_syllable_sequence("nangaon")

Output:
   'CV + V + CVC'
```

## References

* https://www.youtube.com/watch?v=ZULS0evRLHg