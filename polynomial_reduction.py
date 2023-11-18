def vertex_cover_to_hitting_set(graph, k):
    hitting_set_instance = []
    for edge in graph:
        hitting_set_instance.append(set(edge))

    return hitting_set_instance

def hitting_set(S, b):
    elements = set()
    for subset in S:
        elements.update(subset)

    all_combinations = [[]]

    for elem in elements:
        new_combinations = []
        for comb in all_combinations:
            new_combinations.append(comb + [elem])
        all_combinations.extend(new_combinations)

    for combo in all_combinations:
        check = True
        for subset in S:
            if not any(elem in combo for elem in subset):
                check = False
                break

        if check and len(combo) <= b:
            return set(combo)

    return None

def translate_hitting_set_to_vertex_cover(hitting_set_solution):
    vertex_cover_solution = hitting_set_solution

    return vertex_cover_solution

def verify_vertex_cover_solution(vertex_cover_solution, graph, k):
    if not vertex_cover_solution: return True
    elif len(vertex_cover_solution) > k: return False
    else:
        for vertex in graph:
            check = False
            for vertex_solution in vertex_cover_solution:
                if vertex_solution in vertex:
                    check = True
                    break
            if not check: return False
        return True

def main():

    G = [['1','2'],['2', '3'],['3', '4']]
    k = 1

    S = vertex_cover_to_hitting_set(G, k)

    hitting_set_solution = hitting_set(S, k)

    vertex_cover_solution = translate_hitting_set_to_vertex_cover(hitting_set_solution)

    valid = verify_vertex_cover_solution(vertex_cover_solution, G, k)
    print("Solução de HITTING SET:", hitting_set_solution)
    print("Solução traduzida de VERTEX COVER:", vertex_cover_solution)
    print("A solução traduzida é válida?", valid)

if __name__ == "__main__":
    main()