from Scraper.Scraper import scrape
from Scraper.PostFilter import filter
from Analyzer.Analyzer import Analyzer


def main():

    # get top posts of day and filter by DD
    print("Getting top posts of day...")
    posts = scrape('wallstreetbets')
    print('Posts fetched, filtering...')
    filter(posts, tag="DD", textFilter='$')
    print('Posts filtered')

    print('Analyzing post sentiments...')
    analyzer = Analyzer()
    postSentiments = analyzer.analyze(posts)
    print("Posts analyzed")
    print("Post Sentiments:", postSentiments)


if __name__ == '__main__':

    main()
