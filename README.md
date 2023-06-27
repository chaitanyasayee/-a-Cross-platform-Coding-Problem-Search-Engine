# Algozenith Coding Problem Search Engine

The modern world demands individuals to equip themselves with coding skills. Algozenith, as an educational platform, assists learners on this journey by providing them with relevant coding problems to enhance their skills. However, with the plethora of coding platforms available, such as LeetCode, CodeChef, and Codeforces, navigating through the sea of coding problems can be daunting. The task at hand is to simplify this process by developing an efficient search engine.

## Installation

1. Clone the repository:

   git clone https://github.com/chaitanyasayee/-a-Cross-platform-Coding-Problem-Search-Engine.git
 

2. Install the required dependencies:

   
   pip install python
   pip install flask
  
  

3. Download the necessary data files for each coding platform. The files include:

   - `leetcode_vocab.txt`: Vocabulary file for LeetCode problems.
   - `leetcode_documents.txt`: Document file for LeetCode problems.
   - `leetcode_inverted_index.txt`: Inverted index file for LeetCode problems.
   - `LCQindex.txt`: Question links file for LeetCode problems.
   - `codeforces_vocab.txt`: Vocabulary file for Codeforces problems.
   - `codeforces_documents.txt`: Document file for Codeforces problems.
   - `codeforces_inverted_index.txt`: Inverted index file for Codeforces problems.
   - `CFQindex.txt`: Question links file for Codeforces problems.
   - `codechef_vocab.txt`: Vocabulary file for CodeChef problems.
   - `codechef_documents.txt`: Document file for CodeChef problems.
   - `codechef_inverted_index.txt`: Inverted index file for CodeChef problems.
   - `CCQindex.txt`: Question links file for CodeChef problems.

4. Start the Flask server:

   
   python app.py
   
5. Open your web browser and access `http://localhost:5000` to use the coding problem search engine.

## Usage

1. Enter your search query in the search bar.
2. Click on the corresponding button to search for problems in a specific coding platform: LeetCode, Codeforces, or CodeChef.
3. The search results will be displayed below, showing the links to the matching coding problems.

## Development

The coding problem search engine is built using Flask, Python, and web scraping techniques. The main components of the codebase are as follows:

- `app.py`: The main Flask application file that handles the routes and search functionality.
- `vocab.py`: Contains functions to load the vocabulary and IDF values from files.
- `documents.py`: Contains functions to load the document texts from files.
- `inverted_index.py`: Contains functions to load the inverted index from a file.
- `link_of_qs.py`: Contains functions to load the question links from a file.
- `utils.py`: Contains utility functions for calculating TF-IDF values and sorting documents based on relevance.
- `forms.py`: Defines the `SearchForm` class for the search form in the web interface.
- `templates/index.html`: HTML template file for the main search page.
- `static/main.js`: JavaScript file for handling the search form submission.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
