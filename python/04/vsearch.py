def search4vowels(words):
    """Display any vowels found in an supplied word."""
    vowels = set('aeiou');

    found = vowels.intersection(set(words));

    for viwel in found:
        print(viwel);


        
