f = open("plain.txt","r")

all_words = map(lambda l: l.split(" "), f.readlines()) #readslines
all_words = [w for subList in all_words for w in subList] #flattens
all_words = [w.replace("\r\n","") for w in all_words] #removes annoying


def frequency(word):
	return len([x for x in all_words if x == word])


print "Frequence of 'the':"
print frequency('the')
print "Frequence of 'ship':"
print frequency('ship')
print "\n"

def totalFrequency(words):
	return reduce(lambda x,y: x+y, [frequency(a) for a in words])

print "Frequence of 'the' and 'ship':"
print totalFrequency(['ship','the'])
print "\n"


def mostFrequent():
	return reduce(lambda x,y: x if x!=y and frequency(x) > frequency(y) else y, all_words)

print "Most frequent word is"
print mostFrequent()
print "\n"