"""Generate a WordCloud image from text input."""

from argparse import ArgumentParser
from pathlib import Path

import matplotlib.pyplot as plt
from wordcloud import WordCloud

DEFAULT_TEXT = (
    "GitHub Actions for CI/CD "
    "GitHub Packages for container hosting "
    "Protected branches on all repos "
    "Access to Code spaces "
    "Multiple reviewers in pull requests "
    "Required status checks "
    "Code owners "
    "Reviewers "
    "Pages for static website hosting "
    "Web-based support"
)


def parse_args():
    """Parse command-line arguments."""
    parser = ArgumentParser(description="Generate a word cloud PNG from text input.")
    parser.add_argument("--text", help="Inline text input used to generate the word cloud.")
    parser.add_argument(
        "--text-file",
        help="Path to a UTF-8 text file used to generate the word cloud.",
    )
    parser.add_argument(
        "--output",
        default="wordcloud.png",
        help="Path to output PNG file (default: wordcloud.png).",
    )
    return parser.parse_args()


def resolve_text(args):
    """Resolve text from CLI flags or fall back to default text."""
    if args.text and args.text_file:
        raise ValueError("Use either --text or --text-file, not both.")
    if args.text:
        return args.text
    if args.text_file:
        return Path(args.text_file).read_text(encoding="utf-8")
    return DEFAULT_TEXT


def generate_wordcloud(text, output_path):
    """Generate and save a word cloud PNG."""
    wordcloud_str = WordCloud(width=800, height=400, background_color="white").generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud_str, interpolation="bilinear")
    plt.axis("off")
    plt.savefig(output_path)
    plt.close()


def main():
    """Run the script."""
    args = parse_args()
    text = resolve_text(args)
    generate_wordcloud(text, args.output)


if __name__ == "__main__":
    main()
