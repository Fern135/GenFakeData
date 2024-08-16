import asyncio
import requests
import time

# Define the base URL and default port
BASE_URL = "http://127.0.0.1:80/api/"

endpoints = [
    "users",
    "products",
    "companies",
    "credit-cards",
    "jobs",
    "text-contents"
]

def fetch(url):
    """Fetch a URL and return the response."""
    response = requests.get(url)
    return response.text  # Use response.text as a property, not as a callable

async def run_requests(num_requests, urls, label):
    """Run a set of requests and measure the time taken."""
    start_time = time.perf_counter()
    
    loop = asyncio.get_event_loop()
    tasks = [loop.run_in_executor(None, fetch, url) for url in urls]
    await asyncio.gather(*tasks)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    # print(f"Time taken for {num_requests} requests with {label}\t {elapsed_time:.2f} seconds")
    print(f"Time taken for {num_requests} --------------------> {elapsed_time:.2f} seconds")


def generate_urls(base_url, endpoint, count, num_requests):
    """Generate URLs for requests with and without count."""
    urls = []
    for _ in range(num_requests):
        urls.append(f"{base_url}{endpoint}?count={count}")
        urls.append(f"{base_url}{endpoint}/{count}")
    return urls


async def main():
    counts = [10, 30, 60]  
    
    tasks = []
    for count in counts:
        num_requests = count
        
        for endpoint in endpoints:
            urls_with_count = generate_urls(BASE_URL, endpoint, 10, num_requests)
            urls_without_count = generate_urls(BASE_URL, endpoint, '', num_requests)
            
            tasks.append(run_requests(num_requests, urls_with_count, f"{endpoint} with '?count=10'"))
            tasks.append(run_requests(num_requests, urls_without_count, f"{endpoint} without '?count=10'"))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
