# Jejueo-Korean Machine Translation with JIT dataset & AIhub dataset
## Datasest
[JIT Dataset](https://www.kaggle.com/datasets/bryanpark/jit-dataset)

## Requirements
- python >= 3.6
- NumPy >= 1.11.1
- Fairseq
- Sentencepiece
- tqdm

## Training
- STEP 0. Download and extract the JIT dataset
- STEP 1. bpe segment for training
```python
!python bpe_segment.py --jit jit --vocab_size 4000 
```
- STEP 2. fairseq-prepro
```python
!python prepro.py --src ko --tgt je --vocab_size 4000  
```
- STEP 3. train
```python
!fairseq-train data/4k/ko-je-bin \
    --arch transformer       \
    --optimizer adam \
    --lr 0.0005 \
    --label-smoothing 0.1 \
    --dropout 0.3       \
    --max-tokens 4000 \
    --stop-min-lr '1e-09' \
    --lr-scheduler inverse_sqrt       \
    --weight-decay 0.0001 \
    --criterion label_smoothed_cross_entropy       \
    --max-epoch 1 \
    --warmup-updates 4000 \
    --warmup-init-lr '1e-07'    \
    --adam-betas '(0.9, 0.98)'       \
    --save-dir train/4k/ko-je-bin/ckpt  \
    --save-interval 1
```

- STEP 4. fairseq-generate
```python
!fairseq-generate data/4k/ko-je-bin \
  --path train/4k/ko-je-bin/ckpt/checkpoint_best.pt \
  --source-lang ko --target-lang je \
  --valid-subset 'valid' \
  --gen-subset 'test' \
  --beam 5 \
  --remove-bpe 'sentencepiece'\
  --results-path prediction
```
```python  
!grep '^H' prediction/generate-test.txt | cut -f3- > prediction/gen.out.sys # 예측된 문장 (H)
!grep '^T' prediction/generate-test.txt | cut -f2- > prediction/gen.out.ref # 타겟(정답) 문장 (T)
```
- STEP 5. Evaluation
```python
!fairseq-score \
--sys prediction/gen.out.sys \
--ref prediction/gen.out.ref
```
## Citation
@article{park2019jejueo,  
  title={Jejueo Datasets for Machine Translation and Speech Synthesis},  
  author={Park, Kyubyong and Choe, Yo Joong and Ham, Jiyeon},  
  journal={arXiv preprint arXiv:1911.12071},  
  year={2019}  }

## Reference
https://github.com/kakaobrain/jejueo.git
