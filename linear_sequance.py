from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    if not sequence:
        return []
    if isinstance(sequence[0],int):
        return list(sequence[0:1]) +linear_seq(sequence[1:])
    return linear_seq(sequence[0]) + linear_seq(sequence[1:])
    
    


sequence = [1,2,3,[(4,5), (6,7)]]

print(linear_seq(sequence))
