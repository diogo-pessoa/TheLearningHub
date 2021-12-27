def load_role_based_content_list(content_objects: list, subscription_active: bool, user_is_staff: bool):
    """
    Gets a list of Videos and Articles from Model and loading only allowed content to List.

    :param content_objects: list
    :param subscription_active: bool
    :param user_is_staff: bool
    :return: List of Articles and Videos Objects
    """
    if user_is_staff:
        return content_objects
    elif subscription_active:
        premium_content = []
        for content_object in content_objects:
            if not content_object.draft:
                premium_content.append(content_object)
        return premium_content
    else:
        free_content = []
        for content_object in content_objects:
            if not content_object.draft and not content_object.premium_content:
                free_content.append(content_object)
        return free_content
