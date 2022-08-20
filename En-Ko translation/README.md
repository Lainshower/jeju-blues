# English - Korean Machine Translation with AIhub & Netflix dataset
## Requirements
- python >= 3.6
- NumPy >= 1.11.1
- huggingface
- tqdm

## Training
- STEP 0. Download dataset
    - Download AIhub dataset
        - 한국어-영어 번역 말뭉치(구어체, 대화체)
    - extract Netflix dataset using Language Learning with Netflix
        - Focusing on daily life movies and dramas(Friends, Eternal sunshine, etc.)

- STEP 1. Data preprocessing
```python
!python Data_Preprocessing.py 
```

- STEP 2. Train
``` 
    --evaluation_strategy="epoch",
    --learning_rate=2e-5,
    --per_device_train_batch_size=8,
    --per_device_eval_batch_size=8,
    --weight_decay=0.01,
    --save_total_limit=3,
    --num_train_epochs=5,
    --save_strategy='epoch'
```

- STEP 3. Inference
```python
!python Inference.py 
```

- STEP 4. Evaluation
    - BLEU score : 15.55
```python
!python Evaluate.py 
```
