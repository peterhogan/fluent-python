import sys,re
WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1], encoding='utf-8') as f:
    for line_num, line in enumerate(f,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            col_num = match.start()+1
            location = (line_num, col_num)
            index.setdefault(word, []).append(location)
for word in sorted(index, key = str.upper):
    print(word, index[word])
