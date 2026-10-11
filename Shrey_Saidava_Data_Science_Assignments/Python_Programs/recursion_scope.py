def total_plays(plays):
    if len(plays) == 0:
        return 0
    return plays[0] + total_plays(plays[1:])

def reverse_text(text):
    if len(text) <= 1:
        return text
    return reverse_text(text[1:]) + text[0]

print(total_plays([120, 80, 150, 200]))
print(reverse_text("spotify"))
