f = open("plain.txt","r")

all_words = map(lambda l: l.split(" "), f.readlines())
all_words = [x for subList in all_words for x in subList]


all_words = [x.replace("\r\n","") for x in all_words]
all_words = [x.strip() for x in all_words]
x = [''.join(c for c in s if c not in all_words) for s in x]


print new_words

