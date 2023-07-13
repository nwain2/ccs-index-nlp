from elasticsearch import Elasticsearch

#connect to Elasticsearch
es = Elasticsearch()

#index the preprocessed data
def index_data():
    #load the preprocessed data from a CSV file
    data = pd.read_csv('data/cyber_security_data.csv')
    
    #preprocess the data
    data['preprocessed_text'] = data['text'].apply(preprocess_text)
    
    #index each document in Elasticsearch
    for idx, row in data.iterrows():
        doc = {
            'text': row['text'],
            'preprocessed_text': row['preprocessed_text'],
            'category': row['category']
        }
        es.index(index='cyber_security_index', id=idx, body=doc)
    
    print("Data indexed successfully.")

#search for relevant artifacts based on user query
def search(query):
    #preprocess the user query
    preprocessed_query = preprocess_text(query)
    
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
    #index the data
    index_data()
    
    #example search query
    user_query = input("Enter your search query: ")
    search(user_query)
