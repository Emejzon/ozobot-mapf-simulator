from ozobotmapf.mapf_solvers.solver import Solver


class ManualSolver(Solver):
    def __init__(self):
        pass

    def plan(self):
        plan = {1: {'pos_list': [0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2, 0, 1, 3, 2], 'steps': [(0, 1), (1, 3), (3, 2), (2, 0), (0, 1), (1, 3), (3, 2), (2, 0), (0, 1), (1, 3), (3, 2), (2, 0), (0, 1), (1, 3), (3, 2)]}}
        plan_6x6_6a = {1: {'pos_list': [16, 17, 11, 5, 4, 3, 2, 2, 2, 2, 2, 2, 2, 3, 9, 15, 14, 8, 7, 13, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12], 'steps': [(16, 17), (17, 11), (11, 5), (5, 4), (4, 3), (3, 2), None, None, None, None, None, None, (2, 3), (3, 9), (9, 15), (15, 14), (14, 8), (8, 7), (7, 13), (13, 12), None, None, None, None, None, None]}, 2: {'pos_list': [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 9, 15, 14, 8, 7, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13], 'steps': [(1, 2), None, None, (2, 1), None, None, None, None, None, None, None, None, None, (1, 2), (2, 3), (3, 9), (9, 15), (15, 14), (14, 8), (8, 7), (7, 13), None, None, None, None, None]}, 3: {'pos_list': [12, 13, 7, 8, 14, 14, 14, 15, 9, 3, 4, 5, 11, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17], 'steps': [(12, 13), (13, 7), (7, 8), (8, 14), None, None, (14, 15), (15, 9), (9, 3), (3, 4), (4, 5), (5, 11), (11, 17), None, None, None, None, None, None, None, None, None, None, None, None, None]}, 4: {'pos_list': [14, 15, 14, 15, 9, 15, 9, 3, 4, 5, 11, 17, 16, 16, 16, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11], 'steps': [(14, 15), (15, 14), (14, 15), (15, 9), (9, 15), (15, 9), (9, 3), (3, 4), (4, 5), (5, 11), (11, 17), (17, 16), None, None, (16, 10), (10, 11), None, None, None, None, None, None, None, None, None, None]}, 5: {'pos_list': [0, 6, 6, 6, 7, 8, 8, 8, 14, 15, 9, 3, 4, 4, 4, 4, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'steps': [(0, 6), None, None, (6, 7), (7, 8), None, None, (8, 14), (14, 15), (15, 9), (9, 3), (3, 4), None, None, None, None, (4, 3), (3, 2), (2, 1), None, None, None, None, None, None, None]}, 6: {'pos_list': [10, 10, 16, 10, 10, 11, 17, 16, 16, 16, 16, 10, 10, 10, 11, 5, 5, 5, 4, 3, 9, 15, 14, 8, 7, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'steps': [None, (10, 16), (16, 10), None, (10, 11), (11, 17), (17, 16), None, None, None, (16, 10), None, None, (10, 11), (11, 5), None, None, (5, 4), (4, 3), (3, 9), (9, 15), (15, 14), (14, 8), (8, 7), (7, 6), (6, 0)]}}

        return plan_6x6_6a