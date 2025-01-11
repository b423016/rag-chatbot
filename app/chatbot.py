def chatbot_response(query: str, rag_pipeline):
    """
    Get chatbot response using the RAG pipeline.
    :param query: User query.
    :param rag_pipeline: RAG pipeline object.
    :return: Chatbot response.
    """
    response = rag_pipeline.run(query)
    return response
