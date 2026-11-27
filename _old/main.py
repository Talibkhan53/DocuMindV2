from pathlib import Path

from FileLoaders.main_loader import MainLoader
from Chunking.chunking import Chunking
from Embeddings.embedding import Embedding
from Storage.vector_store import VectorStore
from Retreiver.retriever import Retreiver
from ContextBuilder.context_builder import ContextBuilder
from Prompt.prompt import PromptBuilder
from AI.Engine import AIEngine


# 1. Get document path

file_directory = input("\nEnter directory path: ").strip()
file_name = input("Enter file name: ").strip()

file_path = Path(file_directory) / file_name


# 2. Validate and load document

if not file_path.is_file():
    print("Error: File not found in that directory.")
    exit()


try:
    loader = MainLoader.get_loader(file_path)

    if not loader.validate_file(file_path):
        print("Error: Invalid or unsupported file.")
        exit()

    content = loader.read_file(file_path)

except Exception as e:
    print(f"Error while loading document: {e}")
    exit()


print("\nDocument loaded successfully.")


# 3. Chunk document

chunker = Chunking()

# Chunking happens here
chunks = chunker.sliding_window_chunk(content)

print(f"Chunks created: {len(chunks)}")


# 4. Create embeddings

embedder = Embedding()

# Embedding happens here
document_embeddings = embedder.embed_document_chunk(chunks)

print("Embeddings created.")


# 5. Store chunks and embeddings

vector_store = VectorStore()

for chunk, embedding in zip(chunks, document_embeddings):
    vector_store.add(chunk, embedding)

print("Document stored successfully.")


# 6. Create retriever

retriever = Retreiver(
    embedder=embedder,
    vector_store=vector_store
)


# 7. Select operation

print("\nChoose an option:")
print("1. Summarize Document")
print("2. Chat with Document")

choice = input("Enter your choice: ").strip()


# 8. Create AI engine

ai_engine = AIEngine()


# 9. Summarize document

if choice == "1":

    print("\nGenerating document summary...")

    answer = ai_engine.Summarize_document(chunks)


# 10. Chat with document

elif choice == "2":

    query = input("\nEnter your question: ").strip()

    # Retrieve the most relevant chunks
    results = retriever.retreive(query)

    print("\nRelevant context retrieved.")

    # Build context from retrieved chunks
    context_builder = ContextBuilder()

    context = context_builder.build(results)

    # Build prompt
    prompt_builder = PromptBuilder()

    prompt = prompt_builder.build(
        query,
        context
    )

    # Generate answer
    answer = ai_engine.generate(prompt)


else:

    print("Invalid choice.")
    exit()


# 11. Display result

print("\n" + "=" * 60)
print(answer)
print("=" * 60)