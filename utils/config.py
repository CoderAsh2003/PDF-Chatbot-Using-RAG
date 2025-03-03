
DEFAULT_EMBEDDING_MODEL = "ollama" #Sets default to OllamaEmbeddings

HUGGINGFACE_API_TOKEN  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx" #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


TEXT_SPLITTER_CONFIG =  {
    "chunk_size" : 1000,"chunk_overlap":100
}
#Configurations for each embedding model.
EMBEDDING_MODELS_CONFIG = {
    "openai": {
        "model": "text-embedding-3-small",
    },
    "huggingface": {
        "model_name": "sentence-transformers/all-mpnet-base-v2", #Remember to change model name as per wish
        "model_kwargs": {'device': 'cuda'},
        "encode_kwargs": {'normalize_embeddings': False}
    },
    "ollama": {
        "model": "llama3.2",
        "num_gpu": 1
    }
}