def transform_name(name):
    if name is None:
        return "UNKNOWN"

    cleaned_name = name.strip()
    return cleaned_name.upper() if cleaned_name else "UNKNOWN"


print(transform_name(" retail sales "))
print(transform_name(""))
print(transform_name(None))