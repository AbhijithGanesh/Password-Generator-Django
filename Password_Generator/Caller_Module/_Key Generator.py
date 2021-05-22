from .Characterizer import supplier


def password_Final():
    password = []
    b = ""
    for i in range(32):
        a = list(supplier())
        password.append(a)

    for k in range(len(password)):
        '''b += password[k][0]'''
        b += password[k][1]
        b += password[k][2]
        b += password[k][3]
    print("Your Password is:",b[0:256])


if __name__ == "__main__":
    password_Final()
