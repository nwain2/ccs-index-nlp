import pandas as pd
from elasticsearch import Elasticsearch

#connect to Elasticsearch
es = Elasticsearch()

#preprocess the user query
def preprocess_query(query):
    #remove special characters and numbers
    query = re.sub(r'\W', ' ', query)
    query = re.sub(r'\d+', ' ', query)
    
    #convert to lowercase
    query = query.lower()
    
    #tokenization
    tokens = nltk.word_tokenize(query)
    
    #remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token not in stop_words]
    
    #lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    #join tokens back to text
    preprocessed_query = ' '.join(lemmatized_tokens)
    
    return preprocessed_query

#search for relevant artifacts based on user query
def search(query):
    #preprocess the user query
    preprocessed_query = preprocess_query(query)
    
    #search in Elasticsearch
    res = es.search(
        index='cyber_security_index',
        body={
            'query': {
                'match': {
                    'preprocessed_text': preprocessed_query
                }
            }
        }
    )
    
    #process the search results
    hits = res['hits']['hits']
    if len(hits) > 0:
        print("Search Results:")
        for hit in hits:
            print("Text:", hit['_source']['text'])
            print("Category:", hit['_source']['category'])
            print("---")
    else:
        print("No results found.")

if __name__ == "__main__":
    #connect to Elasticsearch
    es = Elasticsearch()
    
    #example search query
    user_query = input("Enter your search query: ")
    search(user_query)
