import asyncio
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "http://127.0.0.1:8000"
TIMEOUT = 60

routes = [
    "/api/users",
    "/api/products",
    "/api/companies",
    "/api/credit-cards",
    "/api/jobs",
    "/api/text-contents",
]


def fetch(route, count):
    url = f"{BASE_URL}{route}/{count}/"
    start = time.perf_counter()
    try:
        with urllib.request.urlopen(url, timeout=TIMEOUT) as res:
            elapsed = time.perf_counter() - start
            return elapsed, res.status
    except Exception as e:
        elapsed = time.perf_counter() - start
        return elapsed, str(e)


async def main():
    count = 10
    multiplier = 2
    loop = asyncio.get_event_loop()

    with ThreadPoolExecutor() as pool:
        while True:
            print(f"\n--- count: {count} ---")

            tasks = [
                loop.run_in_executor(pool, fetch, route, count)
                for route in routes
            ]
            results = await asyncio.gather(*tasks)

            stop = False
            for route, (elapsed, status) in zip(routes, results):
                print(f"{route}/{count} → {status} in {elapsed:.2f}s")
                if elapsed > TIMEOUT:
                    print(f"Stopped: took longer than {TIMEOUT}s at count={count}")
                    stop = True

            if stop:
                break

            count = int(count * multiplier)


if __name__ == "__main__":
    asyncio.run(main())
