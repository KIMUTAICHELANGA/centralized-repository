def map_to_unified_schema(data):
    """
    Map incoming data to a unified schema for storage.

    :param data: Raw data from the source.
    :return: Data mapped to the unified schema.
    """
    unified_data = []
    for item in data:
        mapped_item = {
            "title": item.get("title"),
            "authors": item.get("authors", []),  # Default to empty list if no authors
            "publication_date": item.get("publication_date"),
            "source": item.get("source"),
            "type": item.get("type"),  # Type of content (e.g., article, report, etc.)
            "content": item.get("content"),  # Main content of the publication
            "keywords": item.get("keywords", []),  # Keywords for categorization
            "abstract": item.get("abstract"),  # Summary of the content
            "tags": item.get("tags", []),  # Tags for further categorization
            "created_at": item.get("created_at"),  # Creation date
            "updated_at": item.get("updated_at"),  # Last update date
            "expert_id": item.get("expert_id"),  # ID of the associated expert
            "feedback": item.get("feedback", []),  # User feedback related to the content
            "usage_count": item.get("usage_count", 0)  # Count of how often this item has been accessed
        }
        unified_data.append(mapped_item)
    return unified_data
