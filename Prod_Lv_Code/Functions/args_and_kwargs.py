## *args --> arbitary arguments
## **kwargs --> keyword arbitary arguments

"""
Used constantly in production for wrapper functions (logging, retry, auth) that need to pass arguments through without knowing the target function's 
signature.
"""

def call_api(endpoint, *args, timeout=30, **kwargs):
    # args -> positional extras, kwargs -> named extras (headers, params, etc.)
    print(endpoint, args, timeout, kwargs)

call_api("/users", 1, 2, timeout=10, auth="token123")
# /users (1, 2) 10 {'auth': 'token123'}