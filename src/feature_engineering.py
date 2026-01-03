import hashlib


def hash_feature(value: str, num_buckets: int = 1000) -> int
    """
    Stable hashing (same input -> same bucket).
    """
    h = hashlib.md5(value.encode("utf-8")).hexdigest()
    return int(h, 16) % num_buckets
