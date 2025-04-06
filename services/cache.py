from functools import lru_cache
import hashlib

class CacheManager:
    @staticmethod
    def generate_key(*args):
        """Generate consistent cache key from arguments"""
        return hashlib.md5(str(args).encode()).hexdigest()
    
    @classmethod
    def cached_query(cls, func):
        """Decorator for caching query results"""
        @lru_cache(maxsize=100)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper