import math
import re
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


def load_vocab(platform):
    vocab = {}
    with open(f'Tf-Idf/{platform}_vocab.txt', 'r') as f:
        vocab_terms = f.readlines()
    with open(f'Tf-Idf/{platform}_idf-values.txt', 'r') as f:
        idf_values = f.readlines()

    for (term, idf_value) in zip(vocab_terms, idf_values):
        vocab[term.strip()] = int(idf_value.strip())

    return vocab

def load_documents(platform):
    documents = []
    with open(f'Tf-Idf/{platform}_documents.txt', 'r') as f:
        documents = f.readlines()
    documents = [document.strip().split() for document in documents]

    print('Number of documents:', len(documents))
    print('Sample document:', documents[0])
    return documents

def load_inverted_index(platform):
    inverted_index = {}
    with open(f'Tf-Idf/{platform}_inverted_index.txt', 'r') as f:
        inverted_index_terms = f.readlines()

    for row_num in range(0, len(inverted_index_terms), 2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num + 1].strip().split()
        inverted_index[term] = documents

    print('Size of inverted index:', len(inverted_index))
    return inverted_index

def load_Q_links(platform):
    filename = ''
    if platform == 'leetcode':
        filename = 'LCQindex.txt'
    elif platform == 'codechef':
        filename = 'CCQindex.txt'
    elif platform == 'codeforces':
        filename = 'CFQindex.txt'
    else:
        print(f"Question links not available for platform: {platform}")
        return {}

    links = {}
    with open(filename, 'r') as f:
        lines = f.readlines()

    for line in lines:
        document_index, link = line.strip().split()
        links[int(document_index)] = link

    return links

def get_tf_dictionary(term, platform):
    tf_values = {}
    if term in inverted_index[platform]:
        for document in inverted_index[platform][term]:
            if document not in tf_values:
                tf_values[document] = 1
            else:
                tf_values[document] += 1

    for document in tf_values:
        tf_values[document] /= len(documents[platform][int(document)])

    return tf_values

def get_idf_value(term, platform):
    return math.log(len(documents[platform]) / vocab_idf_values[platform][term])

def calculate_sorted_order_of_documents(query_terms, platforms):
    potential_documents = {}
    for term in query_terms:
        for platform in platforms:
            if term in vocab_idf_values[platform]:
                tf_values_by_document = get_tf_dictionary(term, platform)
                idf_value = get_idf_value(term, platform)
                print(term, tf_values_by_document, idf_value)
                for document in tf_values_by_document:
                    if document not in potential_documents:
                        potential_documents[document] = tf_values_by_document[document] * idf_value
                    else:
                        potential_documents[document] += tf_values_by_document[document] * idf_value

    print(potential_documents)
    # divide by the length of the query terms
    for document in potential_documents:
        potential_documents[document] /= len(query_terms)

    potential_documents = dict(sorted(potential_documents.items(), key=lambda item: item[1], reverse=True))

    links = {}  # Create an empty dictionary to store the links
    for platform in platforms:
        print(f"Results for {platform}:")
        Q_links = load_Q_links(platform)
        for document_index in potential_documents:
            if int(document_index) < len(documents[platform]):
                if potential_documents[document_index] > 0.5:
                    links[document_index] = Q_links[int(document_index)]  # Assign the link to the document index

    return links  # Return the dictionary of links

platforms = ['leetcode', 'codeforces', 'codechef']
vocab_idf_values = {platform: load_vocab(platform) for platform in platforms}
documents = {platform: [] for platform in platforms}
inverted_index = {platform: load_inverted_index(platform) for platform in platforms}

for platform in platforms:
    documents[platform] = load_documents(platform)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

class SearchForm(FlaskForm):
    search = StringField('Enter your search term')
    submit = SubmitField('Search')



@app.route("/", methods=['GET', 'POST'])
def home():
    form = SearchForm()
    results = []
    if form.validate_on_submit():
        query = form.search.data
        q_terms = [term.lower() for term in query.strip().split()]
        results = calculate_sorted_order_of_documents(q_terms,platform)[:20:]
    return render_template('index.html', form=form, results=results)

if __name__ == "__main__":
    app.run(debug=True)