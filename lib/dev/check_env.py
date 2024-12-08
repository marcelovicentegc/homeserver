from env.get_login_info import host, user

def check_env_variables():
    if not host:
        print("Warning: HS_HOST environment variable is not set.")
    if not user:
        print("Warning: HS_USER environment variable is not set.")

if __name__ == "__main__":
    check_env_variables()