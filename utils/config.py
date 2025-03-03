
DEFAULT_EMBEDDING_MODEL = "ollama" #Sets default to OllamaEmbeddings

HUGGINGFACE_API_TOKEN  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx" #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

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