# my_inquiry_chain.py - 장애 신고 접수 체인 (4-3 체인을 운영 업무로 변형)
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_aws import ChatBedrockConverse
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()
llm = ChatBedrockConverse(
    model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    region_name="us-east-1",
    temperature=0,
)


# --- 부품 A: 접수 분류 체인 ---
class IncidentReport(BaseModel):
    severity: str = Field(
        description="장애 등급. P1은 서비스 전면 중단, P2는 일부 기능 장애, P3은 불편 수준. 셋 중 하나만 쓴다"
    )
    system: str = Field(description="대상 시스템 이름. 신고에 없으면 '확인 필요'로 쓴다")
    summary: str = Field(description="장애 현상 한 줄 요약. 30자 이내")


report_parser = JsonOutputParser(pydantic_object=IncidentReport)
report_prompt = PromptTemplate(
    template="다음 장애 신고를 접수 양식으로 정리해.\n\n신고: {inquiry}\n\n{format_instructions}",
    input_variables=["inquiry"],
    partial_variables={"format_instructions": report_parser.get_format_instructions()},
)
report_chain = report_prompt | llm | report_parser

# --- 부품 B: 접수 회신 초안 체인 ---
reply_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "너는 삼성SDS 운영팀 장애 접수 담당자야. "
     "접수 확인, 예상 대응, 신고자에게 요청할 추가 정보를 각각 한 문장으로 써. "
     "총 세 문장을 넘기지 마."),
    ("human", "{inquiry}"),
])
reply_chain = reply_prompt | llm | StrOutputParser()

full_chain = RunnableParallel(report=report_chain, reply=reply_chain)

if __name__ == "__main__":
    cases = [
        "결제 API가 5분째 502를 뱉습니다. 고객 결제가 전부 실패 중입니다.",   # P1을 기대
        "물류 관제 대시보드에서 어제 자 그래프만 안 보입니다.",              # P2~P3을 기대
        "그거 좀 이상한데 한번 봐주세요.",                                  # 일부러 넣은 애매한 입력
    ]
    for c in cases:
        r = full_chain.invoke({"inquiry": c})
        print("=" * 60)
        print(f"신고: {c}")
        print(f"등급 {r['report']['severity']} / 시스템 {r['report']['system']}")
        print(f"요약: {r['report']['summary']}")
        print(r["reply"])