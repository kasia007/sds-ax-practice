# state_schema.py - State 스키마 정의
from typing import TypedDict


class State(TypedDict):
    user_input: str   # 사용자가 넣는 입력
    response: str     # 그래프가 채울 응답


initial: State = {"user_input": "안녕하세요", "response": ""}
print(initial, initial["user_input"])
print(type(initial))   # 실행 시점에는 그냥 dict입니다

# LangGraph가 내부에서 하는 일 (개념적으로)
state = {"user_input": "안녕", "response": ""}
node_returned = {"response": "입력하신 내용은 '안녕' 입니다."}
new_state = {**state, **node_returned}   # 같은 키는 덮어쓰기가 기본

print(new_state)
