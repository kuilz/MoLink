from typing import Dict, List, Tuple, Type
from torch import nn
from vllm.config import ModelConfig
from vllm.model_executor.models.adapters import (as_classification_model,
                                                 as_embedding_model,
                                                 as_reward_model)
from molink.model_executor.models.registry import ModelRegistry

def get_model_architecture(
        model_config: ModelConfig) -> Tuple[Type[nn.Module], str]:
    architectures = getattr(model_config.hf_config, "architectures", [])

    # Special handling for quantized Mixtral.
    # FIXME(woosuk): This is a temporary hack.
    mixtral_supported = [
        "fp8", "compressed-tensors", "gptq_marlin", "awq_marlin"
    ]

    if (model_config.quantization is not None
            and model_config.quantization not in mixtral_supported
            and "MixtralForCausalLM" in architectures):
        architectures = ["QuantMixtralForCausalLM"]

    model_cls, arch = ModelRegistry.resolve_model_cls(architectures)
    if model_config.task == "embed":
        model_cls = as_embedding_model(model_cls)
    elif model_config.task == "classify":
        model_cls = as_classification_model(model_cls)
    elif model_config.task == "reward":
        model_cls = as_reward_model(model_cls)

    return model_cls, arch