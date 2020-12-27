def duplicate_count(text):
    output = 0
    lowered = text.lower()
    counts = {}
    for i in lowered:
        counts[i] = counts.get(i, 0) + 1
    for letter, cnt in counts.items():
        if cnt > 1:
            output += 1
    return output
