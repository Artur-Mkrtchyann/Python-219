import random
import time

def create_file(filename):
    with open(filename, 'w') as f:
        for _ in range(100):
            numbers = [str(random.randint(1, 100)) for _ in range(20)]
            f.write(' '.join(numbers) + '\n')


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"function {func.__name__} is working {end - start:.4f} sec.")
        return result
    return wrapper


@measure_time
def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    result = []
    for line in lines:
        nums = map(int, line.split())
        filtered = filter(lambda x: x > 40, nums)
        result.append(' '.join(map(str, filtered)))

    with open(output_file, 'w') as f:
        f.write('\n'.join(result))


# generator
def file_generator(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield list(map(int, line.split()))


if __name__ == "__main__":
    input_filename = "random_numbers.txt"
    output_filename = "filtered_numbers.txt"
    create_file(input_filename)
    process_file(input_filename, output_filename)
    print("Fayly kardanq generatorov:")
    for nums in file_generator(output_filename):
        print(nums)
       
