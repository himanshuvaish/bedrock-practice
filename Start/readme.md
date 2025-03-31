
python inference-parameters.py "amazon.titan-text-express-v1" "Please write a haiku:"
python inference-parameters.py "mistral.mixtral-8x7b-instruct-v0:1" "Write a haiku:"
python inference-parameters.py "cohere.command-text-v14" "Write a haiku:"

python response-variable-temperature.py "Write a haiku about a long journey. Skip the preamble:" 0.0

python response-variable-temperature.py "Write a haiku about a long journey. Skip the preamble:" 1.0