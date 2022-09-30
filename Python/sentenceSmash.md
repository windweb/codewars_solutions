## Problem

Write a method smash that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

### Example
```
words = ['hello', 'world', 'this', 'is', 'great']
```
smash(words) # returns ```hello world this is great```

**First Solution:**
```python
def smash(words):
    result = ""
    for i in range(len(words)):
        if i != len(words)-1:
            result = result + words[i] + " "
        else:
            result = result + words[i]
    return result              
```

**Second Solution:**
```python
def smash(words):
    # Begin here
    result = ""
    for i in range(len(words)):
        if i != len(words)-1:
            result = result + words[i] + " "
        else:
            result = result + words[i]
    return result           
```

**Third Solution:**
```python
def smash(words):
  return " ".join(words);  
```

Codewars source [link](https://www.codewars.com/kata/53dc23c68a0c93699800041d/) 