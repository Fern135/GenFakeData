// Max requests a single IP can make within a 1-second sliding window
const RATE_LIMIT = 10;

// In-memory store: maps each IP to an array of request timestamps (ms)
const requests = {};

function getIp(req) {
    // Prefer X-Forwarded-For so clients behind a proxy get their real IP
    const forwarded = req.headers['x-forwarded-for'];
    if (forwarded) return forwarded.split(',')[0].trim();
    return req.socket.remoteAddress || 'unknown';
}

function rateLimitMiddleware(req, res, next) {
    const ip = getIp(req);
    const now = Date.now();

    // Only keep timestamps within the last 1 second (sliding window)
    const windowStart = now - 1000;
    const timestamps = (requests[ip] || []).filter(t => t > windowStart);

    if (timestamps.length >= RATE_LIMIT) {
        // IP has hit the limit — reject with 429 Too Many Requests
        return res.status(429).json({
            error: 'rate limit exceeded',
            limit: RATE_LIMIT,
            window: '1s',
        });
    }

    // Record this request and update the store
    timestamps.push(now);
    requests[ip] = timestamps;

    next();
}

module.exports = rateLimitMiddleware;
