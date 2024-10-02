from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Function to break Sanskrit words into syllables
def break_into_syllables(word):
    iast_word = transliterate(word, sanscript.DEVANAGARI, sanscript.IAST)

    syllables = []
    buffer = ''
    for char in iast_word:
        buffer += char
        if char in 'aāiīuūṛṝeaiouṃḥ':
            syllables.append(buffer.strip())
            buffer = ''

    if buffer:
        syllables.append(buffer)

    devanagari_syllables = [transliterate(syl, sanscript.IAST, sanscript.DEVANAGARI) for syl in syllables]
    return ' '.join(devanagari_syllables)
