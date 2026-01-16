"""
Script to pre-download the sentence transformer model
Run this once when you have internet connection
"""
from sentence_transformers import SentenceTransformer

print("Downloading all-MiniLM-L6-v2 model...")
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    print("✅ Model downloaded successfully!")
    print(f"Model saved to cache. You can now use the app offline.")
    
    # Test the model
    test_embedding = model.encode("This is a test sentence")
    print(f"✅ Model test successful! Embedding dimension: {len(test_embedding)}")
except Exception as e:
    print(f"❌ Error downloading model: {str(e)}")
    print("Please check your internet connection and try again.")
