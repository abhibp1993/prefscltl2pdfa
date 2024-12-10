import pygraphviz
import spot
from networkx.drawing import nx_agraph
from loguru import logger


def scltl2dfa(formula):
    # Use LTLf2DFA to convert LTLf formula to DFA.
    aut = spot.translate(formula, "BA", "High", "SBAcc", "Complete")
    bdd_dict = aut.get_dict()
    # logger.info(f"{ltlf_formula=}, dot={dot}")

    # Construct DFA dictionary using networkx MultiDiGraph.
    dfa = dict()
    dfa["states"] = set()
    dfa["transitions"] = dict()
    dfa["init_state"] = int(aut.get_init_state_number())
    dfa["final_states"] = set()

    for src in range(0, aut.num_states()):
        dfa["states"].add(int(src))
        dfa["transitions"][int(src)] = dict()

        for edge in aut.out(src):
            f_lbl_str = str(spot.bdd_format_formula(bdd_dict, edge.cond))
            if f_lbl_str == '1':
                f_lbl_str = "true"
            elif f_lbl_str == '0':
                f_lbl_str = "false"
            dfa["transitions"][int(edge.src)][f_lbl_str] = int(edge.dst)
            if edge.acc.count() > 0:
                dfa["final_states"].add(int(edge.src))

    logger.debug(f"ltlf_formula={formula}, dfa={dfa}")
    return dfa


def outcomes(dfa, q):
    out = set(i for i in range(len(q)) if q[i] in dfa[i]["final_states"])
    if len(out) == 0:
        return {-1}
    return out


def maximal_outcomes(relation, outcomes):
    # No formula in (sat - f) is preferred to f
    return {f for f in outcomes if not any((t, f) in relation for t in outcomes - {f})}


def vectorize(dfa, outcomes):
    """
    In case of ScLTLf formulas, the vector representing class has size len(dfa) + 1.
    The additional entry corresponds to completion formula, and is set to 1 if and only if all other entries are 0.
    """
    vector = [0] * (len(dfa) + 1)
    for idx in outcomes:
        vector[idx] = 1
    return tuple(vector)

