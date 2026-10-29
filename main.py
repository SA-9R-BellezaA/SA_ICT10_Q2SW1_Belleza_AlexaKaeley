from pyscript import document

club_members = [
    "Patrick Star",
    "Sandy Cheeks",
    "Mrs. Puff",
    "Larry Lobster",
    "Squilliam Fancyson",
    "Bubble Bass",
    "Mermaid Man",
    "Barnacle Boy",
    "Sheldon Plankton",
    "Old Man Jenkins",
]


def check_member(event):
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()
    full_name = f"{first_name} {last_name}".strip().title()

    # The "in" check gives true or False. And this is stored in a variable as a result.
    is_member = full_name in club_members

    
    messages = {
        True: f"Congratulations {full_name}! You are indeed a Krusty Krab customer.",
        False: f"Sorry {full_name}, your name is not on the list.",
    }

    document.querySelector("#output").innerText = messages[is_member]