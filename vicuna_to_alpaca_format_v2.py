import argparse
import json
import os

def convert_format(old_data):
    new_data = []
    for item in old_data:
        new_conversation = ""
        for message in item['conversations']:
            if message['from'] == 'human':
                new_conversation += 'USER: ' + message['value'] + '\n'
            elif message['from'] == 'gpt':
                new_conversation += 'ASSISTANT: ' + message['value'] + '</s>\n'

        new_data.append({
            'conversation': new_conversation.strip()
        })

    return new_data

def filter_conversations(new_data):
    filtered_data = []

    for item in new_data:
        if '<s>' not in item['conversation'] and '</s>' not in item['conversation']:
            filtered_data.append(item)

    return filtered_data

def main():
    parser = argparse.ArgumentParser(description="Convert JSON dataset from old format to new format.")
    parser.add_argument('--input', type=str, required=True, help='Path to the input JSON file in old format.')

    args = parser.parse_args()

    with open(args.input, 'r') as input_file:
        old_data = json.load(input_file)

    new_data = convert_format(old_data)
    filtered_data = filter_conversations(new_data)

    os.makedirs('datasets', exist_ok=True)

    with open(os.path.join('datasets', 'vicuna_data.json'), 'w') as all_output_file:
        json.dump(filtered_data, all_output_file, indent=2)

if __name__ == "__main__":
    main()
