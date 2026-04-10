from scipy.stats import randint , uniform


LIGHTGM_MODEL = {
    "n_estimators": randint(50,500),
    "learning_rate": uniform(0.01, 0.04),   # 0.01 → 0.05
    "max_depth": randint(5, 100),
    "num_leaves": randint(50, 100),
    "min_child_samples": randint(10, 20),
    "subsample": uniform(0.5, 0.3),         # 0.5 → 0.8
    "reg_alpha": uniform(0.1, 0.4),         # 0.1 → 0.5
    "reg_lambda": uniform(0.1, 0.4)         # ✅ fixed name
}

RANDOM_SEARCH_PARAMS = {
    'n_iter': 5,
    "cv": 2,
    "n_jobs": -1,
    "verbose": 2,
    "random_state": 42,
    "scoring": "accuracy"
}
