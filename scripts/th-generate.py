import torch
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

def load_model(checkpoint_path, scale='small'):
    model = MusicGen.get_pretrained(scale, device='cuda' if torch.cuda.is_available() else 'cpu')
    state_dict = torch.load(checkpoint_path)
    model.lm.load_state_dict(state_dict.get('model', state_dict), strict=False)
    return model

def generate_samples(model, num_samples=2, duration=10, save_path='./out'):
    model.set_generation_params(duration=duration)
    for idx, audio in enumerate(model.generate_unconditional(num_samples)):
        audio_write(f'{save_path}/sample_{idx}', audio.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)

if __name__ == "__main__":
    model = load_model("out.bin")
    #model = load_model("all-the-breaks.pt")
    generate_samples(model)
    print("Generation complete. Check the 'out' directory for the output.")