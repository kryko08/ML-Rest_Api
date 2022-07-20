import torch

class NTSNetPredictor():
    def __init__(self) -> None:
        self.en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.en-de.single_model', tokenizer='moses', bpe='fastbpe')
    
    def translate(self, message):
        response = self.en2de.translate(message)
        return response