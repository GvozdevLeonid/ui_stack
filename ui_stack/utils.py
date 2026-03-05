import os


def get_project_root() -> str:
    root = os.environ.get("UI_STACK_PROJECT_ROOT")
    if not root:
        raise RuntimeError("UI_STACK_PROJECT_ROOT env var is not set")
    return os.path.realpath(root)


def get_folder_path(folder: str) -> str:
    return os.path.join(get_project_root(), folder)


def get_src_path(folder: str) -> str:
    return os.path.join(get_folder_path(folder), "static_src")


def get_node_modules_path(folder: str) -> str:
    return os.path.join(get_folder_path(folder), "static_src", "node_modules")
