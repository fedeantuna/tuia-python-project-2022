def average(summatory: float, quantity: int) -> float:
    average = round(summatory / quantity , 2)
    return average

def normalize_str(str: str) -> str:
    return str.upper().replace(' ', '_').replace('/', '_')