def read_sentences(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return {s.strip() for s in text.split(".") if s.strip()}


def common_sentences(path1, path2):
    return len(read_sentences(path1) & read_sentences(path2))


with open("a.txt", "w", encoding="utf-8") as f:
    f.write("Привет мир. Это тест. Общее предложение.")
with open("b.txt", "w", encoding="utf-8") as f:
    f.write("Общее предложение. Другое предложение. Это тест.")

print("Одинаковых предложений:", common_sentences("a.txt", "b.txt"))
