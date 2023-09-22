def transform(legacy_data):
    return {n.lower(): k for k, v in legacy_data.items() for n in v}
