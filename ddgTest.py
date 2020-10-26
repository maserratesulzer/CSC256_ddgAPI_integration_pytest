import requests, pytest


presidentsList = [
    'George Washington',
    'John Adams',
    'Thomas Jefferson',
    'James Madison',
    'James Monroe',
    'John Quincy Adams',
    'Andrew Jackson',
    'Martin Van Buren',
    'William Henry Harrison',
    'John Tyler',
    'James K. Polk',
    'Zachary Taylor',
    'Millard Fillmore',
    'Franklin Pierce',
    'James Buchanan',
    'Abraham Lincoln',
    'Andrew Johnson',
    'Ulysses S. Grant',
    'Rutherford B. Hayes',
    'James Garfield',
    'Chester A. Arthur',
    'Grover Cleveland',
    'Benjamin Harrison',
    'Grover Cleveland',
    'William McKinley',
    'Theodore Roosevelt',
    'William Howard Taft',
    'Woodrow Wilson',
    'Warren G. Harding',
    'Calvin Coolidge',
    'Herbert Hoover',
    'Franklin D. Roosevelt',
    'Harry S. Truman',
    'Dwight D. Eisenhower',
    'John F. Kennedy',
    'Lyndon B. Johnson',
    'Richard M. Nixon',
    'Gerald R. Ford',
    'James Carter',
    'Ronald Reagan',
    'George H. W. Bush',
    'William J. Clinton',
    'George W. Bush',
    'Barack Obama',
    'Donald J. Trump']
presidentsList = list(set(presidentsList))

# list of president's last names
presidents_last_names = [name.split()[-1] for name in presidentsList]


# query and get the results from duck duck go
url_ddg = "https://api.duckduckgo.com"
query = "presidents of the united states"
resp = requests.get(url_ddg + '/?q=' + query + '&format=json')
if resp == None:
    print('Error: "' + url_ddg + '/?q=' + query + '&format=json" returned None')
    exit(1)
data_json = resp.json()
related_topics = data_json['RelatedTopics']
texts = [topic['Text'].split(' - ')[0] for topic in related_topics]


@pytest.fixture
def texts_copy():
    return texts[:]

def get_index(astring, alist):
    if len(alist) == 0:
        raise IndexError('Empty list.')
    for i, val in enumerate(alist):
        if astring in val:
            return i
    return -1


def test_ddg_get_all_presidents_by_last_name(texts_copy):
    """without repeating them"""
    for name in presidents_last_names:
        name_index = get_index_with_string(name, texts_copy)
        assert name_index != -1, name + ' not found.'
        del texts_copy[name_index]