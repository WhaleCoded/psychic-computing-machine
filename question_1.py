import asyncio
import random


# Simulated data source
async def fetch_data(source_id: int) -> str:
    """
    Simulates fetching data from a source.
    Args:
        source_id (int): ID of the data source.
    Returns:
        str: The data fetched from the source (may include invalid data).
    """
    delay_time = random.randint(1, 5)
    await asyncio.sleep(delay_time)
    # Simulate occasional invalid data
    data = random.choice([f" data_from_source_{source_id} ", None, "", 42])
    print(f"Fetched from source {source_id}: {data}")
    return data


async def process_data_concurrently(sources):
    """
    Fetch, retry, clean, and process data from multiple sources concurrently.
    Args:
        sources (list of ints): A list where each int represents a new source.
        max_retries (int): Maximum number of retries allowed for each source.
    Returns:
        list of tuples: Processed data in the order sources finish, along with source ID.
    """

    pass


# Example input
sources = [i for i in range(1, 11)]  # List of source IDs

if __name__ == "__main__":
    processed_data = asyncio.run(process_data_concurrently(sources))
    print(processed_data)
