import unittest
from app.models.seo_optimizer import analyze_seo, suggest_improvements

class TestSEO(unittest.TestCase):
    def test_analyze_seo(self):
        content = "AI is transforming healthcare."
        keyword = "AI"
        result = analyze_seo(content, keyword)
        self.assertEqual(result['keyword_count'], 1)
        self.assertAlmostEqual(result['keyword_density'], 16.67, places=2)

    def test_suggest_improvements(self):
        content = "AI is transforming healthcare."
        keyword = "AI"
        suggestions = suggest_improvements(content, keyword, 3)
        self.assertIn("Consider using the keyword 'AI' at least 2 more times.", suggestions)
