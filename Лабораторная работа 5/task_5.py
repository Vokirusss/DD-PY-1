import random
import string

alphabet = string.ascii_letters + string.digits  # Add letters and digits in our alphabet


def get_random_password(pass_len: int = 8) -> str:
    password_ = "".join(random.sample(alphabet, pass_len))
    return password_


print(get_random_password())
