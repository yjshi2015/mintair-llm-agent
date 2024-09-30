import json
import sys
import os

def extract_markdown(input_filepath, output_filepath):
    """
    Extract the markdown content under the data node in the JSON file, retain the original format, and save it to the specified file.

    Args:
    input_filepath: The path of the JSON file.
    output_filepath: The path of the output MD file.

    Returns:
    None. If an error occurs, print the error message.
    """
    if not os.path.exists(input_filepath):
        print(f"Error: Input file '{input_filepath}' not found.")
        return

    try:
        with open(input_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{input_filepath}'.")
        return

    if not data.get("success") or data.get("data") is None:
        print(f"Error: No 'data' node found or request failed in '{input_filepath}'.")
        return

    markdown_content = ""
    for item in data["data"]:
        markdown_content += item["markdown"] + "\n\n"  # 保留原始格式，节点间添加两行空行


    try:
        with open(output_filepath, "w", encoding='utf-8') as outfile:
            outfile.write(markdown_content)
        print(f"Markdown content extracted and saved to '{output_filepath}'")
    except Exception as e:
        print(f"Error writing to output file: {e}")



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <input_filepath> <output_filepath>")
        sys.exit(1)

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    extract_markdown(input_filepath, output_filepath)