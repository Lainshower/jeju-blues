JEJU-BLUES
======
### ENGLISH TEXT-TO-JEJU SPEECH READER
안녕하세요. 투빅스 14회 컨퍼런스 프로젝트 "우리 모두의 블루스"팀의 레포지토리입니다.
![image](https://user-images.githubusercontent.com/68999203/185734999-5af55674-7373-4422-9f3b-f1b76d95f38a.png)

**JEJU-BLUES는 영어 문장을 입력으로 받아, 제주도 사투리로 읽어주는 프레임워크입니다.**

### JEJU-BLUES 모델 구조
- 영어-한국어(표준어) : mBART-large-cc25 finetuned with Netflix eng-kor script, AI-HUB 구어체 데이터
- 한국어(표준어)-제주도 사투리 : transformer trained with JIT dataset
- 제주도 사투리(text)-mel_spectogram : GlowTTS trained with JSS dataset
- mel_spectogram-제주도 사투리 음성(wav) : HiFiGAN trained with JSS dataset

### JEJU-BLUES 모델 특징
- 한 문장씩 받아서 제주도 음성으로 변환합니다.
- 구어체 데이터셋을 중심으로 학습하였습니다.

### 학습 데이터
- Netfilx 한영 자막
- AI-HUB 구어체 데이터셋
- JIT 데이터셋
- JSS 데이터셋

### 모델 성능
Model| Dataset|BLUE|
---|-----|---|
mBART|AI-HUB구어체, Netfilx 한영 자막|15.55|
transformer|JIT|44.47|

음성의 경우 주로 human evaluation을 하기 때문에 성능을 따로 평가하진 않았습니다.

### 학습 모델 파일
- [mBART-large-cc25 finetuned with Netflix eng-kor script, AI-HUB 구어체 데이터](https://drive.google.com/drive/folders/1-kkk5d2vFzghxPRDuvkKB2dneR16bxOx?usp=sharing)
- [transformer trained with JIT dataset](https://drive.google.com/file/d/11EIMiCl2-c9o6gq3kPVGyFdGYPZnToh5/view?usp=sharing)
- [GlowTTS trained with JSS dataset]
- [HiFiGAN trained with JSS dataset](https://drive.google.com/drive/folders/1AZw5xjjQqOhfUuyre0yPCKyQrVN6yOEW?usp=sharing)

### JEJU-BLUES 관련 자료
- JEJU-BLUES와 관련된 자세한 내용은 컨퍼런스 발표 자료를 참고해주세요!
- https://docs.google.com/viewer?url=https://github.com/Lainshower/jeju-blues/files/9386560/NLP_SPEECH_.pdf?raw=True

### Reference
- [mBART](https://github.com/facebookresearch/fairseq/tree/main/examples/mbart)
- [Transformer](https://github.com/pytorch/fairseq)
- [GlowTTS]()
- [HiFiGAN](https://github.com/jik876/hifi-gan)
### Contributors
![image](https://user-images.githubusercontent.com/68999203/185737859-5befa5fa-0cc2-4832-bdb3-010f7f81e5c2.png) | ![image](https://user-images.githubusercontent.com/68999203/185738044-f7ed2c4a-72f4-4f28-aa49-1af3aa331ded.png) | ![image](https://user-images.githubusercontent.com/68999203/185738193-b88c7e6d-f03a-41d3-9ce8-e92d04d95969.png) | ![image](https://user-images.githubusercontent.com/68999203/185738756-11c5e388-6e69-4835-9a5c-df8b8d5b7732.png)|
---|---|---|---|
[SUYEON JEONG](https://github.com/fromslow)|[JONGHYUN HONG](https://github.com/jody1188) | [SEUNG JU LEE](https://github.com/) | [SUJIN LIM](https://github.com/sujjin)
Eng-Kor Translate|Eng-Kor Translate|Kor-Jeju dialect Translate|Kor-Jeju dialect Translate|

![image](https://user-images.githubusercontent.com/68999203/185738871-94b76735-a24c-43f3-a735-03b6c8f9ae1a.png)|![image](https://user-images.githubusercontent.com/68999203/185738900-e9c9ff04-59cd-4483-aac7-5487ae64e187.png)|![image](https://user-images.githubusercontent.com/68999203/185738890-a850e71d-c483-48ff-a684-37e9a43d8f1b.png)|
---|---|---|
[JOONWON JANG](https://github.com/Lainshower)|[KEONWOO KIM](https://github.com/gunny97)|[MINJIN JEON](https://github.com/minjin-jeon)|
TTS|TTS|TTS|


