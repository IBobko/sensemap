from main import MeaningNode

# Простой граф для демо
semantic_graph = {
    "дважды": ["умножение"],
    "два": ["число_2"],
    "умножение": ["операция"],
    "операция": ["результат"],
    "число_2": ["операнд"],
    "результат": ["4"],
}

def find_semantic_route(text):
    # Очень грубая демка! В реальности будет embeddings и анализ.
    route = []
    if "дважды два" in text:
        route.append(MeaningNode(node_id="start", content="дважды два", transformation="распознавание выражения"))
        route.append(MeaningNode(node_id="умножение", content="умножение 2*2", transformation="выделение операции"))
        route.append(MeaningNode(node_id="результат", content="4", transformation="вычисление"))
        return route, "4"
    # Если нет подходящего маршрута
    return [], "not implemented"
