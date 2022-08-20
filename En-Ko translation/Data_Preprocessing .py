import pandas as pd 
import re
import unicodedata
import glob

def make_df(data_path):
  all_data = pd.DataFrame() 
  for f in glob.glob(data_path):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)

  return all_data

# 문장부호 ".", ",", "?", "!" 외 제거 및 문장 끝 "." 없는 경우 "." 추가

def plus_aspt(data):

  data = data.drop_duplicates() # 중복 데이터 제거

  data = data.dropna() # 결측치 제거

  data['a'] = data['kr'].apply(lambda x: x.rstrip()[-1])
  data['a'] = data['a'].apply(lambda x: "" if (x==".") | (x==",") | (x=="?") | (x=="!") else " .")
  data['kr'] = data['kr'] + data['a']
  return data

def remove_gwal(text):

  text = re.sub(r'\([^)]*\)','',text).strip() # ()로 감싸진 모든 문자 삭제
  text = re.sub(r"\[.+\]",'',text).strip() # []로 감싸진 모든 문자 삭제
  return text

def unicode_to_ascii(s):
  return ''.join(c for c in unicodedata.normalize('NFD', s)
      if unicodedata.category(c) != 'Mn')


def preprocess_sentence_en(w):
  w = unicode_to_ascii(w.lower().strip())
  w = re.sub(r"\[.+\]",'',w).strip() 
  w = re.sub(r'\([^)]*\)','',w).strip() 
  w = re.sub(r"([?.!,¿])", r" \1 ", w)
  w = re.sub(r'[" "]+', " ", w)
  w = re.sub(r"[^0-9a-zA-Z?.!',¿$]+", " ", w)
  w = w.strip()

  return w


def preprocess_sentence_kr(w):
  w = w.strip()
  w = re.sub(r"\".+\"",'',w).strip() 
  w = re.sub(r"([?.!,¿])", r" \1 ", w)
  w = re.sub(r'[" "]+', " ", w)
  w = re.sub(r"[^0-9가-힣?.!,¿]+", " ", w)
  w = w.strip()

  return w

previous = ""

def transcript_preprocessing(data):

  for i in range(1,len(data)):
    if previous in data.iloc[i,1]:
      data.iloc[i,0] = data.iloc[i-1,0] + ' '+ data.iloc[i,0] 
      data = data.drop(data.index[i-1]) # 이전 문장 삭제
      previous = data.iloc[i,1]
  
  # 이전 문장이 더 길면, 현재 문장이 이전 문장과 중복뙤는 부분이 존재하면 실행
    if data.iloc[i,1] in previous:
  #if data.loc[i,'kr'] in previous:
      data.iloc[i-1,0] = data.iloc[i-1,0] + ' '+ data.iloc[i,0] # 이전 문장을 현재 문장과 합침
      data = data.drop(data.index[i]) # 그리고 현재 문장을 지운다
      previous = data.iloc[i-1,1]

    else: # 만약 중복되지 않는다면,
      previous = data.iloc[i,1] # 현재 문장을 previous 로 만들고 루프 돌리기

    if i>len(data):
      print(f"{i-1} 줄까지 실행, 한국어 문장 = {data.iloc[i-1,1]}")
      break
