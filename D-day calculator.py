#!/usr/bin/env python3
# """D-day calculator CLI.

# Usage examples:
#   python dday_calculator.py 2026-12-31
#   python dday_calculator.py 2024-01-01 --from-date 2026-04-27
# """

# from __future__ import annotations

# import argparse
# from datetime import date, datetime


# def parse_iso_date(value: str) -> date:
#     """Parse YYYY-MM-DD date string."""
#     try:
#         return datetime.strptime(value, "%Y-%m-%d").date()
#     except ValueError as exc:
#         raise argparse.ArgumentTypeError(
#             f"잘못된 날짜 형식입니다: {value}. YYYY-MM-DD 형식으로 입력하세요."
#         ) from exc


# def calculate_d_day(target_date: date, base_date: date) -> str:
#     """Return D-day string from base date to target date."""
#     diff = (target_date - base_date).days

#     if diff == 0:
#         return "D-DAY"
#     if diff > 0:
#         return f"D-{diff}"
#     return f"D+{abs(diff)}"


# def build_parser() -> argparse.ArgumentParser:
#     parser = argparse.ArgumentParser(description="디데이(D-day) 계산기")
#     parser.add_argument("target_date", type=parse_iso_date, help="목표 날짜 (YYYY-MM-DD)")
#     parser.add_argument(
#         "--from-date",
#         dest="base_date",
#         type=parse_iso_date,
#         default=date.today(),
#         help="기준 날짜 (YYYY-MM-DD), 기본값: 오늘",
#     )
#     return parser


# def main() -> None:
#     parser = build_parser()
#     args = parser.parse_args()

#     d_day = calculate_d_day(args.target_date, args.base_date)

#     print(f"기준일: {args.base_date.isoformat()}")
#     print(f"목표일: {args.target_date.isoformat()}")
#     print(f"결과: {d_day}")


# if __name__ == "__main__":
#     main()

# import  random   random은 모듈이라 ()안씀, 그 안에 함수는  () 사용

# workouts=['bench press','dead lift','squat','over head press'] 리스트: 데이터 한번에 관리, 서로 다른 자료형도 ㄱㄴ

# for i in range(3):   range(3): 0부터 3 전까지   range(2,6): 2부터 5까지    range(4,10,2) 4부터 9까지 2씩 추가 
'''print(random.choice(workouts))

i=0
print

i=1
print

i=2
print 

프린트 계속 해 줘  다시 돌아온다는 표시로 그냥 i 써줌
'''

# for i in range(5):
#  print(i)

# exercise=['벤치','스쿼트','데드리프트']   

# from random import randint


# print(randint(5,10))


# while True:
    # print('무한')

# from random import *
# print(randint(5,10))
'''
while True :
    text=input('종료하려면 q 입력:')
    
    if text=='q' :
        break
print('계속하기')
''' 
'''
pw=''

while pw!= '1021' :

    pw=input('비밀번호를 입력해 주세요. \n 비밀번호:')

    if pw=='1021' :
        print('잠금이 해제됩니다')
    
    elif pw=='2407' :
        print('비밀번호 %d 틀렸다 ㅋㅋ'%2407)
    
    else :
        print('좃까')
'''

student={
    '우영' :24 ,
    '세민' : 30 , 
    '서한' : 24
}

print(student['우영'])


