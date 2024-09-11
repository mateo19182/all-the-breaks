[Download on Huggingface](https://huggingface.co/mateo-19182/all-the-breaks)

smol model trained on 295 freely available drum breaks. No text conditioning was used (inspired by https://github.com/aaronabebe/micro-musicgen, also using his audiocraft fork). 

only trained for 5 epochs, liked the sound there but can resume training with continue_from=checkpoint.th

useful docs: https://github.com/facebookresearch/audiocraft/blob/main/docs/TRAINING.md

examples:
  (picked at random)

<table style="width:100%; text-align:center;">
  <tr>
    <td>
      <audio controls>
        <source src="https://huggingface.co/mateo-19182/all-the-breaks/resolve/main/3.wav?download=true" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </td>
    <td>
      <audio controls>
        <source src="https://huggingface.co/mateo-19182/all-the-breaks/resolve/main/sample_3.wav?download=true" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </td>
  </tr>
  <tr>
    <td>
      <audio controls>
        <source src="https://huggingface.co/mateo-19182/all-the-breaks/resolve/main/9.wav?download=true" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </td>
    <td>
      <audio controls>
        <source src="https://huggingface.co/mateo-19182/all-the-breaks/resolve/main/sample_9.wav?download=true" type="audio/wav">
        Your browser does not support the audio element.
      </audio>
    </td>
   </tr>
</table>

training:

```
dora run solver=musicgen/musicgen_base_32khz model/lm/model_scale=small conditioner=none dataset.batch_size=5 dset=audio/breaks.yaml dataset.valid.num_samples=1 generate.every=10000 evaluate.every=10000 optim.optimizer=adamw optim.lr=1e-4 optim.adam.weight_decay=0.01 checkpoint.save_every=5
```


inference: 

```
import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
model = MusicGen.get_pretrained('mateo-19182/all-the-breaks')
model.set_generation_params(duration=10)
wav = model.generate_unconditional(10)

for idx, one_wav in enumerate(wav):
    audio_write(f'{idx}', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)
```


included export.py from https://huggingface.co/spaces/facebook/MusicGen/blob/main/audiocraft/utils/export.py since I couldnt find it in the audiocraft git repo and its pretty usefull.