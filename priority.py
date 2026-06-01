tasks = []

print("우선순위 정하기 프로그램")
print("그만 입력하려면 할 일 이름에 '끝' 입력")

while True:
    name = input("\n할 일 이름: ")

    if name == "끝":
        break

    importance = int(input("중요도 1~5: "))
    urgency = int(input("긴급도 1~5: "))
    effort = int(input("난이도/소요시간 1~5: "))

    score = importance * 2 + urgency * 2 - effort

    tasks.append({
        "name": name,
        "importance": importance,
        "urgency": urgency,
        "effort": effort,
        "score": score
    })

tasks.sort(key=lambda x: x["score"], reverse=True)

print("\n=== 우선순위 결과 ===")

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task['name']} / 점수: {task['score']}")