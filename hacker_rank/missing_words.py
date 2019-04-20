def missingWords(s, t):
    s = s.split()
    t = t.split()
    missing = []

    for w in s:
        if t and w == t[0]:
            t.pop(0)
        else:
            missing.append(w)

    return missing

assert missingWords(
        "I am using hackerrank to improve programming",
        "am hackerrank to improve") == ["I",'using','programming']

assert missingWords(
        'Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing',
        'Python is an easy to learn powerful programming language') ==  ['It', 'has', 'efficient', 'high-level', 'data',
        'structures', 'and', 'a', 'simple', 'but',
        'effective', 'approach', 'to', 'objectoriented',
        'programming', 'Python', 'elegant',
        'syntax', 'and', 'dynamic', 'typing']
 