def parser_http_referer(http_referer: str):
    """
        parses site url from http_referer meta for url() path and id,
        Note this function will returns the declaration of the view in the urls.py of this application
        :param http_referer
        :return dict {"path", "id"}
    """
    redirect_path = http_referer.split("/")
    path = redirect_path[3]
    object_id = redirect_path[4]

    if redirect_path[3] == 'articles':

        if redirect_path[4] == 'edit':
            path = 'edit_article'
            object_id = redirect_path[5]
        elif redirect_path[4] == 'write_articles':
            path = redirect_path[3]
            object_id = redirect_path[4]

    return {'path': path,
            'id': object_id}
