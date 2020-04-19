def is_isogram(string: str):
    string = string.lower().replace(' ', '').replace('-', '')
    
    return len(set(string)) == len(string)
