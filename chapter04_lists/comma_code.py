def comma_code(wordlist):
    if wordlist:
        for item in wordlist:
            if wordlist.index(item) != len(wordlist)-1:
                print(f'{item},', end = ' ')
            else:
                print(f'and {item}')
    else: 
        print("Empty list.")

if __name__ == "__main__":
    comma_code(['apples', 'bananas', 'tofu', 'cats'])