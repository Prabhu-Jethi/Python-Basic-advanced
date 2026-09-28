# WRONG — the list is created ONCE at function definition time
def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

add_item("a")  # ['a']
add_item("b")  # ['a', 'b']  <-- bug, not a fresh list

# CORRECT
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket