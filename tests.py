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


# from functools import wraps
# import platform
# import time
# # import asyncio
# import requests

# host = ""

# def timer(func):
#     @wraps(func)
#     async def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()  # Start the timer
#         result = await func(*args, **kwargs)  # Await the async function
#         end_time = time.perf_counter()  # Stop the timer
#         elapsed_time = end_time - start_time
#         print(f"Elapsed time: {elapsed_time} seconds")
#         return result
#     return wrapper

# @timer
# # async def getOs():
# def getOs():
#     """
#     Returns the name of the operating system.
    
#     Possible return values:
#     - 'Windows' : if the operating system is Windows
#     - 'Linux' : if the operating system is Linux
#     - 'Darwin' : if the operating system is macOS
#     - 'Java' : if running on a Java platform (e.g., Jython)
#     - 'Other' : for any other operating system or if platform is unknown
#     """
#     return platform.system()
#     # os_name =  platform.system()
    
#     # if os_name == 'Windows':
#     #     return 'Windows'
#     # elif os_name == 'Linux':
#     #     return 'Linux'
#     # elif os_name == 'Darwin':
#     #     return 'macOS'
#     # elif os_name == 'Java':
#     #     return 'Java'
#     # else:
#     #     return 'Other'

# @timer
# # async def testUsers(mainUrl):
# def testUsers(mainUrl):
#     print("default users (10):\n" + requests.get(f"{mainUrl}/users").content)
#     time.sleep(1)

#     # 30 times
#     print("testing without ?count=Num")
#     for wCount in range(1, 30 + 1):
#         wCountRes =  requests.get(f"{mainUrl}/users/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num")
#     for wiCount in range(1, 30 + 1):
#         wiCountRes =  requests.get(f"{mainUrl}/users/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

#     # 60 times
#     print("testing without ?count=Num\n60 times")
#     for wCount in range(1, 30 + 1):
#         wCountRes =  requests.get(f"{mainUrl}/users/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num\n60 times")
#     for wiCount in range(1, 30 + 1):
#         wiCountRes =  requests.get(f"{mainUrl}/users/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

# @timer
# # async def testProducts(mainUrl):
# def testProducts(mainUrl):
#     print("default products (10):\n" + requests.get(f"{mainUrl}/products").content)
#     time.sleep(1)

#     # 30 times
#     print("testing without ?count=Num")
#     for wCount in range(1, 30 + 1):
#         wCountRes = requests.get(f"{mainUrl}/products/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num")
#     for wiCount in range(1, 30 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/products/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

#     # 60 times
#     print("testing without ?count=Num\n60 times")
#     for wCount in range(1, 60 + 1):
#         wCountRes = requests.get(f"{mainUrl}/products/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num\n60 times")
#     for wiCount in range(1, 60 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/products/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

# @timer
# # async def testCompanies(mainUrl):
# def testCompanies(mainUrl):
#     print("default companies (10):\n" + requests.get(f"{mainUrl}/companies").content)
#     time.sleep(1)

#     # 30 times
#     print("testing without ?count=Num")
#     for wCount in range(1, 30 + 1):
#         wCountRes = requests.get(f"{mainUrl}/companies/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num")
#     for wiCount in range(1, 30 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/companies/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

#     # 60 times
#     print("testing without ?count=Num\n60 times")
#     for wCount in range(1, 60 + 1):
#         wCountRes = requests.get(f"{mainUrl}/companies/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num\n60 times")
#     for wiCount in range(1, 60 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/companies/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

# @timer
# # async def testCreditCards(mainUrl):
# def testCreditCards(mainUrl):
#     print("default credit-cards (10):\n" + requests.get(f"{mainUrl}/credit-cards").content)
#     time.sleep(1)

#     # 30 times
#     print("testing without ?count=Num")
#     for wCount in range(1, 30 + 1):
#         wCountRes = requests.get(f"{mainUrl}/credit-cards/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num")
#     for wiCount in range(1, 30 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/credit-cards/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

#     # 60 times
#     print("testing without ?count=Num\n60 times")
#     for wCount in range(1, 60 + 1):
#         wCountRes = requests.get(f"{mainUrl}/credit-cards/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num\n60 times")
#     for wiCount in range(1, 60 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/credit-cards/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

# @timer
# # async def testJobs(mainUrl):
# def testJobs(mainUrl):
#     print("default jobs (10):\n" + requests.get(f"{mainUrl}/jobs").content)
#     time.sleep(1)

#     # 30 times
#     print("testing without ?count=Num")
#     for wCount in range(1, 30 + 1):
#         wCountRes = requests.get(f"{mainUrl}/jobs/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num")
#     for wiCount in range(1, 30 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/jobs/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

#     # 60 times
#     print("testing without ?count=Num\n60 times")
#     for wCount in range(1, 60 + 1):
#         wCountRes = requests.get(f"{mainUrl}/jobs/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num\n60 times")
#     for wiCount in range(1, 60 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/jobs/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

# @timer
# # async def testTextContents(mainUrl):
# def testTextContents(mainUrl):
#     print("default text-contents (10):\n" + requests.get(f"{mainUrl}/text-contents").content)
#     time.sleep(1)

#     # 30 times
#     print("testing without ?count=Num")
#     for wCount in range(1, 30 + 1):
#         wCountRes = requests.get(f"{mainUrl}/text-contents/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num")
#     for wiCount in range(1, 30 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/text-contents/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)

#     # 60 times
#     print("testing without ?count=Num\n60 times")
#     for wCount in range(1, 60 + 1):
#         wCountRes = requests.get(f"{mainUrl}/text-contents/{wCount}")
#         print(f"test num: {wCount}\n{wCountRes.content}")
#         time.sleep(3)

#     print("testing with ?count=Num\n60 times")
#     for wiCount in range(1, 60 + 1):
#         wiCountRes = requests.get(f"{mainUrl}/text-contents/?count={wiCount}")
#         print(f"test num: {wiCount}\n{wiCountRes.content}")
#         time.sleep(3)


# def main(host):
#     print("Starting the program...")
#     time.sleep(1)

#     mainUrl = f"{host}:3000/api/"

#     testUsers(mainUrl)
#     testProducts(mainUrl)
#     testCompanies(mainUrl)
#     testCreditCards(mainUrl)
#     testJobs(mainUrl)
#     testTextContents(mainUrl)


#     # testUser        = asyncio.create_task(testUsers(mainUrl))
#     # testProduct     = asyncio.create_task(testProducts(mainUrl))
#     # testCompanie    = asyncio.create_task(testCompanies(mainUrl))
#     # testCreditCard  = asyncio.create_task(testCreditCards(mainUrl))
#     # testJob         = asyncio.create_task(testJobs(mainUrl))
#     # testTextContent = asyncio.create_task(testTextContents(mainUrl))

#     # await asyncio.gather(
#     #     testUser, 
#     #     testProduct,
#     #     testCompanie,
#     #     testCreditCard,
#     #     testJob,
#     #     testTextContent
#     # )

#     # results = await asyncio.gather(
#     #     testUsers(mainUrl),
#     #     testProducts(mainUrl),
#     #     testCompanies(mainUrl),
#     #     testCreditCards(mainUrl),
#     #     testJobs(mainUrl),
#     #     testTextContents(mainUrl),
#     # )

#     # print(results)

# if __name__ == "__main__":

#     # if getOs() == "Windows":
#     #     host = "localhost"

#     host = "127.0.0.1"

#     # asyncio.run(main(host))
#     main(host)