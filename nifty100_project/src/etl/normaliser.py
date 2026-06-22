import re


def normalize_year(value):

    if value is None:
        return None

    value = str(value)

    value = value.replace(".0","")

    match = re.search(r"\d{4}", value)

    if match:
        return int(match.group())

    return None



def normalize_ticker(value):

    if value is None:
        return None

    value = str(value)

    value = value.strip()

    value = value.upper()

    value = value.replace(" ", "")

    return value