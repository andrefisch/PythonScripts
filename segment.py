"""
Given an longInput string and a dictionaryionary of words,
segment the longInput string into a space-separated
sequence of dictionary words if possible. For
example, if the longInput string is "applepie" and
dictionaryionary contains a standard set of English words,
then we would return the string "apple pie" as output.

String SegmentString(String input, Set<String> dict) {
    if (dict.contains(input)) return input;
    int len = input.length();
    for (int i = 1; i < len; i++) {
        String prefix = input.substring(0, i);
        if (dict.contains(prefix)) {
            String suffix = input.substring(i, len);
            String segSuffix = SegmentString(suffix, dict);
            if (segSuffix != null) {
                return prefix + " " + segSuffix;
            }
        }
    }
    return null;
}

"""

words = open("/usr/share/dict/words", "r")
dictionary = words.read()
print len(dictionary)
memoized = {}

def segmentString(longInput, dictionary):
    if longInput in dictionary:
        return longInput
    if longInput in memoized:
        return memoized[longInput]
    length = len(longInput)
    for i in range (1, length):
        word0 = longInput[0:i]
        print "Starting from beginning with: " + word0
        if word0 in dictionary:
            print "Now analyzing " + longInput[i:length]
            rest = segmentString(longInput[i:length], dictionary)
            print rest
            if rest is not None:
                print word0 + " " + rest
                # memoized[longInput] = word0 + " " + rest
                return word0 + " " + rest
    memoized[longInput] = None
    return None

# dictionary = ["the", "big", "cat"]

print segmentString("thebigcat", dictionary)
