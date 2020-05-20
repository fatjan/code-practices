def generate_hashtag(s):
    #your code here
    if s == '':
        return False
    else:
        hash_tag = '#'
        s_list = s.split(' ')
        for i in range(s_list.count('')):
            s_list.remove('')
        for word in s_list:
            if len(word) > 0:
                if len(word) == 1:
                    inside = word[0].upper() 
                else:
                    inside = word[0].upper() + word[1:].lower()
            hash_tag += inside
    if len(hash_tag) > 140:
        return False
    return hash_tag

print(generate_hashtag(''))
print(generate_hashtag('Do We have A Hashtag'))
print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('codewars is nice'))
print(generate_hashtag('CodeWars is nice'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice'))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))

