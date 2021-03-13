

# First Step : Go to cmd and type: pip install googletrans==3.1.0a0


# Using the Translator Class
from googletrans import Translator

# Making Object of Translator Class
translator  = Translator()


# Word you want to translate
Word = input('Enter what you want to translate : ')



# For further language Codes
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
Code = input('Enter Language Code : ')


# Using the translator method to get work done
translation = translator.translate(Word,dest=Code)

# printing to console
print(translation.text)
