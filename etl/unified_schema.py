# unified_schema.py
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
            "authors": item.get("authors"),
            "publication_date": item.get("publication_date"),
            "source": item.get("source"),
            # Add more mappings as needed
        }
        unified_data.append(mapped_item)
    return unified_data
