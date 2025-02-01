from flask import Flask, jsonify, render_template, request, redirect, url_for
import math
import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import codecs
from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key'

def load_vocab(filename):
    vocab = {}
    with open(filename, "r") as f:
        vocab_terms = f.readlines()
    with open(filename.replace("vocab", "idf-values"), "r") as f:
        idf_values = f.readlines()

    for (term, idf_value) in zip(vocab_terms, idf_values):
        vocab[term.rstrip()] = int(idf_value.rstrip())

    return vocab

def load_document(filename):
    doc_dict = {}
    with open(filename, "r") as f:
        documents = f.readlines()
        for idx, doc in enumerate(documents):
            parts = doc.strip().split('||')
            if len(parts) == 2:
                doc_dict[str(idx)] = {
                    'challenge_name': parts[0],
                    'full_text': doc
                }
            else:
                doc_dict[str(idx)] = {
                    'challenge_name': doc.strip(),
                    'full_text': doc
                }
    return doc_dict

def load_inverted_index(filename):
    inverted_index = {}
    with open(filename, "r") as f:
        inverted_index_terms = f.readlines()

    for row_num in range(0, len(inverted_index_terms), 2):
        term = inverted_index_terms[row_num].strip()
        documents = inverted_index_terms[row_num+1].strip().split()
        inverted_index[term] = documents

    return inverted_index

def load_link_of_qs(filename):
    with open(filename, "r") as f:
        links = f.readlines()
    return links

def get_tf_dict(term, inverted_index, document):
    tf_dict = {}
    if term in inverted_index:
        for doc in inverted_index[term]:
            if doc not in tf_dict:
                tf_dict[doc] = 1
            else:
                tf_dict[doc] += 1

    for doc in tf_dict:
        try:
            tf_dict[doc] /= len(document[doc]['full_text'].split())
        except (ZeroDivisionError, ValueError, IndexError, KeyError) as e:
            print(f"Error calculating tf: {e}")
            print(doc)

    return tf_dict

def get_idf_value(term, vocab, document):
    return math.log((1 + len(document)) / (1 + vocab[term]))

def calc_docs_sorted_order(q_terms, vocab, document, inverted_index, Qlink):
    potential_docs = {}
    ans = []
    
    for term in q_terms:
        if term not in vocab:
            continue

        tf_vals_by_docs = get_tf_dict(term, inverted_index, document)
        idf_value = get_idf_value(term, vocab, document)

        for doc in tf_vals_by_docs:
            if doc not in potential_docs:
                potential_docs[doc] = tf_vals_by_docs[doc] * idf_value
            else:
                potential_docs[doc] += tf_vals_by_docs[doc] * idf_value

    for doc in potential_docs:
        potential_docs[doc] /= len(q_terms)

    potential_docs = dict(sorted(potential_docs.items(), key=lambda item: item[1], reverse=True))

    if len(potential_docs) == 0:
        print("No matching question found. Please search with more relevant terms.")

    for doc_index in potential_docs:
        try:
            challenge_name = document[doc_index]['challenge_name']
            ans.append({
                "Question Link": Qlink[int(doc_index) - 1][:-2],
                "Challenge Name": challenge_name,
                "Score": potential_docs[doc_index]
            })
        except (KeyError, IndexError) as e:
            print(f"Error processing document index {doc_index}: {e}")
            continue

    return ans

class SearchForm(FlaskForm):
    search = StringField('Search')

@app.route('/leetcode')
def search_leetcode():
    query = request.args.get('query')
    vocab = load_vocab("./data/leetcode/vocab.txt")
    document = load_document("./data/leetcode/documents.txt")
    inverted_index = load_inverted_index("./data/leetcode/inverted-index.txt")
    Qlink = load_link_of_qs("./data/leetcode/question-links.txt")

    if query:
        query = re.sub(r'[^a-zA-Z0-9\s]+', '', query.encode('utf-8').decode('unicode_escape'))
        query_terms = query.lower().split()
        results = calc_docs_sorted_order(query_terms, vocab, document, inverted_index, Qlink)
        return jsonify(results)
    else:
        return jsonify([])

@app.route('/codeforces')
def search_codeforces():
    query = request.args.get('query')
    vocab = load_vocab("./data/codeforces/vocab.txt")
    document = load_document("./data/codeforces/documents.txt")
    inverted_index = load_inverted_index("./data/codeforces/inverted-index.txt")
    Qlink = load_link_of_qs("./data/codeforces/question-links.txt")

    if query:
        query = re.sub(r'[^a-zA-Z0-9\s]+', '', query.encode('utf-8').decode('unicode_escape'))
        query_terms = query.lower().split()
        results = calc_docs_sorted_order(query_terms, vocab, document, inverted_index, Qlink)
        return jsonify(results)
    else:
        return jsonify([])

@app.route('/codechef')
def search_codechef():
    query = request.args.get('query')
    vocab = load_vocab("./data/codechef/vocab.txt")
    document = load_document("./data/codechef/documents.txt")
    inverted_index = load_inverted_index("./data/codechef/inverted-index.txt")
    Qlink = load_link_of_qs("./data/codechef/question-links.txt")

    if query:
        query = re.sub(r'[^a-zA-Z0-9\s]+', '', query.encode('utf-8').decode('unicode_escape'))
        query_terms = query.lower().split()
        results = calc_docs_sorted_order(query_terms, vocab, document, inverted_index, Qlink)
        return jsonify(results)
    else:
        return jsonify([])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        query = form.search.data
        return redirect(url_for('search_leetcode', query=query))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
