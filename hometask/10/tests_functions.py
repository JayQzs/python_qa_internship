from response import Response

def test_getting_user_list(get_users):
    Response(get_users).assert_status_code(200)

def test_creating_user(create_user):
    Response(create_user).assert_status_code(201)

def test_find_user(find_user):
    Response(find_user).assert_status_code(200)