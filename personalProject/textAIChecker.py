import re
import nltk
import numpy as np
from collections import Counter
from wordfreq import zipf_frequency
from math import log2

nltk.download('punkt')

#######################################
# TOKENIZATION
#######################################

def tokenize_words(text):
    words = nltk.word_tokenize(text.lower())
    words = [w for w in words if re.match(r"[a-zA-Z']+", w)]
    return words

def tokenize_sentences(text):
    return nltk.sent_tokenize(text)

#######################################
# METRICS
#######################################

def type_token_ratio(words):
    return len(set(words)) / len(words) if words else 0

def comma_ratio(text, total_words):
    return text.count(",") / total_words if total_words else 0

def rare_word_ratio(words, threshold=3):
    rare = sum(1 for w in words if zipf_frequency(w, 'en') < threshold)
    return rare / len(words) if words else 0

def avg_sentence_length(sentences):
    lengths = [len(tokenize_words(s)) for s in sentences]
    return np.mean(lengths) if lengths else 0

def sentence_variance(sentences):
    lengths = [len(tokenize_words(s)) for s in sentences]
    return np.var(lengths) if lengths else 0

def burstiness(sentences):
    lengths = [len(tokenize_words(s)) for s in sentences]
    if len(lengths) < 2:
        return 0
    mean = np.mean(lengths)
    std = np.std(lengths)
    return std / mean if mean else 0

def lexical_entropy(words):
    freq = Counter(words)
    total = len(words)

    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)

    return entropy

#######################################
# INTERPRETATION LAYER
#######################################

def interpret_ttr(ttr):
    if ttr < 0.4:
        return "Low vocabulary diversity"
    elif ttr < 0.6:
        return "Moderate vocabulary diversity"
    else:
        return "High vocabulary diversity"

def interpret_burstiness(b):
    if b < 0.15:
        return "Very uniform sentence length"
    elif b < 0.3:
        return "Moderate variation"
    else:
        return "High variation in sentence length"

def interpret_entropy(e):
    if e < 4:
        return "Low lexical randomness"
    elif e < 6:
        return "Moderate lexical variation"
    else:
        return "High lexical randomness"

def interpret_rare(r):
    if r < 0.02:
        return "Very common vocabulary"
    elif r < 0.06:
        return "Balanced vocabulary"
    else:
        return "Uncommon vocabulary usage"

#######################################
# MAIN ANALYSIS
#######################################

def analyze_text(text):

    words = tokenize_words(text)
    sentences = tokenize_sentences(text)

    metrics = {}

    metrics["total_words"] = len(words)
    metrics["sentences"] = len(sentences)

    metrics["type_token_ratio"] = type_token_ratio(words)
    metrics["rare_word_ratio"] = rare_word_ratio(words)
    metrics["comma_ratio"] = comma_ratio(text, len(words))
    metrics["avg_sentence_length"] = avg_sentence_length(sentences)
    metrics["sentence_variance"] = sentence_variance(sentences)
    metrics["burstiness"] = burstiness(sentences)
    metrics["lexical_entropy"] = lexical_entropy(words)

    ###################################
    # INTERPRETATION
    ###################################

    interpretation = {
        "TTR_meaning": interpret_ttr(metrics["type_token_ratio"]),
        "burstiness_meaning": interpret_burstiness(metrics["burstiness"]),
        "entropy_meaning": interpret_entropy(metrics["lexical_entropy"]),
        "rare_word_meaning": interpret_rare(metrics["rare_word_ratio"])
    }

    return metrics, interpretation


#######################################
# TEST
#######################################

if __name__ == "__main__":

    text = """
    Paste your essay here. This analyzer will compute stylometric
    metrics and give human readable explanations.
    """

    metrics, meaning = analyze_text(text)

    print("\n=== NUMERICAL METRICS ===")
    for k,v in metrics.items():
        print(k, ":", v)

    print("\n=== INTERPRETATION ===")
    for k,v in meaning.items():
        print(k, ":", v)