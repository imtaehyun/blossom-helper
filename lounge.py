import time
import sys
from blossom import Blossom

CONFIG = {
    'id': '', # Blossom ID
    'pw': '', # Blossom PW
}

blossom = Blossom()
blossom.login(CONFIG['id'], CONFIG['pw'])

reserve_option = {
    'people': '8', # 이용인원
    'date': '2018032420180325', # 이용기간 (YYYYMMDDYYYYMMDD, 시작일(토)종료일(일))
    'lounge': ['O', 'P', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'], # 예약라운지 선호도 순
}

refresh = False

while True:
    if len(reserve_option['lounge']) == 0:
        print('이번주는 공쳤어요. 다음주에.')
        sys.exit()

    print('라운지 {} 시도'.format(reserve_option['lounge'][0]))
    result = blossom.reserve_lounge(reserve_option['people'], reserve_option['date'], reserve_option['lounge'][0], refresh)
    
    if result == 'NO_DATE':
        print('아직 시간이 아닌가봐요. 5초 쉽니다.')
        time.sleep(5)
        refresh = True
        pass
    elif result == 'ALREADY_BOOKED':
        # 다음방으로
        del reserve_option['lounge'][0]
        print(len(reserve_option['lounge']))
        refresh = False
        time.sleep(1)
        pass
    elif result == 'SUCC':
        print('성공')
        sys.exit()
