import random
import string

URL_DOMAIN = 'http://prnt.sc'

def gen_random_sequence():
    return '{ltr_1}{num_1:03}{ltr_2}{num_2}'.format(
        ltr_1=random.choice(string.ascii_lowercase),
        num_1=random.randint(100, 999),
        ltr_2=random.choice(string.ascii_lowercase),
        num_2=random.randint(1, 9),
    )

def get_random_url():
    return '{url}/{seq}'.format(
        url=URL_DOMAIN,
        seq=gen_random_sequence(),
    )


if __name__ == '__main__':
    print(get_random_url())