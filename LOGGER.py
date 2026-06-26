import json
from tkinter import messagebox
_____logger_license_____ = '''
MIT License

Copyright (c) 2026 AS50SB

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
_____LOGGER_LIST______ = []
class LOGGER:
    def info(msg):
        global _____LOGGER_LIST______
        print("[INFO]",msg)
        _____LOGGER_LIST______.append(f"[INFO] {msg}")
    def error(msg):
        global _____LOGGER_LIST______
        print("[ERROR]",msg)
        _____LOGGER_LIST______.append(f"[ERROR] {msg}")
    def warn(msg):
        global _____LOGGER_LIST______
        print("[WARNING]",msg)
        _____LOGGER_LIST______.append(f"[WARNING] {msg}")
    def debug(msg):
        global _____LOGGER_LIST______
        print("[DEBUG]",msg)
        _____LOGGER_LIST______.append(f"[DEBUG] {msg}")
    def show_license():
        global _____logger_license_____
        messagebox.showinfo("LOGGER Library LICENSE",_____logger_license_____)
        LOGGER.info("[LOGGER] Successfully to show license.")
    def show_log():
        global _____LOGGER_LIST______
        temp_logger_str = ""
        for i in range(len(_____LOGGER_LIST______)):
            temp_logger_str = temp_logger_str + _____LOGGER_LIST______[i] + "\n"
        messagebox.showinfo("LOGGER Library LOG", temp_logger_str)
        del temp_logger_str
        return _____LOGGER_LIST______
    def show_choose_log(log_type):
        global _____LOGGER_LIST______
        to_return_list = []
        if log_type == "info":
            for i in range(len(_____LOGGER_LIST______)):
                if "[INFO]" in _____LOGGER_LIST______[i]:
                    messagebox.info("LOGGER Library LOG",_____LOGGER_LIST______[i])
                    to_return_list.append(_____LOGGER_LIST______[i])
        elif log_type == "error":
            for i in range(len(_____LOGGER_LIST______)):
                if "[ERROR]" in _____LOGGER_LIST______[i]:
                    messagebox.error("LOGGER Library LOG",_____LOGGER_LIST______[i])
                    to_return_list.append(_____LOGGER_LIST______[i])
        elif log_type == "warn":
            for i in range(len(_____LOGGER_LIST______)):
                if "[WARNING]" in _____LOGGER_LIST______[i]:
                    messagebox.showwarning("LOGGER Library LOG",_____LOGGER_LIST______[i])
                    to_return_list.append(_____LOGGER_LIST______[i])
        elif log_type == "debug":
            for i in range(len(_____LOGGER_LIST______)):
                if "[DEBUG]" in _____LOGGER_LIST______[i]:
                    messagebox.showinfo("LOGGER Library LOG",_____LOGGER_LIST______[i])
                    to_return_list.append(_____LOGGER_LIST______[i])
        else:
            LOGGER.error("[LOGGER] Please input correct log type.")
        return to_return_list
    def clear_log():
        global _____LOGGER_LIST______
        _____LOGGER_LIST______.clear()
        return 0
    def clear_choose_log(log_type):
        global _____LOGGER_LIST______
        if log_type == "info":
            for i in range(len(_____LOGGER_LIST______)):
                if "[INFO]" in _____LOGGER_LIST______[i]:
                    del _____LOGGER_LIST______[i]
        elif log_type == "error":
            for i in range(len(_____LOGGER_LIST______)):
                if "[ERROR]" in _____LOGGER_LIST______[i]:
                    del _____LOGGER_LIST______[i]
        elif log_type == "warn":
            for i in range(len(_____LOGGER_LIST______)):
                if "[WARNING]" in _____LOGGER_LIST______[i]:
                    del _____LOGGER_LIST______[i]
        elif log_type == "debug":
            for i in range(len(_____LOGGER_LIST______)):
                if "[DEBUG]" in _____LOGGER_LIST______[i]:
                    del _____LOGGER_LIST______[i]
        else:
            LOGGER.error("[LOGGER] Please input correct log type.")
        return 0
    def clear_set_log(log_message):
        global _____LOGGER_LIST______
        # remove the first log message that matches the input log_message
        for i in range(len(_____LOGGER_LIST______)):
            if log_message == _____LOGGER_LIST______[i]:
                del _____LOGGER_LIST______[i]
                return 0
        LOGGER.error("[LOGGER] Please input correct log message.")
        return 1
    def clear_log_no(log_no):
        global _____LOGGER_LIST______
        if 0 <= log_no < len(_____LOGGER_LIST______):
            del _____LOGGER_LIST______[log_no]
        return 0
    def get_log_len():
        return len(_____LOGGER_LIST______)
    def clear_log_range(start_no, end_no):
        global _____LOGGER_LIST______
        if 0 <= start_no < len(_____LOGGER_LIST______) and 0 <= end_no < len(_____LOGGER_LIST______):
            del _____LOGGER_LIST______[start_no:end_no+1]
        return 0
    def get_log(log_no):
        global _____LOGGER_LIST______
        if 0 <= log_no < len(_____LOGGER_LIST______):
            return _____LOGGER_LIST______[log_no]
        else:
            LOGGER.error("[LOGGER] Please input correct log number.")
            return 1
    def get_logger_library_version():
        return json.loads(open("LOGGER.json","r").read())["version"]
    def logger_library_version_checker():
        if "snapshot" in LOGGER.get_logger_library_version() or "alpha" in LOGGER.get_logger_library_version() or "beta" in LOGGER.get_logger_library_version():
            LOGGER.warn("[LOGGER] LOGGER Library is not stable, please use it carefully.")
            return False
        elif "release" in LOGGER.get_logger_library_version():
            LOGGER.info("[LOGGER] LOGGER Library is stable, you can use it safely.")
            return True
        elif "dev" in LOGGER.get_logger_library_version():
            LOGGER.warn("[LOGGER] LOGGER Library is in development, please use it carefully.")
            return "dev"
        elif "april" in LOGGER.get_logger_library_version():
            LOGGER.warn("[LOGGER] LOGGER Library is a april fool, good luck :)")
            return ":)"
        else:
            LOGGER.warn("[LOGGER] LOGGER Library version is unknown, please use it carefully,if you edited LOGGER.json,pleaese redownload it!")
            return
    def show_author():
        messagebox.showinfo("LOGGER Library Author",json.load(open("LOGGER.json","r").read())["authors"])
        LOGGER.info("[LOGGER] Successfully to show author.")
LOGGER.info("[LOGGER] LOGGER Library loaded SUCCESSFUL!")