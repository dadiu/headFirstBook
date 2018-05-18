vowels = ['a','e','i','o','u'];
words = input('Provide a word to search for vowels:')

found={}

for letter in words:
    if letter in vowels:
        found.setdefault(letter, 0);
        found[letter] += 1

for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)');
