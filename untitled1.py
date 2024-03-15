import pandas as pd
data = pd.read_csv('C:/Users/skrtk/Desktop/전기차충전소 입지예측/data/나주_전기차충전소정보1 (1).csv')
data.info()
data['이용자제한'].value_counts()
data1 = data[data['이용자제한']!='비공개']
# 시도 군구 급속충전량 제거

data2 = data1.drop(['시도', '군구', '급속충전량'], axis=1)
data2 = data2.drop('Unnamed: 0', axis=1)
data2.to_csv('C:/Users/skrtk/Desktop/전기차충전소 입지예측/data/나주_전기차충전소정보2.csv')


data2.info()


see = pd.read_csv('C:/Users/skrtk/Downloads/naju_floor.csv')
see.val.value_counts()

raw = pd.read_csv('C:/Users/skrtk/Downloads/나주통합데이터.csv')
raw.info()
raw.columns

col = ['공연시설_공연시설접근성', '공시지가_공시지가',
'도서관_도서관접근성', '병원_병원접근성', '보건기관_보건기관접근성', '생활권공원_생활권공원 접근성',
'소방서_소방서접근성', '인구_인구', '주제공원_주제공원접근성', '주차장_주차장접근성', '체육시설__체육시설접근성',
'초등학교_초등학교접근성']

col.str.split('_')

raw1 = raw.rename(columns = {'공연시설_공연시설접근성': '공연시설접근성',
                             '공시지가_공시지가': '공시지가',
                             '도서관_도서관접근성':'도서관접근성',
                             '병원_병원접근성':'병원접근성', 
                             '보건기관_보건기관접근성':'보건기관접근성',
                             '생활권공원_생활권공원 접근성': '생활권공원접근성',
                             '소방서_소방서접근성':'소방서접근성',
                             '인구_인구':'인구',
                             '주제공원_주제공원접근성':'주제공원접근성',
                             '주차장_주차장접근성':'주차장접근성',
                             '체육시설__체육시설접근성':'체육시설접근성',
                             '초등학교_초등학교접근성':'초등학교접근성'})

raw1.columns
raw1.to_csv('C:/Users/skrtk/Downloads/나주통합데이터.csv', index=False)


raw.CHARGING.value_counts()
