import json
import tkinter as tk
from tkinter import filedialog

def process_json(json_data):
    result = []

    def process_dict(d, depth=0):
        for key, value in d.items():
            if isinstance(value, dict):
                result.append(f"{'  ' * depth}{key}:")
                process_dict(value, depth + 1)
            elif isinstance(value, list):
                result.append(f"{'  ' * depth}{key}:")
                process_list(value, depth + 1)
            else:
                result.append(f"{'  ' * depth}{key}: {value}")

    def process_list(l, depth=0):
        for item in l:
            if isinstance(item, dict):
                process_dict(item, depth)
            elif isinstance(item, list):
                process_list(item, depth)
            else:
                result.append(f"{'  ' * depth}{item}")

    if isinstance(json_data, dict):
        process_dict(json_data)
    elif isinstance(json_data, list):
        process_list(json_data)

    return "\n".join(result)

def main():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])

    if not file_path:
        print("No file selected.")
        return

    with open(file_path, "r") as f:
        data = json.load(f)

    output = process_json(data)

    output_file_path = file_path.replace(".json", "_formatted.txt")
    with open(output_file_path, "w") as f:
        f.write(output)

    print(f"Formatted JSON saved to: {output_file_path}")

if __name__ == "__main__":
    main()
