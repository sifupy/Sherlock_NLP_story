from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def main_view(request):
    return render(request,"main_app/main.html")
import spacy
# from gensim import corpora
# from gensim.models import LdaModel
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.decomposition import LatentDirichletAllocation
from django.shortcuts import render

# Load spaCy model for POS tagging and NER
nlp = spacy.load("en_core_web_sm")

# def topic_modeling(texts):
#     # Use CountVectorizer to prepare the text for topic modeling
#     vectorizer = CountVectorizer(stop_words='english')
#     X = vectorizer.fit_transform(texts)
    
#     lda = LatentDirichletAllocation(n_components=1, random_state=42)
#     lda.fit(X)
    
#     # Get the topics
#     terms = vectorizer.get_feature_names_out()
#     topic_keywords = [terms[i] for i in lda.components_[0].argsort()[-5:]]
    
#     return ', '.join(topic_keywords)

import spacy
from django.shortcuts import render
from django.http import HttpResponse
from spacy import displacy
import joblib
import os

# Load spaCy model for POS tagging and NER
nlp = spacy.load("en_core_web_sm")
base_dir = os.path.dirname(os.path.abspath(__file__))
vectorizer_path = os.path.join(base_dir, 'models', 'vectorizer.joblib')
lda_model_path = os.path.join(base_dir, 'models', 'lda_model.joblib')

vectorizer = joblib.load(vectorizer_path)
lda_model = joblib.load(lda_model_path)
def get_top_topics(doc_vector, top_n=3):
    topic_probs = lda_model.transform(doc_vector)[0]
    top_topics = topic_probs.argsort()[-top_n:][::-1]
    return {f"Topic_{topic_id+1}": round(topic_probs[topic_id] * 100, 2) for topic_id in top_topics}
def second_view(request):
    result = None  # Initialize result variable
    pos_tags = None  # Initialize POS tags variable
    ner_entities = None  # Initialize NER entities variable
    parse_tree_html = None  # Initialize parse tree HTML variable
    
    if request.method == 'POST':
        text_input = request.POST.get('text', '')
        uploaded_file = request.FILES.get('file')

        if uploaded_file:
            text = uploaded_file.read().decode('utf-8')
        else:
            text = text_input

        # Perform POS tagging using spaCy
        doc = nlp(text)
        pos_tags = [(token.text, token.pos_) for token in doc]

        # Perform NER using spaCy
        ner_entities = [(ent.text, ent.label_) for ent in doc.ents]

        # Render the parsing tree using displaCy
        parse_tree_html = displacy.render(doc, style='dep', page=True)
        doc_vector = vectorizer.transform([text])

        # Get the top topics
        top_topics = get_top_topics(doc_vector)

        # Set the result to be displayed
        result = {
            'text': text,
            'pos_tags': pos_tags,
            'ner_entities': ner_entities,
            'parse_tree_html': parse_tree_html,
            'top_topics': top_topics,
        }
    
    return render(request, 'main_app/computer.html', {'result': result})
