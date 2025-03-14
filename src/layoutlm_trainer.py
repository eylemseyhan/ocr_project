from transformers import LayoutLMv2Processor, LayoutLMv2ForTokenClassification
from PIL import Image
import torch


processor = LayoutLMv2Processor.from_pretrained("microsoft/layoutlmv2-base-uncased")
model = LayoutLMv2ForTokenClassification.from_pretrained("microsoft/layoutlmv2-base-uncased", num_labels=10)
