#import another file(Manipulate string) 
import Manipulate_string
#If I type " "[apple, banana, cherry]" "
text = (input("Enter a sentence:"))
#If I type "This is a test sentence."
sentence = (input("Enter a list of words"))
#If I type "["Python", "is", "fun"]"
words = (input("Enter a string with words separted by commas:"))

#print it(replace comas with space)
#"[apple  banana  cherry]"
print(Manipulate_string.replace_comas_with_space(text))

#print it(string string split sentence)
#['This', 'is', 'a', 'test', 'sentence']
print(Manipulate_string.split_sentence(sentence))

#print it(string join words)
#[ " P y t h o n " ,   " i s " ,   " f u n " ]
print(Manipulate_string.join_words(words))

"""
text = "[apple,banana,cherry]"
sentence = "This is a test sentence."
words = ["Python", "is", "fun"]
"""
