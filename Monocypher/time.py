import re

def parse_time_to_seconds(time_str):
    """Convert a time string like '1.47s' to float seconds."""
    return float(time_str.strip('s'))

def average_time_output(file_path):
    time_data = {
        'real': [],
        'user': [],
        'sys': [],
        'cpu': []
    }

    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    for i in range(0, len(lines), 4):
        real_line = lines[i]
        user_line = lines[i + 1]
        sys_line = lines[i + 2]
        cpu_line = lines[i + 3]

        time_data['real'].append(parse_time_to_seconds(real_line.split()[1]))
        time_data['user'].append(parse_time_to_seconds(user_line.split()[1]))
        time_data['sys'].append(parse_time_to_seconds(sys_line.split()[1]))
        time_data['cpu'].append(int(cpu_line.split()[1].strip('%')))

    print("Average times across all runs:")
    for key, values in time_data.items():
        avg = sum(values) / len(values)
        unit = "s" if key != "cpu" else "%"
        print(f"{key}: {avg:.2f}{unit}")

# Example usage
if __name__ == "__main__":
    print("for unmodded times")
    file_path = "regular_times.txt"  # Replace with your actual file path
    average_time_output(file_path)

    print("for modded times")
    file_path = "modded_times.txt"  # Replace with your actual file path
    average_time_output(file_path)

