from ddd import test


@test.route('/')
@test.route('/index')
def home():
    return "Test World!"
