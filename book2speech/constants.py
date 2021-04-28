TRANSFORMATIONS = ["reduced", "default", "extended"]
CORRECTIONS = ["simple", "compound", "segmentation"]

THRESHS = ["simple", "gaussian", "mean", "otsu", "disable"]
BLURS = ["average", "gaussian", "median", "bilateral", "disable"]

OPTIMIZERS = [
    "Nelder-Mead",
    "Powell",
    "CG",
    "BFGS",
    "Newton-CG",
    "L-BFGS-B",
    "TNC",
    "COBYLA",
    "SLSQP",
    "trust-constr",
    "dogleg",
    "trust-ncg",
    "trust-exact",
    "trust-krylov",
    "disable",
]

KEYS = [
    "image_path",
    "dictionary",
    "bigram",
    "lang",
    "correction_mode",
    "improve_image",
    "thresh_mode",
    "blur_mode",
    "dewarp",
    "optimizer",
    "transform_mode",
    "time",
    # "ellapsed",
]

METRICS = ["wer", "mer", "wil", "wip"]
