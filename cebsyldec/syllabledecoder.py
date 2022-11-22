def get_CV_sequence(word):
    word=word.lower()
    vowels=["a","e","i","o","u"]
    consonants=["p", "t", "k", "b", "d", "g", "m", "n", "ng", "s", "h", "l", "r","w","y"]
    consonant_clusters=["pw", "py", "pr", "pl", "tw", "ty", "tr", "ts", "kw","ky","kr","kl","bw","by","br","bl","dw","dy","dr","gw","gr","mw","my","nw","ny","sw","sy","hw"]
    glottal_stop=["-"] # plus VV
    
    prev_cons=None
    cv_seq=""
    skip=False
    
    for char in word:
        if char not in vowels and char not in consonants:
            continue
        elif prev_cons=="n" and char=="g":
            prev_cons="ng"
            continue
        elif prev_cons and char in vowels:
            cv_seq +="V"
        elif prev_cons and prev_cons + char in consonant_clusters:
            cv_seq +="CC"
            prev_cons=None
        elif char in consonants:
            cv_seq +="C"
            prev_cons=char
        elif char in vowels:
            cv_seq +="V"
            prev_cons=None
        
    return cv_seq

def get_syllable_sequence(word):
    word=word.lower()
    syl_seq = get_CV_sequence(word)
    
    while "CCVCCV" in syl_seq:
        syl_seq = syl_seq.replace("CCVCCV","CCVC-CV")
    while "CCVCV" in syl_seq:
        syl_seq = syl_seq.replace("CCVCV","CCV-CV")
    while "VCC" in syl_seq:
        syl_seq = syl_seq.replace("VCC","VC-C")
    while "CVCV" in syl_seq:
        syl_seq = syl_seq.replace("CVCV","CV-CV")
    while "VV" in syl_seq:
        syl_seq = syl_seq.replace("VV","V-V")
    while "VCVC" in syl_seq:
        syl_seq = syl_seq.replace("VCVC","V-CVC")
    while "VVC" in syl_seq:
        syl_seq = syl_seq.replace("VVC","V-VC")
    return syl_seq


def get_syllables(word):
    word=word.lower()
    syl_seq = get_syllable_sequence(word)
    
    syl_seq_arr = syl_seq.split("-")
    syllables=[]
    i=0
    for syl in syl_seq_arr:
        chars = len(syl)
        if "ng" in word[i:i+chars+1]:
            syllables.append(word[i:i+chars+1])
            i += chars+1
        else:
            syllables.append(word[i:i+chars])
            i += chars
    
    return syllables


if __name__ == "__main__":
    pass
