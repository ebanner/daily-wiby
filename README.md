# daily-s3-cache

Caches daily links for changing (dynamic) resources

## Explanation

Any daily link which comes from an API is dynamic and may change from call to call. We want the same result to come back for a given day

So we check to see if today's link is already in the cache. If it is, just return that. Else, hit then API and cache it
