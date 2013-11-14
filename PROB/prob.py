from operator import mul
from math import log
lines = list(open("input.dat"))
s = lines[0].rstrip()
gc_content_array = map(float, lines[1].rstrip().split(" "))

def make_prob_dict(gc_content):
    probs = {}
    probs['C'] = probs['G'] = gc_content / 2.0
    probs['A'] = probs['T'] = (1-gc_content)/2.0
    return probs

for gc_content in gc_content_array:
    probs = make_prob_dict(gc_content)
    print round(log(reduce(mul, map(lambda x: probs[x], s)), 10), 3),
