## Description
This conversion script is designed to convert vicuna datasets to a more alpaca-like format.
To be used with the trainer found here: https://github.com/oobabooga/text-generation-webui/wiki/Using-LoRAs#training-a-lora
This was designed to conform to SOME of the format from the conv_vicuna_v1_1 format from the FastChat Github repo (https://github.com/lm-sys/FastChat/blob/main/fastchat/conversation.py) while working within the format of Ooba's Trainer. Some liberties were taken on this format adaptation...

## Note about versions
3 Different versions. Not sure which is best. (B is probably the best for booga)
* Version A - My original Script 
* Version B - Most Closely Matches Ooba's Vicuna format here: https://github.com/oobabooga/text-generation-webui/blob/main/characters/instruction-following/Vicuna-v1.yaml
* Version C - Most Closely Matches Fastchat's Vicuna 1.1 format here: https://github.com/lm-sys/FastChat/blob/main/fastchat/conversation.py

**Make sure whatever version you pick matches the vicuna-format JSON**

## How to use Script
1. Convert vicuna json to alpaca format with `python format_B.py --input <path_to_vicuna_dataset>`
2. Copy the datasets folder to `text-generation-webui/training/datasets`
3. Copy the formats folder to `text-generation-webui/training/formats`

Still ~~Totally~~ Mostly Untested WIP

## Patch Training Data Logging
1. Copy the training_logData.diff file to "text-generation-webui/modules/"
2. Run command `patch training.py training_logData.diff`
3. Logs now sent to "text-generation-webui/logs/"

## Patch Training Token Pad
1. Copy the training_padHotFix.diff file to "text-generation-webui/modules/"
2. Run command `patch training.py training_padHotFix.diff`
3. Logs now sent to "text-generation-webui/logs/"
