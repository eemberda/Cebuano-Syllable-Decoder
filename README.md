# Cebuano-Syllable-Decoder
Cebuano Syllable Decoder

## Installation
* `pip install cebsyldec` or
* inside the folder run `python setup.py install`

## Requirements
* `python>=3.7`

## Functions
* get_syllables(word)
   - Accepts a Cebuano word and returns the syllables of the word, and the sequence of Consonants and Vowels
   - Default Output: List of syllables and Sequence of Consonants and Vowels
   - Ex. 
      ``` 
         syllabledecoder.get_syllables("tinabangay")   
         [['ti', 'na', 'ba', 'ngay'], ['CV', 'CV', 'CV', 'CVC']]
      ```
      ```
         syllabledecoder.get_syllables("mag-tinabangay") 
         [['mag', 'ti', 'na', 'ba', 'ngay'], ['CVC', 'CV', 'CV', 'CV', 'CVC']]      
      ```
## How to Use
```
from cebsyldec import syllabledecoder

syllabledecoder.get_syllables("mangaon")        

```

Output: 
   [['ma', 'nga', 'on'], ['CV', 'CV', 'VC']]


## References

* https://www.youtube.com/watch?v=ZULS0evRLHg