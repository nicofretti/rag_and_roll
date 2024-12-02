from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.readers.web import SimpleWebPageReader
from rich import print as rprint
from llama_index.core.schema import MetadataMode
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core.schema import Document


def clean_metadata(doc):
    doc.excluded_llm_metadata_keys = ["Header_1", "Header_2", "Header_3"]
    return doc


if __name__ == "__main__":
    documents = SimpleWebPageReader(html_to_text=True).load_data(
        [
            "https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/modules/"
        ]
    )
    # apply on documents
    documents = list(map(clean_metadata, documents))

    parser = MarkdownNodeParser()
    nodes = parser.get_nodes_from_documents(documents)

    documents_filtered = []
    for doc in documents:
        if "Header_3" not in doc.metadata:
            documents_filtered.append(doc)
