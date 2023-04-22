## Description
This conversion script is designed to convert vicuna datasets to a more alpaca-like format.
To be used with the trainer found here: https://github.com/oobabooga/text-generation-webui/wiki/Using-LoRAs#training-a-lora
This was designed to conform to SOME of the format from the conv_vicuna_v1_1 format from the FastChat Github repo (https://github.com/lm-sys/FastChat/blob/main/fastchat/conversation.py) while working within the format of Ooba's Trainer. Some liberties were taken on this format adaptation...

## Note on Conversation Length
Some of the conversations in the SparseGPT dataset are pretty long. This reason there are two versions created when you run the script:
"vicuna-short.json" Is more likely to work in training but does not include conversations over 1500 words
"vicuna-all.json" Includes ALL conversations within the original vicuna dataset regardless of length

*MAY BE ABLE TO USE CUTOFF LENGTH PARAMETER IN OOBA'S TRAINER*

## How to use Script
1. Convert vicuna json to alpaca format with `python vicuna_to_alpaca_format.py --input <path_to_vicuna_dataset>`
2. Copy the datasets folder to `text-generation-webui/training/datasets`
3. Copy the formats folder to `text-generation-webui/training/formats`

Still Totally Untested WIP
