
import chromadb
import hashlib
from chromadb.utils import embedding_functions
from typing import Dict, List, Optional

class ChromaManager:
    def __init__(self, persist_dir: str = "chroma_db"):
        self.client = chromadb.PersistentClient(path=persist_dir)
        self.embedding_function = embedding_functions.DefaultEmbeddingFunction()
    
    def _generate_unique_id(self, input_str: str, prefix: str = "") -> str:
        """Generate unique ID using hash of input string"""
        return f"{prefix}{hashlib.md5(input_str.encode()).hexdigest()}"
    
    def get_collection(self, name: str):
        """Get or create a ChromaDB collection"""
        try:
            return self.client.get_collection(
                name=name,
                embedding_function=self.embedding_function
            )
        except:
            return self.client.create_collection(
                name=name,
                embedding_function=self.embedding_function
            )
    
    def add_documents(self, collection_name: str, documents: List[str], metadatas: List[Dict], source_urls: List[str]):
        """Add documents with automatic deduplication"""
        collection = self.get_collection(collection_name)
        
        # Generate unique IDs based on content + metadata
        ids = [self._generate_unique_id(f"{doc}{meta}") for doc, meta in zip(documents, metadatas)]
        
        # Check for existing documents
        existing = collection.get(ids=ids)
        if existing and len(existing['ids']) > 0:
            # Update existing documents instead of adding duplicates
            collection.update(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )
        else:
            # Add new documents
            collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )
    
    def query_collection(self, collection_name: str, query: str, filters: Optional[Dict] = None, n_results: int = 3):
        """Query a ChromaDB collection"""
        collection = self.get_collection(collection_name)
        return collection.query(
            query_texts=[query],
            n_results=n_results,
            where=filters
        )