import pulp as p


def zlp_solver(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, p1, p2, p3, r1, r2, r3, r4):
    Lp_prob = p.LpProblem('Problem', p.LpMaximize)
    x1 = p.LpVariable("x1", lowBound = 0)   # Создать переменную x> = 0
    x2 = p.LpVariable("x2", lowBound = 0)
    x3 = p.LpVariable("x3", lowBound = 0)

    Lp_prob += p1*x1 + p2*x2 + p3*x3 # тут меняются коэфф и это функция для максимизации

    # тут пишем неравенства
    Lp_prob += k1*x1 + k2*x2 + k3*x3 <= r1
    Lp_prob += k4*x1 + k5*x2 + k6*x3 <= r2
    Lp_prob += k7*x1 + k8*x2 + k9*x3 <= r3
    Lp_prob += k10*x1 + k11*x2 + k12*x3 <= r4

    print(Lp_prob)

    status = Lp_prob.solve()   # Солвер

    out_str = f"статус - {p.LpStatus[status]}, оптимальные значения x1({p.value(x1)}) x2({p.value(x2)}) x3({p.value(x3)}). Ответ: {p.value(Lp_prob.objective)}"

    print(p.LpStatus[status])   # Статус решения
    print(p.value(x1), p.value(x2), p.value(x3), p.value(Lp_prob.objective))
    return out_str
