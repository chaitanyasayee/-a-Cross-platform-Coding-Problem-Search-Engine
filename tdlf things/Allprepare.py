import chardet

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

# Process Leetcode data
leetcode_data_filename = 'LCindex.txt'
leetcode_encoding = find_encoding(leetcode_data_filename)

with open(leetcode_data_filename, 'r', encoding=leetcode_encoding) as f:
    leetcode_lines = f.readlines()

# Process CodeChef data
codechef_data_filename = 'CCindex.txt'
codechef_encoding = find_encoding(codechef_data_filename)

with open(codechef_data_filename, 'r', encoding=codechef_encoding) as f:
    codechef_lines = f.readlines()

# Process Codeforces data
codeforces_data_filename = 'CFindex.txt'
codeforces_encoding = find_encoding(codeforces_data_filename)

with open(codeforces_data_filename, 'r', encoding=codeforces_encoding) as f:
    codeforces_lines = f.readlines()

def preprocess(document_text):
    # remove the leading numbers from the string, remove non-alphanumeric characters, make everything lowercase
    terms = [term.lower() for term in document_text.strip().split()[1:]]
    return terms

def process_data(lines):
    vocab = {}
    documents = []
    for index, line in enumerate(lines):
        tokens = preprocess(line)
        documents.append(tokens)
        tokens = set(tokens)
        for token in tokens:
            if token not in vocab:
                vocab[token] = 1
            else:
                vocab[token] += 1

    vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

    return vocab, documents

# Process Leetcode data
leetcode_vocab, leetcode_documents = process_data(leetcode_lines)

# Process CodeChef data
codechef_vocab, codechef_documents = process_data(codechef_lines)

# Process Codeforces data
codeforces_vocab, codeforces_documents = process_data(codeforces_lines)

# Save the vocabularies in separate text files
with open('Tf-Idf/leetcode_vocab.txt', 'w') as f:
    for key in leetcode_vocab.keys():
        f.write("%s\n" % key)

with open('Tf-Idf/codechef_vocab.txt', 'w') as f:
    for key in codechef_vocab.keys():
        f.write("%s\n" % key)

with open('Tf-Idf/codeforces_vocab.txt', 'w') as f:
    for key in codeforces_vocab.keys():
        f.write("%s\n" % key)
# save the idf values in a text file
with open('Tf-Idf/codeforces_idf-values.txt', 'w') as f:
    for key in codeforces_vocab.keys():
        f.write("%s\n" % codeforces_vocab[key])
with open('Tf-Idf/codechef_idf-values.txt', 'w') as f:
    for key in codechef_vocab.keys():
        f.write("%s\n" % codechef_vocab[key])
with open('Tf-Idf/leetcode_idf-values.txt', 'w') as f:
    for key in leetcode_vocab.keys():
        f.write("%s\n" % leetcode_vocab[key])

# Save the documents in separate text files
with open('Tf-Idf/leetcode_documents.txt', 'w') as f:
    for document in leetcode_documents:
        f.write("%s\n" % ' '.join(document))

with open('Tf-Idf/codechef_documents.txt', 'w') as f:
    for document in codechef_documents:
        f.write("%s\n" % ' '.join(document))

with open('Tf-Idf/codeforces_documents.txt', 'w') as f:
    for document in codeforces_documents:
        f.write("%s\n" % ' '.join(document))

def build_inverted_index(documents):
    inverted_index = {}
    for index, document in enumerate(documents):
        for token in document:
            if token not in inverted_index:
                inverted_index[token] = [index]
            else:
                inverted_index[token].append(index)

    return inverted_index

# Build the inverted index for each dataset
leetcode_inverted_index = build_inverted_index(leetcode_documents)
codechef_inverted_index = build_inverted_index(codechef_documents)
codeforces_inverted_index = build_inverted_index(codeforces_documents)

# Save the inverted indexes in separate text files
with open('Tf-Idf/leetcode_inverted_index.txt', 'w') as f:
    for key in leetcode_inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in leetcode_inverted_index[key]]))

with open('Tf-Idf/codechef_inverted_index.txt', 'w') as f:
    for key in codechef_inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in codechef_inverted_index[key]]))

with open('Tf-Idf/codeforces_inverted_index.txt', 'w') as f:
    for key in codeforces_inverted_index.keys():
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join([str(doc_id) for doc_id in codeforces_inverted_index[key]]))
