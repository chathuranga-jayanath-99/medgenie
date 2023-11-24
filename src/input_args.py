from typing import Optional
from dataclasses import dataclass, field
from transformers import HfArgumentParser

# Define and parse arguments.
@dataclass
class ScriptArguments:
   
    model_name: Optional[str] = field(default="pmc-llama-13b-awq", metadata={"help": "the model name"})
    dataset_name: Optional[str] = field(default="medmcqa", metadata={"help": "the dataset name", "choices":["medmcqa"]})
    data_path: Optional[str] = field(default=None, metadata={"help": "the dataset file path if you want to load data locally"})
    split: Optional[str] = field(default="train", metadata={"help": "dataset split to consider for context extraction"})
    out_dir: Optional[str] =  field(default="./out", metadata={"help": "outputs directory"})
    prompt_dir: Optional[str] =  field(default="./prompt", metadata={"help": "prompt templates directory"})
    cache_dir: Optional[str] =  field(default="/home/llms", metadata={"help": "cache directory"})
    max_samples: Optional[int] = field(default=-1, metadata={"help": "Maximum number of data to process. Default is -1 to process all data."})
    start_train_sample_idx: Optional[int] = field(default=0, metadata={"help": "Start index of first train sample to consider"})
    batch_size: Optional[int] = field(default=8, metadata={"help": "Number of prompts per batch to process during inference"})
    saving_steps: Optional[int] = field(default=2, metadata={"help": "interval for saving model outputs"})

    # Sampling Parameters
    n: Optional[int] = field(default=2, metadata={"help": "Number of output sequences to return for the given prompt."})
    best_of: Optional[int] = field(default=5, metadata={"help": "Number of output sequences that are generated from the prompt. From these best_of sequences, the top n sequences are returned. best_of must be greater than or equal to n. This is treated as the beam width when use_beam_search is True. By default, best_of is set to n."})
    temperature: Optional[float] = field(default=0.9, metadata={"help": "Float that controls the randomness of the sampling. Lower values make the model more deterministic, while higher values make the model more random. Zero means greedy sampling."})
    frequency_penalty: Optional[float] = field(default=1.95, metadata={"help": "Float that penalizes new tokens based on whether they appear in the generated text so far. Values > 0 encourage the model to use new tokens, while values < 0 encourage the model to repeat tokens."})
    top_p: Optional[float] = field(default=1.0, metadata={"help": " Float that controls the cumulative probability of the top tokens to consider. Must be in (0, 1]. Set to 1 to consider all tokens."})
    max_tokens: Optional[int] = field(default=512, metadata={"help": "maximum number of tokens to generate"})
    use_beam_search: Optional[bool] = field(default=False, metadata={"help": "Whether to use beam search instead of sampling."})

def get_parser():
    return HfArgumentParser(ScriptArguments)