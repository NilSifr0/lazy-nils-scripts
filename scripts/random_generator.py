import secrets
import string


def random_generator():
    # return 10 random chars
    alphabet = (
        string.ascii_letters
        + string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.hexdigits
        + string.octdigits
        + string.printable
        + string.punctuation
        + string.whitespace
    )
    content = [
        secrets.choice(string.ascii_letters),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.hexdigits),
        secrets.choice(string.octdigits),
        secrets.choice(string.printable),
        secrets.choice(string.punctuation),
        secrets.choice(string.whitespace),
    ]
    content += [secrets.choice(alphabet) for _ in range(1)]
    secrets.SystemRandom().shuffle(content)

    return "".join(content)


with open("text_file.txt", "a", encoding="utf-8") as file:
    length = 1000000
    for _ in range(length):
        chunk = random_generator()
        file.write(chunk)
    # print((secrets.choice(alphabet)) * length)
    # file.write(final_stuff)
