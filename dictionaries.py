
import subprocess

# open dictionaries 同时打开三个词典网页.
# 井号后面是注释, 程序自动忽略,不运行.
dictionaries = [
'https://dictionary.cambridge.org/zhs/词典/英语-汉语-简体/discipline',
'https://en.oxforddictionaries.com/definition/subject',
'https://www.etymonline.com/',
]

for dictionary in dictionaries:
    cmd = "start {}".format(dictionary)
    subprocess.run(cmd, shell=True)