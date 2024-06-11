from fuzzywuzzy import fuzz
import numpy as np
import re
      
# List of companies and their commonly used names


# Preprocessing function to clean text
def preprocess(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # Optionally, add more preprocessing steps here if needed
    return text

# def find_knn_fuzzy(query, k=3):
#     # Apply preprocessing to the query
#     processed_query = preprocess(query)
#     # Calculate fuzzy matching scores with all common names
#     scores = [fuzz.ratio(processed_query, preprocess(name)) for name in common_names]
#     # Get the indices of the top k scores in descending order
#     indices = np.argsort(-np.array(scores))[:k]
#     # Return the top k common names and their corresponding companies
#     return [(common_names[i], companies[i]) for i in indices]

# # Example usage
# query_company = "apple"
# knn_result = find_knn_fuzzy(query_company, k=3)

# print("K-nearest neighbors using Fuzzy Matching:")
# for common_name, company in knn_result:
#     print(f"{common_name}: {company}")


text_data = ["Apple Inc specializes in consumer electronics", "Google LLC is a tech giant", ...]  # Example data
tokenized_data = [preprocess(text).split() for text in text_data]
bm25 = BM25Okapi(tokenized_data)

def find_knn_bm25(query, k=3):
    query_tokens = preprocess(query).split()
    scores = bm25.get_scores(query_tokens)
    indices = np.argsort(-np.array(scores))[:k]
    return [(common_names[i], companies[i]) for i in indices]

# Example usage
query_company = "apple"
knn_result = find_knn_bm25(query_company, k=3)

print("K-nearest neighbors using Okapi BM25:")
for common_name, company in knn_result:
    print(f"{common_name}: {company}")










