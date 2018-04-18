import pandas as pd
import numpy as np
import operator
#Class names
class_names = pd.read_csv('class.csv')
#Documents
documents = pd.read_csv('document.csv',encoding = "ISO-8859-1")
#Documents and tokens
#document_token = pd.read_csv('document_token.csv', encoding = "ISO-8859-1")


total_number_of_instances = document_token['token_text'].count()
print("\nTotal number of instances : ",total_number_of_instances)

sum_len = 0
sum_len_list = []
less_then_five = []
words = []
pure_words = []
for index, row in document_token.iterrows():
    words.append(str(row['token_text']))
    if str(row['token_text']) not in pure_words:
        pure_words.append(str(row['token_text']))
        
    if len(str(row['token_text'])) < 5:
        less_then_five.append(str(row['token_text']))
    
    sum_len_list.append(len(str(row['token_text'])))
    sum_len = sum_len + len(str(row['token_text']))

average_length_of_instances = sum_len / total_number_of_instances
print("Average length of instances : ", average_length_of_instances)

arr = np.array(sum_len_list)
std_dev = np.std(arr,axis=0)
print("Std dev of length of instances : ", std_dev)


word_freq = []
for word in pure_words:
    word_freq.append((word,words.count(word)))
    
freq_list = sorted(word_freq, key=operator.itemgetter(1), reverse=True)    
top50 = freq_list[:50]
top10 = freq_list[:10]
print("The most frequent 10 words : ")
print("The most frequent 50 words : ")
print("Number of instances that are less than 5 characters : ", len(less_then_five))







