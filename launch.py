from configparser import ConfigParser
from argparse import ArgumentParser

from utils.server_registration import get_cache_server
from utils.config import Config
from crawler import Crawler

from scraper import WORD_COUNTS, LONGEST_PAGE, SUBDOMAIN_COUNTS
import json
from similarity_ngram import NEAR_DUPLICATES
# from scraper import NEAR_DUPLICATES

def save_analytics():
    # Top 50 words
    top_words = sorted(WORD_COUNTS.items(), key=lambda x: -x[1])[:50]

    data = {"longest_page": {
        "url": LONGEST_PAGE[0],
        "word_count": LONGEST_PAGE[1]
    }, "top_words": top_words, "subdomains": dict(sorted(SUBDOMAIN_COUNTS.items())),
        "near_duplicates": [
        {"url1": u1, "url2": u2, "similarity": sim}
        for (u1, u2, sim) in NEAR_DUPLICATES
    ]}

    with open("analytics.json", "w") as f:
        json.dump(data, f, indent=2)


def main(config_file, restart):
    cparser = ConfigParser()
    cparser.read(config_file)
    config = Config(cparser)
    config.cache_server = get_cache_server(config, restart)
    crawler = Crawler(config, restart)
    crawler.start()

    save_analytics()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--restart", action="store_true", default=False)
    parser.add_argument("--config_file", type=str, default="config.ini")
    args = parser.parse_args()
    main(args.config_file, args.restart)
