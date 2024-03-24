# 2. Return all possible letter combinations that an area code (3-digit number) could represent. 
# It's a standard telephone mapping where 1 and 0 doesn't map to a letter. 
import numpy as np


# LET_num = {2:"ABC", 3:"EFG", 4:"HIJ", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}

# def combinations(nums):
#     try: 
        
#         Lookup = {2:"ABC", 3:"EFG", 4:"HIJ", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
        
#         for key, value in Lookup:
#             return value
        
#         letters = []
#         for i in nums:
#             letters.append(Lookup[i])
            
            

def solution(nums):
    # Assuming nums is a string
    mapping = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ'
    }
    
    # Generating combinations of letters based on the input digits
    combos = [mapping[num] for num in nums]
    
    # Initializing results list with an empty string
    results = [""]
    
    # Iterating through each combination of letters
    for combo in combos:
        # Temporary list to store updated results        
        temp_results = []
        
        # Iterating through each result in the current results list        
        for result in results:
            # Iterating through each letter in the current combination
            for letter in combo:
                # Appending the combination of result and letter to the temporary results list                
                temp_results.append(result + letter)
        results = temp_results
    return results

print(solution("456"))
            

            
            

        
        
    # except Exception as e: 





