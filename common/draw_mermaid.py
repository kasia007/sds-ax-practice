from pathlib import Path

# 프로젝트 루트(= 이 파일의 상위 폴더의 상위) 기준으로 저장 위치를 고정합니다.
# 실행 위치(cwd)가 어디든 항상 common/img 에 저장됩니다.
IMG_DIR = Path(__file__).resolve().parent / "img"


def draw(graph, fileName):
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    out = IMG_DIR / f"{fileName}.png"
    try:
        graph.get_graph().draw_mermaid_png(output_file_path=str(out))
        print(f"{out} 저장 완료")
    except Exception as e:
        print("PNG 저장은 건너뜁니다:", e)
        print(graph.get_graph().draw_mermaid())   # 텍스트 출력으로 대체
