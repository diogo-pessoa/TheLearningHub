def parser_http_referer(http_referer: str):
    """
        parses site url from http_referer meta for url() path and id
        :param http_referer
        :return dict {"path", "id"}
    """
    redirect_path = http_referer.split("/")
    path = redirect_path[3]
    object_id = redirect_path[4]
    return {'path': path,
            'id': object_id}
