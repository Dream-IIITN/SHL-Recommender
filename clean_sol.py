import pandas as pd
import hashlib

def clean_dataset(input_path: str, output_path: str) -> pd.DataFrame:
    """Clean and deduplicate the SHL dataset"""
    df = pd.read_csv(input_path)
    
    # 1. Remove exact duplicates
    df = df.drop_duplicates(subset=['url', 'title', 'description'], keep='first')
    
    # 2. Generate content-based hash for duplicate detection
    df['content_hash'] = df.apply(
        lambda x: hashlib.md5(
            f"{x['title']}{x['description']}{x['job_level']}".encode()
        ).hexdigest(),
        axis=1
    )
    
    # 3. Remove content duplicates (different URLs but same content)
    df = df.drop_duplicates(subset=['content_hash'], keep='first')
    
    # 4. Clean problematic URLs
    df['url'] = df['url'].str.strip().str.lower()
    
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    clean_dataset("shl_solutions.csv", "shl_solutions_clean.csv")