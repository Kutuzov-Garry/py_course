# Igor Lab-14 Config.

import configparser


def main():
    config = configparser.ConfigParser()
    print(config.read("my_conf.ini"))


    print("Sections:", config.sections(),"\n")
    print()
    print("ADMIN section:")
    print("User email :", config['admin']['usr_email'])
    print("User name :", config["admin"]["usr_name"])
    print("User password :", config["admin"]["usr_pass"])
    print()
    print("FILES section:")
    print("Old file:", config["files"]["source"])
    print("New file:", config["files"]["dist"])


if __name__ == "__main__":
    main()

# ADMIN section:
# User email : kolyan@mail.ru
# User name : kolya_kot
# User password : my_strong_pass
# 
# FILES section:
# Old file: data_from_serv.xml
# New file: data_after_proc.xml
