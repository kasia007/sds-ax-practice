def draw(graph, fileName):
    try:
        graph.get_graph().draw_mermaid_png(output_file_path=f"{fileName}.png")
        print(f"{fileName}.png 저장 완료")
    except Exception as e:
        print("PNG 저장은 건너뜁니다:", e)
        print(graph.get_graph().draw_mermaid())   # 텍스트 출력으로 