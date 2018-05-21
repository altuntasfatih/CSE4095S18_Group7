import pandas as pd
import openpyxl
#document = pd.read_csv('presentation/document.csv')
#document_token = pd.read_csv('statistic/document_token.csv',encoding = "ISO-8859-1")

number_of_rows = len(documents)
#number of columns is missing

document_token_new = document_token.copy()

##ADDING NEW FEATURES TO DATASET

#Start Capital (whether the term is capitalized or not)
document_token_new['start_capital']= 0
for index, row in document_token_new.iterrows():
    word = str(row['token_text'])
    if word[0].isupper():
        document_token_new.at[index,'start_capital'] = 1

#All Capital (If the term is all uppercase)
document_token_new['all_capital']= 0
for index, row in document_token_new.iterrows():
    word = str(row['token_text'])
    if word.isupper():
        document_token_new.at[index,'all_capital'] = 1

#Capital Ratio (the ratio of capital letters in the term)
document_token_new['capital_ratio']= 0.0
for index, row in document_token_new.iterrows():
    word = str(row['token_text'])
    ratio = (sum(1 for c in word if c.isupper())) / len(word)
    document_token_new.at[index,'capital_ratio'] = ratio
    
#Length (number of characters in the word)
document_token_new['length']= 0
for index, row in document_token_new.iterrows():
    word = str(row['token_text'])
    document_token_new.at[index,'length'] = len(word)

#Vowel Ratio (The ratio of number consonant over the number of vowels in the word)
#Number of Vowels (The number vowels in the word) 
document_token_new['vowel_ratio']= 0.0
document_token_new['number_of_vowels']= 0.0
vowels = list("aeıioöuü")
consonants = list("bcçdfgğhjklmnpqrsştvwyxz") 
for index, row in document_token_new.iterrows():
    word = str(row['token_text']).lower()
    
    number_of_consonants = sum(word.count(c) for c in consonants)
    number_of_vowels = sum(word.count(c) for c in vowels)
    
    try:
        vowel_ratio = number_of_consonants / number_of_vowels
    except:
        vowel_ratio = number_of_consonants
    
    document_token_new.at[index,'vowel_ratio'] = vowel_ratio
    document_token_new.at[index,'number_of_vowels'] = number_of_vowels

#Number of numeric characters (The number of numerical characters {0,1,2,3,4,5,6,7,8,9} in the term)
#Numeric Ratio (The ratio of numerical characters {0,1,2,3,4,5,6,7,8,9} in the term)    
document_token_new['numeric_charecter']= 0.0
document_token_new['numeric_ratio']= 0.0
for index, row in document_token_new.iterrows():
    word = str(row['token_text'])
    number_numeric_charecter = sum(1 for c in word if c.isnumeric())
    document_token_new.at[index,'numeric_charecter'] = number_numeric_charecter
    document_token_new.at[index,'numeric_ratio'] = number_numeric_charecter / len(word)

#Number Of NonAlphanumeric  (The number of characters except alphanumerical characters a-z and 0-9 in the term) 
#NonAlphanumericRatio (The ratio of characters except alphanumerical characters a-z and 0-9 in the term) 
document_token_new['number_of_nonAlphanumeric']= 0.0
document_token_new['nonAlphanumericRatio ']= 0.0
for index, row in document_token_new.iterrows():
    word = str(row['token_text'])
    nonAlphanumberic_word = ''.join([i for i in word if not i.isalnum()])
    
    document_token_new.at[index,'number_of_nonAlphanumeric'] = len(nonAlphanumberic_word)
    document_token_new.at[index,'nonAlphanumericRatio'] = len(nonAlphanumberic_word) / len(word)

error_row = []
for index, row in document_token_new.iterrows():
    if type(row['c_id']) is type(None):
        error_row.append(index)
        
document_token_new = document_token_new.drop(document_token_new.index[error_row])

document_token_new.to_csv('presentation/document_token_new_features.csv',index=False)
writer = pd.ExcelWriter('presentation/document_token_new_features.xlsx')
document_token_new.to_excel(writer)
writer.save()

