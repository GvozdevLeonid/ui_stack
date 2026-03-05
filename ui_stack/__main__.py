import argparse
import sys

from .ui_stack import (
    build,
    check_dependency_updates,
    clean,
    install_dependencies,
    install_template,
    start,
    update_dependencies,
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="ui_stack is a Python pipeline for UI (includes Tailwind CSS, daisyUI and AlpineJS)",
    )
    parser.add_argument(
        "-f", "--folder",
        help="Your ui_stack folder name",
    )

    subparsers = parser.add_subparsers(dest="command", title="Available commands", required=True)

    ui_stack_init_parser = subparsers.add_parser("init", help="Initialize ui_stack folder.")
    ui_stack_init_parser.add_argument("-d", "--daisyui", action="store_true", help="Include daisyUI")
    ui_stack_init_parser.add_argument("-a", "--alpinejs", action="store_true", help="Include AlpineJS")
    ui_stack_init_parser.add_argument("-p", "--alpinejs_plugins", action="store", help="comma-separated list of AplineJS plugins (mask, intersect, resize, persist, focus, collapse, anchor, morph, sort)", default="")

    ui_stack_install_parser = subparsers.add_parser("install", help="Install npm packages")
    ui_stack_build_parser = subparsers.add_parser("build", help="Compile css and js into production")
    ui_stack_start_parser = subparsers.add_parser("start", help="Start watching css changes")
    ui_stack_clean_parser = subparsers.add_parser("clean", help="Remove node modules folder")
    ui_stack_check_updates_parser = subparsers.add_parser("check_updates", help="List possible updates for css and js dependencies")
    ui_stack_update_parser = subparsers.add_parser("update", help="Update possible css and js dependencies")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    args, _ = parser.parse_known_args()

    if args.command == "init":
        install_template(
            args.folder,
            args.daisyui,
            args.alpinejs,
            args.alpinejs_plugins,
        )

    elif args.command == 'install':
        install_dependencies(args.folder)

    elif args.command == 'build':
        build(args.folder)

    elif args.command == 'start':
        start(args.folder)

    elif args.command == 'check_updates':
        check_dependency_updates(args.folder)

    elif args.command == 'update':
        update_dependencies(args.folder)

    elif args.command == 'clean':
        clean(args.folder)


if __name__ == "__main__":
    main()
