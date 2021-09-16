from Scraper.Scraper import scrape
from Scraper.PostFilter import filter


def main():

    # get top posts of day and filter by DD
    print("Getting top posts of day...")
    posts = scrape('wallstreetbets')
    print('Posts fetched, filtering...')
    filter(posts, tag="DD", textFilter='$')
    print('Posts filtered')





if __name__ == '__main__':

    main()
