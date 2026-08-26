# hello_graph.py (작성 시작)
from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class State(TypedDict):
    user_input: str
    response: str


def respond(state: State) -> dict:
    user = state["user_input"]                            # 1) State에서 읽고
    return {"response": f"입력하신 내용은 '{user}' 입니다."}  # 2) 갱신분만 반환


# 노드는 그냥 함수이므로 그래프 없이도 직접 호출해 볼 수 있습니다
print(respond({"user_input": "테스트"}))

builder = StateGraph(State)
builder.add_node("respond", respond)
builder.add_edge(START, "respond")
builder.add_edge("respond", END)

graph = builder.compile()    # 그래프를 실행 가능한 객체로 변환

result = graph.invoke({"user_input": "안녕하세요"})
print(result)