import unittest
from python_hash.core import generate_hash_from_text, compare_hash_and_text

class TestHashFunctions(unittest.TestCase):
    def test_hash_generation(self):
        """Test that hash generation works correctly"""
        text = "password123"
        hashed = generate_hash_from_text(text)
        self.assertIsNotNone(hashed)
        self.assertNotEqual(text, hashed)
    
    def test_hash_comparison_match(self):
        """Test that hash comparison works for matching passwords"""
        text = "password123"
        hashed = generate_hash_from_text(text)
        self.assertTrue(compare_hash_and_text(hashed, text))
    
    def test_hash_comparison_no_match(self):
        """Test that hash comparison fails for non-matching passwords"""
        text1 = "password123"
        text2 = "password456"
        hashed = generate_hash_from_text(text1)
        self.assertFalse(compare_hash_and_text(hashed, text2))
    
    def test_hash_generation_empty_string(self):
        """Test hash generation with empty string"""
        with self.assertRaises(ValueError):
            generate_hash_from_text("")
    
    def test_hash_generation_invalid_input(self):
        """Test hash generation with None input"""
        with self.assertRaises(ValueError):
            generate_hash_from_text(None)
    
    def test_hash_comparison_invalid_hash(self):
        """Test hash comparison with invalid hash string"""
        with self.assertRaises(ValueError):
            compare_hash_and_text("invalid_hash", "password123")

if __name__ == "__main__":
    unittest.main()