import seaborn as sns
import matplotlib.pyplot as plt

# (데이터 측정)년도, (대상)국가, (1인당 연간 의료비)지출액, (평균)기대수명
health = sns.load_dataset("healthexp")

# 가장 최근 연도인 2020년 데이터를 필터링 후 추출
health_2020 = health[health['Year']==2020]
# print(health_2020)
# print(health_2020.sort_values(by=['Life_Expectancy'], ascending=False))
# print(health_2020.sort_values('Life_Expectancy', ascending=False))
# print(health_2020.sort_values(ascending=False, by=['Life_Expectancy']))
# print(health_2020.sort_values(ascending=False, 'Life_Expectancy'))  # error

# 전체 데이터셋에서 의료비 지출이 5000달러 이상인 데이터 추출
# high_spending = health[health['Spending_USD']>=5000]
# print(high_spending)
# 어떤 국가들이 있는지 확인
# print(high_spending['Country'].unique())
# 국가별 평균 의료비 지출과 평균 기대수명 구하기
# country_mean = health.groupby('Country')[['Spending_USD', 'Life_Expectancy']].mean()
# print(country_mean)
# 국가별로 데이터가 몇 개씩 있는지 개수 세기
# print(health['Country'].value_counts())
# 년도별 평균 의료비 지출과 평균 기대수명 구하기
# year_mean = health.groupby('Year')[['Spending_USD', 'Life_Expectancy']].mean()
# print(year_mean)
# 국가별 기대수명 분포 확인
# sns.catplot(data=health, x='Year', y='Life_Expectancy', col='Country', kind='box', col_wrap=3)
# plt.show()
# 가장 최근(2020년) 국가별 의료비 지출 비교
# sns.catplot(data=health_2020, x='Country', y='Spending_USD', kind='bar', palette='muted')
# plt.show()
# 국가별 의료비와 기대수명의 상관관계 (산점도)
sns.relplot(data=health,
            x='Spending_USD',
            y='Life_Expectancy',
            col='Country',
            col_wrap=3,
            kind='scatter',
            hue='Year',
            palette='Set1'
            )
plt.show()