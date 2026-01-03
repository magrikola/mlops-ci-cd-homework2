from src.feature_engineering import hash_feature

def test_feature_with_file_system(tmp_path):
    p = tmp_path / "input.txt"
    p.write_text("from_file")

    value = p.read_text()
    out = hash_feature(value, 100)

    assert isinstance(out, int)
    assert 0 <= out < 100
