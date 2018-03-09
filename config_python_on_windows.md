

### 3.1.3. Removing the MAX_PATH Limitation

Windows historically has limited path lengths to 260 characters. This meant that paths longer than this would not resolve and errors would result.

In the latest versions of Windows, this limitation can be expanded to approximately 32,000 characters. Your administrator will need to activate the “Enable Win32 long paths” group policy, or set the registry value`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem@LongPathsEnabled` to `1`.

This allows the [`open()`](https://docs.python.org/3/library/functions.html#open) function, the [`os`](https://docs.python.org/3/library/os.html#module-os) module and most other path functionality to accept and return paths longer than 260 characters when using strings. (Use of bytes as paths is deprecated on Windows, and this feature is not available when using bytes.)

After changing the above option, no further configuration is required.

Changed in version 3.6: Support for long paths was enabled in Python.



### 3.3.1. Excursus: Setting environment variables[¶](https://docs.python.org/3/using/windows.html#excursus-setting-environment-variables)

```python
C:\>set PATH=C:\Program Files\Python 3.6;%PATH%
C:\>set PYTHONPATH=%PYTHONPATH%;C:\My_python_lib
C:\>python
```

