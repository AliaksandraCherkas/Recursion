def seq_sum(sequence) -> int:
    sum = 0
    for element in sequence:
        
        if isinstance(element,int):
            sum+=element
        
        else:
            sum += seq_sum(element)
        
    return sum

sequence = [1,2,3,[4,5, (6,7)]]

print(seq_sum(sequence))
