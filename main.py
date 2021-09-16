from Scraper.Scraper import scrape


def main():

    print("Getting top posts of day...")
    posts = scrape('wallstreetbets')
    print('Posts fetched')


if __name__ == '__main__':

    main()
