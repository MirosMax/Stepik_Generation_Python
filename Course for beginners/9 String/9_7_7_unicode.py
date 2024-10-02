text = input()

if '[u-' not in text:
    print(text)
else:
    for _ in range(text.count('[')):
        unicode = int(text[(text.find('[') + 3):(text.find('[') + 7)])
        unicode_text = text[text.find('['):(text.find('[') + 8)]
        text = text.replace(unicode_text, chr(unicode), 1)
    print(text)