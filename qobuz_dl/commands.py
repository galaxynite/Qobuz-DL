import argparse


def qobuz_dl_args(
    default_quality=6, default_limit=10, default_folder="Qobuz Downloads"
):
    parser = argparse.ArgumentParser(
        prog="qobuz-dl",
        description=(
            "The ultimate Qobuz music downloader.\nSee usage"
            " examples on https://github.com/vitiko98/qobuz-dl"
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-r", "--reset", action="store_true", help="create/reset config file"
    )

    subparsers = parser.add_subparsers(
        title="commands",
        description="run qobuz-dl <command> --help for more info\n(e.g. qobuz-dl fun --help)",
        dest="command",
    )

    def add_common_arg(custom_parser):
        custom_parser.add_argument(
            "-e", "--embed-art", action="store_true", help="embed cover art into files"
        )
        custom_parser.add_argument(
            "-d",
            "--directory",
            metavar="PATH",
            default=default_folder,
            help='directory for downloads (default: "{}")'.format(default_folder),
        )
        custom_parser.add_argument(
            "-q",
            "--quality",
            metavar="int",
            default=default_quality,
            help=(
                'audio "quality" (5, 6, 7, 27)\n'
                "[320, LOSSLESS, 24B <96KHZ, 24B >96KHZ] (default: 6)"
            ),
        )

    interactive = subparsers.add_parser(
        "fun",
        description="Interactively search for tracks and albums.",
        help="interactive mode",
    )
    interactive.add_argument(
        "-a",
        "--albums-only",
        action="store_true",
        help="enable albums-only search",
    )
    interactive.add_argument(
        "-l",
        "--limit",
        metavar="int",
        default=default_limit,
        help="limit of search results by type (default: 10)",
    )
    add_common_arg(interactive)

    download = subparsers.add_parser(
        "dl",
        description="Download by album/track/artist/label/playlist URL.",
        help="input mode",
    )
    add_common_arg(download)
    download.add_argument(
        "SOURCE",
        metavar="SOURCE",
        nargs="+",
        help=("one or more URLs (space separated) or a text file"),
    )

    lucky = subparsers.add_parser(
        "lucky",
        description="Download the first <n> albums returned from a Qobuz search.",
        help="lucky mode",
    )
    lucky.add_argument(
        "-t",
        "--type",
        default="album",
        help="type of items to search (artist, album, track, playlist) (default: album)",
    )
    lucky.add_argument(
        "-n",
        "--number",
        metavar="int",
        default=default_limit,
        help="number of results to download (default: 1)",
    )
    add_common_arg(lucky)
    lucky.add_argument("QUERY", nargs="+", help="search query")

    return parser
