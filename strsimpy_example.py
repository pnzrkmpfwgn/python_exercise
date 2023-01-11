from strsimpy.normalized_levenshtein import NormalizedLevenshtein

normalized_levenstein = NormalizedLevenshtein()
print(normalized_levenstein.distance("Hello World","World Hello"))

from strsimpy.jaro_winkler import JaroWinkler

jarowinkler = JaroWinkler()
print(jarowinkler.similarity('hello','Hello'))