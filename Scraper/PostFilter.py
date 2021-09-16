def filter(posts, tag=False, textFilter=False):

    filteredPosts = []

    for post in posts:
        if tag:
            if post.link_flair_text != tag:
                continue

        if textFilter:
            if not (textFilter in post.title or textFilter in post.selftext):
                continue

        filteredPosts.append(post)


    print(filteredPosts)

    return filteredPosts
