from src.feature_engineering import hash_feature

def test_hash_feature_is_stable():
    assert hash_feature("user_123", 10) == hash_feature("user_123", 10)

def test_hash_feature_bucket_range():
    b = hash_feature("abc", 10)
    assert 0 <= b < 10
