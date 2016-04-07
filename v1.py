import sys
import argparse
from teamrooms import teamroom
from workflow import Workflow, ICON_WEB, ICON_WARNING, web, PasswordNotFound

log = None


def upperfirst(x):
    return x[0].upper() + x[1:]


def make_query(url, api_key, params=dict(sel="Name")):
    headers = dict(Authorization=api_key, Accept="application/json")
    r = web.get(url, params, headers)
    r.raise_for_status()

    return r.json()


def get_by_asset_type(url, api_key, asset_type):
    asset_type = upperfirst(asset_type)[:-1]
    query_url = url + 'rest-1.v1/Data/' + asset_type
    assets = make_query(query_url, api_key)["Assets"]
    for asset in assets:
        oid = asset['id']
        name = asset['Attributes']['Name']['value']
        arg_to_pass_on_enter_click = url + asset_type + '.mvc/Summary?oidToken=' + oid
        wf.add_item(title=name, subtitle=oid, arg=arg_to_pass_on_enter_click, valid=True, icon=ICON_WEB)
    wf.send_feedback()
    return 0


def get_by_oid(url, api_key, oid):
    asset_type = upperfirst(oid.split(':')[0])
    asset_number = oid.split(':')[1]
    query_url = url + 'rest-1.v1/Data/' + asset_type + '/' + asset_number
    asset = make_query(query_url, api_key)
    oid = asset['id']
    name = asset['Attributes']['Name']['value']
    arg_to_pass_on_enter_click = url + asset_type + '.mvc/Summary?oidToken=' + oid
    wf.add_item(title=name, subtitle=oid, arg=arg_to_pass_on_enter_click, valid=True, icon=ICON_WEB)
    wf.send_feedback()
    return 0


def get_by_name(url, api_key, query):
    asset_type = upperfirst(query.split(' ', 1)[0])
    name = query.split(' ', 1)[1]
    params = dict(where="Name='" + name + "'")
    query_url = url + 'rest-1.v1/Data/' + asset_type
    assets = make_query(query_url, api_key, params)["Assets"]
    for asset in assets:
        oid = asset['id']
        name = asset['Attributes']['Name']['value']
        arg_to_pass_on_enter_click = url + asset_type + '.mvc/Summary?oidToken=' + oid
        wf.add_item(title=name, subtitle=oid, arg=arg_to_pass_on_enter_click, valid=True, icon=ICON_WEB)
    wf.send_feedback()
    return 0


def main(wf):
    parser = argparse.ArgumentParser()
    parser.add_argument('--seturl', dest='url', nargs='?', default=None)
    parser.add_argument('--setkey', dest='apikey', nargs='?', default=None)
    parser.add_argument('query', nargs='?', default=None)
    args = parser.parse_args(wf.args)

    if args.url:
        wf.settings['url'] = args.url
        return 0

    url = wf.settings.get('url', None)
    if not url:
        wf.add_item('Set VersionOne Url', 'Please use v1url to set your instace url', valid=False, icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    if args.apikey:
        wf.save_password('api_key', args.apikey)
        return 0

    try:
        api_key = wf.get_password('api_key')
    except PasswordNotFound:
        wf.add_item('Set API Token', 'Please use v1token to set your API token', valid=False, icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    query = args.query
    if query:
        if query == 'teamroom lobby':
            teamroom.open_lobby(url)
        elif query.startswith('teamroom'):
            team_room_name = query.split('teamroom ')[1]
            teamroom.open_team_room(url, api_key, team_room_name)
        elif ":" in query:
            get_by_oid(url, api_key, query)
        elif query.endswith('s'):
            get_by_asset_type(url, api_key, query)
        else:
            get_by_name(url, api_key, query)

if __name__ == u"__main__":
    wf = Workflow()
    log = wf.logger
    sys.exit(wf.run(main))
