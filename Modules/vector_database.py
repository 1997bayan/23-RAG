from multiprocessing import context

import chromadb 
from Modules.embedding import load_embedding_model


embedding_model = load_embedding_model()

def build_vector_database(chuncks):
    client = chromadb.Client()
    collection = client.get_or_create_collection("Course")
    embeddings = embedding_model.encode(chuncks)

    ids = [str(i) for i in range(len(chuncks))]

    try :
        collection.delete(ids=ids)
    except:
        pass

    collection.add(
        documents = chuncks,
        embeddings = embeddings.tolist(),
        ids = ids
    )

    return collection



def rwtrive_context(question , collection):
    question_embedding = embedding_model.encode([question])
    results = collection.query(
        query_embeddings = [question_embedding.tolist()],
        n_results = 3
    )

    context = (results["documents"][0])

    return "\n\n".join(context)