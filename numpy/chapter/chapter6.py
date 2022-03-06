'''
영훈이가 창업한 흥부부대찌개 신주쿠점은 이제 직장인들에게 소문난 맛집입니다. 그러나 매일같이 성공적인 것은 아닙니다. 목표 일 매출을 달성하지 못하는 날들이 아직 꽤 있거든요. 영훈이가 생각하는 성공적인 하루 매출은 20만 엔입니다.

성공적이지 않은 날의 매출만 골라서 보고 싶습니다. 20만 엔 이하의 매출만 담긴 numpy array를 출력해주세요.
반복문은 사용하면 안 됩니다!

주의: 자동 채점 과제입니다. 정답 출력 코드는 print 없이 작성해 주세요. (예시: bad_days_revenue)
'''

import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000,
    440000, 140000, 180000, 340000,
    330000, 290000, 280000, 380000,
    170000, 140000, 230000, 390000,
    400000, 350000, 380000, 150000,
    110000, 240000, 380000, 380000,
    340000, 420000, 150000, 130000,
    360000, 320000, 250000
]

yen_array = np.array(revenue_in_yen)

bad_days_revenue = yen_array[np.where(yen_array < 200000)]

# 정답 출력
print(bad_days_revenue)