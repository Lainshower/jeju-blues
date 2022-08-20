import glob
import os
import argparse
import json
import torch
from scipy.io.wavfile import write
from env import AttrDict
from meldataset import mel_spectrogram, MAX_WAV_VALUE, load_wav
from models import Generator
import easydict
from scipy.io import wavfile
import IPython.display as ipd

h = None
device = None

def load_checkpoint(filepath, device):
    assert os.path.isfile(filepath)
    print("Loading '{}'".format(filepath))
    checkpoint_dict = torch.load(filepath, map_location=device)
    print("Complete.")
    return checkpoint_dict

def get_mel(x):
    return mel_spectrogram(x, h.n_fft, h.num_mels, h.sampling_rate, h.hop_size, h.win_size, h.fmin, h.fmax)

def scan_checkpoint(cp_dir, prefix):
    pattern = os.path.join(cp_dir, prefix + '*')
    cp_list = glob.glob(pattern)
    if len(cp_list) == 0:
        return ''
    return sorted(cp_list)[-1]

def inference_mel_spec_from_librosa(a):
    generator = Generator(h).to(device)

    state_dict_g = load_checkpoint(a.checkpoint_file, device)
    generator.load_state_dict(state_dict_g['generator'])

    filelist = os.listdir(a.input_wavs_dir)

    os.makedirs(a.output_dir, exist_ok=True)

    generator.eval()
    generator.remove_weight_norm()
    with torch.no_grad():
        for i, filname in enumerate(filelist):
            wav, sr = load_wav(os.path.join(a.input_wavs_dir, filname))
            wav = wav / MAX_WAV_VALUE
            wav = torch.FloatTensor(wav).to(device)
            x = get_mel(wav.unsqueeze(0))
            
            y_g_hat = generator(x)
            audio = y_g_hat.squeeze()
            audio = audio * MAX_WAV_VALUE
            audio = audio.cpu().numpy().astype('int16')

            output_file = os.path.join(a.output_dir, os.path.splitext(filname)[0] + '_generated.wav')
            write(output_file, h.sampling_rate, audio)
            print(output_file)

def inference_mel_spec_from_model(a):
    generator = Generator(h).to(device)

    state_dict_g = load_checkpoint(a.checkpoint_file, device)
    generator.load_state_dict(state_dict_g['generator'])

    filelist = os.listdir(a.input_mels_dir)

    os.makedirs(a.output_dir, exist_ok=True)

    generator.eval()
    generator.remove_weight_norm()
    with torch.no_grad():
        for i, filname in enumerate(filelist):
            x = np.load(os.path.join(a.input_mels_dir, filname))
            x = torch.FloatTensor(x).to(device)
            
            
            if len(x.shape) == 2:
              
              x = x.unsqueeze(0)
              print('축 변환 완료 ')
              print('\n')

            y_g_hat = generator(x)
            audio = y_g_hat.squeeze()
            audio = audio * MAX_WAV_VALUE
            audio = audio.cpu().numpy().astype('int16')

            output_file = os.path.join(a.output_dir, os.path.splitext(filname)[0] + '_generated_e2e.wav')
            write(output_file, h.sampling_rate, audio)
            print(output_file)

def main_mel_spec_from_librosa():
    print('Initializing Inference Process..')

    parser = argparse.ArgumentParser()

    parser.add_argument('--group_name', default=None)
    parser.add_argument('--input_wavs_dir', default="/content/drive/MyDrive/tts_hifiGAN/dataset/wav_data")
    parser.add_argument('--output_dir', default="/content/drive/MyDrive/tts_hifiGAN/output_result")
    parser.add_argument('--checkpoint_file', default="/content/drive/MyDrive/tts_hifiGAN/hifi-gan/cp_hifigan/g_00162000")
    parser.add_argument('--config', default="/content/drive/MyDrive/tts_hifiGAN/hifi-gan/cp_hifigan/config.json")

    a = parser.parse_args()

    with open(a.config) as f:
        data = f.read()

    global h
    json_config = json.loads(data)
    h = AttrDict(json_config)

    torch.manual_seed(h.seed)

    global device
    if torch.cuda.is_available():
        torch.cuda.manual_seed(h.seed)
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    inference_mel_spec_from_librosa(a)

def main_mel_spec_from_model():
    print('Initializing Inference Process..')

    parser = argparse.ArgumentParser()

    parser.add_argument('--input_mels_dir', default="/content/drive/MyDrive/tts_hifiGAN/dataset/mel_data/bye")
    parser.add_argument('--output_dir', default="/content/drive/MyDrive/tts_hifiGAN/USING_output/bye")
    parser.add_argument('--checkpoint_file', default="/content/drive/MyDrive/tts_hifiGAN/hifi-gan/cp_hifigan/g_00200000")
    parser.add_argument('--config_file', default="/content/drive/MyDrive/tts_hifiGAN/hifi-gan/cp_hifigan/config.json")

    a = parser.parse_args()

    with open(a.config) as f:
        data = f.read()

    global h
    json_config = json.loads(data)
    h = AttrDict(json_config)

    torch.manual_seed(h.seed)
    global device
    if torch.cuda.is_available():
        torch.cuda.manual_seed(h.seed)
        device = torch.device('cuda')
    else:
        device = torch.device('cpu')

    inference_mel_spec_from_model(a)

if __name__ == "__main__":
    main_mel_spec_from_librosa()

    main_mel_spec_from_model()


    ### jupter notebook cell에서 실행하면서 예시 확인 ###
    # path = "/content/drive/MyDrive/tts_hifiGAN/output_result/9005_generated.wav"

    # fs, data = wavfile.read(path)
    # ipd.Audio(data, rate=22050)