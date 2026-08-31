from pathlib import Path

# 프로젝트 루트(= 이 파일의 상위 폴더의 상위) 기준으로 저장 위치를 고정합니다.
# 실행 위치(cwd)가 어디든 항상 common/img 에 저장됩니다.
IMG_DIR = Path(__file__).resolve().parent / "img"


def _as_drawable(graph, xray):
    """CompiledGraph 와 Graph(=get_graph() 결과) 를 모두 받아 Graph 로 통일합니다."""
    if hasattr(graph, "draw_mermaid"):        # 이미 Graph 객체
        return graph
    if hasattr(graph, "get_graph"):           # CompiledGraph / StateGraph
        return graph.get_graph(xray=xray) if xray else graph.get_graph()
    raise TypeError(f"그릴 수 없는 객체입니다: {type(graph).__name__}")


def draw(graph, fileName, xray=False):
    """그래프를 common/img 에 png 로 저장하고, mermaid 텍스트도 .mmd 로 남깁니다.

    xray=True 를 주면 서브그래프(팀) 내부까지 펼쳐서 그립니다.
    """
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    g = _as_drawable(graph, xray)

    mermaid = g.draw_mermaid()
    mmd = IMG_DIR / f"{fileName}.mmd"
    mmd.write_text(mermaid, encoding="utf-8")
    print(f"{mmd} 저장 완료 (mermaid 텍스트)")

    out = IMG_DIR / f"{fileName}.png"
    try:
        g.draw_mermaid_png(output_file_path=str(out))   # mermaid.ink 사용 (네트워크 필요)
        print(f"{out} 저장 완료")
    except Exception as e:
        print("PNG 저장은 건너뜁니다:", e)
        print(mermaid)   # 텍스트 출력으로 대체
