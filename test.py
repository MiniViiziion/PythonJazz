import numpy as np
import os

# Load base data and weight data as numpy arrays
base_data = np.loadtxt('test_packet_base.txt')
weight_data = np.loadtxt('test_packet_weight.txt')

# Reshape base data into a 2D array of 4096 arrays of 8 values
chunked_data = base_data.reshape((-1, 4))

# Multiply base data by weight data 
weighted_data = base_data * weight_data

# Reshape weighted data into a 2D array of 4096 arrays of 8 values
chunked_weighted_data = weighted_data.reshape((-1, 4))

# Calculate the result for each chunk the min,max, and mean
chunk_results = []
for chunk in chunked_weighted_data:
    chunk_min = np.min(chunk)
    chunk_max = np.max(chunk)
    chunk_mean = np.mean(chunk)
    chunk_result = (chunk_max - chunk_mean) * chunk_min
    chunk_results.append(chunk_result)

# Calculate the final answer
final_result = int(np.floor(np.sum(chunk_results)) % 4096)

# Check the test_answers file
dirname = os.path.dirname(__file__)
answer_dir = os.path.join(dirname, 'test_answers')
with open(os.path.join(answer_dir, f'{final_result}'), 'r') as f:
    answer = f.read().strip()

if answer == 'correct':
    print(f'Congratulations! Your deactivation key is {final_result}.')
else:
    print(f'Sorry, your deactivation key is incorrect. Please try again.')
