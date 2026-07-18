from storage import load_members, save_members


def add_member(member):
    members = load_members()
    members.append(member)
    save_members(members)


def get_members():
    return load_members()
