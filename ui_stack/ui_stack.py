import logging
import os
import subprocess
import sys
from typing import Any

from .utils import get_project_root, get_src_path


def install_pip_package(package: str) -> None:
    import pip._internal as pip  # noqa: PLC2701

    pip.main(["install", package])


def get_or_install_cookiecutter() -> Any:
    try:
        from cookiecutter.main import cookiecutter
    except ImportError:
        logging.info("Cookiecutter is not found, installing...")
        try:
            install_pip_package("cookiecutter")
            from cookiecutter.main import cookiecutter
        except ModuleNotFoundError:
            return logging.error(
                "Failed to install 'cookiecutter' via pip. Please install it manually "
                "(https://pypi.org/project/cookiecutter/) and run `ui_stack init` again.",
            )
    return cookiecutter


def npm_command(folder: str, *args: str) -> None:
    cwd = get_src_path(folder)
    npm = os.environ.get('NPM_BIN_PATH', 'npm')

    try:
        try:
            subprocess.run([npm, *list(args)], cwd=cwd, check=True)
            return True
        except subprocess.CalledProcessError:
            sys.exit(1)
        except OSError as err:
            raise Exception(
                "\nIt looks like node.js and/or npm is not installed or cannot be found.\n\n"
                "Visit https://nodejs.org to download and install node.js for your system.\n\n"
                "If you have npm installed and still getting this error message, "
                "set NPM_BIN_PATH env variable to match path of NPM executable in your system.",
            ) from err

    except Exception as err:
        return logging.error(err)
    except KeyboardInterrupt:
        sys.exit(0)


def install_template(folder: str, include_daisy_ui: bool = False, include_alpinejs: bool = False, alpinejs_plugins: str = "") -> None:
    cookiecutter = get_or_install_cookiecutter()
    # try:
    theme_folder_path = cookiecutter(
        os.path.dirname(__file__),
        output_dir=get_project_root(),
        directory="template",
        no_input=True,
        overwrite_if_exists=True,
        extra_context={
            "folder": folder,
            "include_daisy_ui": "yes" if include_daisy_ui else "no",
            "include_alpinejs": "yes" if include_alpinejs else "no",
            "include_alpinejs_plugins": "yes" if alpinejs_plugins else "no",
            "alpinejs_plugins": alpinejs_plugins,
        },
    )

    theme_folder = os.path.basename(theme_folder_path)
    logging.info(
        f"your UI folder has been successfully created in '{theme_folder}' "
        "Please run the following command to install all dependencies: `ui_stack install`",
    )

    # except Exception as err:
    #     return logging.error(err)


def install_dependencies(folder: str, no_package_lock: bool = False) -> None:
    if no_package_lock:
        npm_command(folder, "install", "--no-package-lock")
    else:
        npm_command(folder, "install")


def check_dependency_updates(folder: str) -> None:
    npm_command(folder, "outdated")


def update_dependencies(folder: str) -> None:
    npm_command(folder, "update")


def build(folder: str) -> None:
    npm_command(folder, "run", "build")


def start(folder: str) -> None:
    npm_command(folder, "run", "start")
