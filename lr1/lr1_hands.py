import numpy as np


def is_negativ(fun):
    for i in fun:
        if i < 0:
            return True
    return False


def get_max_module(fun):
    return np.where(fun == fun.min())


def table_changer(change_list, main_str, mainstlb, main_el):
    for i in range(len(change_list)):
        for j in range(len(change_list[i])):
            # print(change_list[i][j], '/n', main_str[j], '/n', mainstlb[i], '/n', main_el, '/n')
            change_list[i][j] = change_list[i][j] - (main_str[j] * mainstlb[i])/main_el
            # print(change_list[i][j])
    return change_list


def zlp_hads(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, p1, p2, p3, p4, r1, r2, r3):
    result = np.array((0,-r1, -r2, -r3, 0, 0, 0, 0))
    s1 = np.array((p1, k1, k2, k3, 1, 0, 0, 0))
    s2 = np.array((p2, k4, k5, k6, 0, 1, 0, 0))
    s3 = np.array((p3, k7, k8, k9, 0, 0, 1, 0))
    s4 = np.array((p4, k10, k11, k12, 0, 0, 0, 1))

    print(s1, s2, s3, s4, result)
    max_iteration = 20

    new_basis = []

    while is_negativ(result) and max_iteration > 0:
        max_iteration -= 1
        main_stlb = get_max_module(result)[0][0]
        basis_new_index = main_stlb
        main_str = np.array((
            s1[0]/s1[main_stlb],
            s2[0]/s2[main_stlb],
            s3[0]/s3[main_stlb],
            s4[0]/s4[main_stlb]
        ))
        main_index = np.where(main_str > 0, main_str, np.inf).argmin()
        basis_old_index = main_index+1
        main_str = np.array((
            s1[main_stlb],
            s2[main_stlb],
            s3[main_stlb],
            s4[main_stlb],
            result[main_stlb]
        ))
        main_el = main_str[main_index]
        main_stlb = np.delete(main_str, main_index)
        new_basis.append([basis_old_index, basis_new_index])
        if main_index == 0:
            s2, s3, s4, result = table_changer(change_list=[s2/1.0, s3/1.0, s4/1.0, result/1.0], main_str=s1, mainstlb=main_stlb, main_el=main_el)
            s1 = s1/main_el
            # print(s1, s2, s3, s4, result, max_iteration)
            # print(main_el, main_str, main_stlb)

        elif main_index == 1:
            s1, s3, s4, result = table_changer(change_list=[s1/1.0, s3/1.0, s4/1.0, result/1.0], main_str=s2, mainstlb=main_stlb, main_el=main_el)
            s2 = s2/main_el
            # print(s1, s2, s3, s4, result, max_iteration)
            # print(main_el, main_str, main_stlb)
            break
        elif main_index == 2:
            s1, s2, s4, result = table_changer(change_list=[s1/1.0, s2/1.0, s4/1.0, result/1.0], main_str=s3, mainstlb=main_stlb, main_el=main_el)
            s3 = s3/main_el
            # print(s1, s2, s3, s4, result, max_iteration)
        else:
            s1, s2, s3, result = table_changer(change_list=[s1/1.0, s2/1.0, s3/1.0, result/1.0], main_str=s4, mainstlb=main_stlb, main_el=main_el)
            s4 = s4/main_el
            # print(s1, s2, s3, s4, result, max_iteration)
    if max_iteration == 0:
        out_str = f"Невозможно решить даную ЗЛП"
    else:
        # print(new_basis)
        out_str = f"оптимальные значения "
        for i in new_basis:
            if i[0] == 1:
                data_row = s1
            elif i[0] == 2:
                data_row = s2
            elif i[0] == 3:
                data_row = s3
            elif i[0] == 4:
                data_row = s4
            out_str += f"x{i[1]} = {data_row[0]} "
        out_str += f"Ответ: {result[0]}"
    return(out_str)


print(zlp_hads(2, 4, 5, 1, 8, 6, 7, 4, 5, 4, 6, 7, 120, 280, 240, 360, 10, 14, 12))
