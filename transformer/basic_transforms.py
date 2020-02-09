import hashlib

import core


@core.function_annotation(**{
    "description": "Create a unique value with 'b_hash' key based on record.values()"
})
def apply_hash(record, transform):
    hash_keys = transform.get("hash_key_list") or sorted(record.keys())
    hash_values = [record[k] for k in hash_keys]
    m = hashlib.sha256()
    m.update("".join(hash_values))
    record["b_hash"] = m.digest().encode()
