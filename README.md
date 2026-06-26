# LOGGER usage documentation

# English

# SOMETHING IS LEGACY MESSAGE

***LOOGER is a simple logger library for Python, it can be used to log information, errors, warnings and debug messages.***
All functions belong to the LOGGER class.

## Function List

**info(msg)** Normal information
**error(msg)** Error information
**warn(msg)** Warning information
**debug(msg)** Debug information
**show_license()** Outputs the license using tkinter.messagebox. This project is open-sourced under the MIT License and can be found at as50sb/logger-py
**show_log()** Outputs all logs using tkinter.messagebox
**clear_log()** Clears all logs and outputs one log entry
**clear_info/error/warn/debug_log()** Clears logs of the corresponding type
**clear_choose_log(log_type)** Clears logs of the type specified by log_type (info/error/warn/debug)
**clear_set_log(log_message)** Clears logs whose content matches log_message
**clear_log_no(log_no)** Clears the log at index log_no in the sequence (0-based)
**clear_log_range(start_no, end_no)** Clears logs from start_no to end_no in the sequence
**get_log(to_get_logger_no)** Gets the content of the log at index to_get_logger_no in the sequence
**get_logger_library_version()** Gets the version of LOGGER
**logger_library_version_checker()** This function runs automatically and is used to check the version type of LOGGER; it will issue a warning if it is not a stable release
**show_author()** Displays the list of authors

## JSON Content

**logger_library_class_name** Main class name. Can be checked here if changed; not referenced in code
**version** LOGGER version. Referenced in code
**authors** List of authors. Referenced in code
**license** License. Not referenced in code
**description** [Removed] Description. Not referenced in code

## License

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

## Final Reminder

**This library is not yet fully developed and contains some bugs. Please use with caution.**



# 简体中文

# 部分内容已过时！

***LOGGER是一个简单的Python日志库，它可以输出标准、报错、警告、调试日志。***
所有函数均属于LOGGER类。

## 函数列表

**info(msg)** 正常信息
**error(msg)** 报错信息
**warn(msg)** 警告信息
**debug(msg)** 调试信息
**show_license()** 使用tkinter.messagebox输出许可证，本项目采用MIT许可证开源，可在as50sb/logger-py中找到
**show_log()** 使用tkinter.messagebox输出所有日志
**clear_log()** 清空日志并输出一条日志
**clear_info/error/warn/debug_log()** 清空对应类型的日志
**clear_choose_log(log_type)** 清空类型为log_type的类型的日志（info/error/warn/debug）
**clear_set_log(log_message)** 清空内容为log_message的日志
**clear_log_no(log_no)** 清空序列中第log_no条日志（从0开始）
**clear_log_range(start_no, end_no)** 清空序列中从start_no到end_no的日志
**get_log(to_get_logger_no)** 获取序列中第to_get_logger_no条日志的内容
**get_logger_library_version()** 获取LOGGER的版本
**logger_library_version_checker()** 本函数将会自动运行，用于检查LOGGER的版本类型，若非稳定版将警告
**show_author()** 显示作者列表

## JSON内容

**logger_library_class_name** 主类名称，若有更换可在此查看，代码无引用
**version** LOGGER的版本，代码有引用
**authors** 作者列表，代码有引用
**license** 许可证，代码无引用
**description** 【已移除】介绍，代码无引用

## 许可证

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

## 最后提醒

**该库尚未开发完全，存在部分bug，请谨慎使用**
