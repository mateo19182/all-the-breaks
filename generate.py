import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
model = MusicGen.get_pretrained('mateo-19182/all-the-breaks')
model.set_generation_params(duration=10)
wav = model.generate_unconditional(10)

for idx, one_wav in enumerate(wav):
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)
