import time
import threading
from django.http import JsonResponse

# Max requests a single IP can make within a 1-second window
RATE_LIMIT = 10

# Lock to prevent race conditions when multiple workers read/write _requests
_lock = threading.Lock()

# In-memory store: maps each IP to a list of request timestamps
_requests: dict[str, list[float]] = {}


def _get_ip(request) -> str:
    # Prefer X-Forwarded-For so clients behind a proxy/load balancer get their real IP
    forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR", "unknown")


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = _get_ip(request)
        now = time.monotonic()

        # Only keep timestamps within the last 1 second (sliding window)
        window_start = now - 1.0

        with _lock:
            timestamps = _requests.get(ip, [])

            # Drop timestamps outside the current window
            timestamps = [t for t in timestamps if t > window_start]

            if len(timestamps) >= RATE_LIMIT:
                # IP has hit the limit — reject with 429 Too Many Requests
                return JsonResponse(
                    {"error": "rate limit exceeded", "limit": RATE_LIMIT, "window": "1s"},
                    status=429,
                )

            # Record this request and update the store
            timestamps.append(now)
            _requests[ip] = timestamps

        return self.get_response(request)
