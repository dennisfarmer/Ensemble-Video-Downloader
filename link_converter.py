#!/usr/bin/env python3

import pyperclip
import re
import os

# sudo apt install libgl1-mesa-glx
# python -m pip install PyQt5
# python -m pip install pyperclip

# f.seek(0) to go to beginning of file
# f.readline().replace("\n", "")

def convert_url(old_url):
    if "https://cloud.ensemblevideo.com/app/plugin/embed.aspx?" in old_url:
        # Convert link to "Full Player" link
        content_id = re.search(r"&idn_content=(.*?)&", old_url).group(1)
        new_url = f"https://cloud.ensemblevideo.com/hapi/v1/contents/{content_id}/launch?&displayDownloadIcon=True"
    else:
        new_url = re.sub(r".?((?:[Ll]aunch)\?.*|(?:[Pp]lugin)\?.*)",
                    r"/launch?&displayDownloadIcon=True",
                    old_url
                    )
    return new_url

def main():
    file_url = "/mnt/c/Users/denni/Downloads/coursework/MTH160/ensemble.txt"
    option = ""
    file_line = ""
    print("Q to exit")
    option = input("Enter to load from clipboard, or F to read from file: ")
    while option.upper() != "Q":
        if option.upper() == "F":
            # check if file exist and is not empty
            if os.path.exists(file_url) and os.stat(file_url).st_size != 0:
                f = open(file_url, "r")
                old_url = f.readline().replace("\n", "")
                f.close()
                new_url = convert_url(old_url)
                f = open(file_url, "w")
                f.write(new_url)
                f.close()
            else:
                print("File empty or does not exist:", url, sep=" ")
        else:
            new_url = convert_url(pyperclip.paste())
            pyperclip.copy(url)
        option = input("Enter to load from clipboard, or F to read from file: ")

# cloud.ensemblevideo
# https://cloud.ensemblevideo.com/hapi/v1/contents/e5ee9fb7-8a1e-48f2-9e4d-2ac8a77c2478/launch?&displayDownloadIcon=True

if __name__ == "__main__":
    main()

