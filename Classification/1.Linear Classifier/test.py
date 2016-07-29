def remove_punctuation(text):
    import string
    return text.translate(None, string.punctuation) 
print remove_punctuation("Cake!")