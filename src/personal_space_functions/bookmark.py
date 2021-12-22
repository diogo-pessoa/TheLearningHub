def build_unified_bookmark_dict(article_bookmarks, video_class_bookmarks):
    unified_bookmark_dict = []
    for article_bookmark in article_bookmarks:
        unified_bookmark_dict.append(
            {
                'url': 'articles',
                'object': article_bookmark.article,
            }
        )
        for video_class_bookmark in video_class_bookmarks:
            unified_bookmark_dict.append(
                {
                    'url': 'video_class',
                    'object': video_class_bookmark.video_class,
                }
            )
    return unified_bookmark_dict
