# !git clone https://github.com/Lainshower/jeju-blues.git 
%cd glow-tts
!pip install -q --no-cache-dir "torch==1.5.1" -f https://download.pytorch.org/whl/cu101/torch_stable.html
!pip install -q --no-cache-dir "cython==0.29.12" "librosa==0.6.0" "numpy==1.16.4" "scipy==1.3.0" "numba==0.48" "Unidecode==1.0.22" "tensorflow==2.3.0" "inflect==4.1.0" "matplotlib==3.3.0"
%cd /content
!git clone https://github.com/NVIDIA/apex /content/apex
%cd /content/apex
!git checkout 37cdaf4
!pip install -q --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" .
%cd /content/drive/MyDrive/glow-tts/monotonic_align
!python setup.py build_ext --inplace
%cd /content/drive/MyDrive/glow-tts
!mkdir -p "/content/drive/MyDrive/glow-tts/checkpoint"
!pip install unidecode
%cd /content/drive/MyDrive/glow-tts
!python init.py -c configs/base.json -m "/content/drive/MyDrive/glow-tts/checkpoint"
!python train.py -c configs/base.json -m "/content/drive/MyDrive/glow-tts/checkpoint"
