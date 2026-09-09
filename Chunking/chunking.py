class Chunking:

    # Split a document into overlapping chunks
    def sliding_window_chunk(
        self,
        text,
        chunk_size=150,
        overlap=30
    ):

        # Return an empty list when the document has no content
        if not text or not text.strip():
            return []

        # Prevent an invalid sliding-window configuration
        if overlap >= chunk_size:
            raise ValueError(
                "Overlap must be smaller than chunk size."
            )

        # Split the document into individual words
        words = text.split()

        # Store the generated chunks
        chunks = []

        # Calculate how far the window moves after each chunk
        step = chunk_size - overlap

        # Create chunks using a sliding window
        for start in range(
            0,
            len(words),
            step
        ):

            # Select the words belonging to the current chunk
            chunk_words = words[
                start:start + chunk_size
            ]

            # Stop if there are no words left
            if not chunk_words:
                break

            # Convert the words back into a text chunk
            chunk = " ".join(chunk_words)

            # Store the chunk
            chunks.append(chunk)

            # Stop when the end of the document is reached
            if start + chunk_size >= len(words):
                break

        # Return all document chunks
        return chunks