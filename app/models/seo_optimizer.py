from collections import Counter
import re

def analyze_seo(content, target_keyword):
    """
    Analyze content for SEO metrics like keyword density and readability.
    
    :param content: Text content to analyze.
    :param target_keyword: The keyword to analyze for.
    :return: Analysis results as a dictionary.
    """
    # Count words
    words = re.findall(r'\w+', content.lower())
    word_count = len(words)
    
    # Keyword density
    keyword_count = Counter(words)[target_keyword.lower()]
    keyword_density = (keyword_count / word_count) * 100 if word_count else 0
    
    # Readability (basic Flesch-Kincaid formula)
    sentence_count = content.count('.') or 1
    avg_words_per_sentence = word_count / sentence_count
    syllable_count = sum([len(re.findall(r'[aeiouy]+', word)) for word in words])
    avg_syllables_per_word = syllable_count / word_count if word_count else 0
    readability = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
    
    return {
        'word_count': word_count,
        'keyword_count': keyword_count,
        'keyword_density': keyword_density,
        'readability_score': readability
    }

def suggest_improvements(content, target_keyword, ideal_keyword_count):
    """
    Suggest improvements to optimize SEO.
    
    :param content: Text content to analyze.
    :param target_keyword: The keyword to optimize for.
    :param ideal_keyword_count: Target count for the keyword.
    :return: Suggestions as a list.
    """
    analysis = analyze_seo(content, target_keyword)
    suggestions = []
    
    if analysis['keyword_count'] < ideal_keyword_count:
        suggestions.append(f"Consider using the keyword '{target_keyword}' at least {ideal_keyword_count - analysis['keyword_count']} more times.")
    
    if analysis['readability_score'] < 60:
        suggestions.append("Improve readability by shortening sentences or using simpler words.")
    
    return suggestions
