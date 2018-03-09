
import subprocess

# open dictionaries in MS windows
dictionaries = [
'https://www.merriam-webster.com/dictionary/discipline',
'https://www.collinsdictionary.com',
'https://www.etymonline.com/',
'https://en.oxforddictionaries.com/definition/subject',
'https://dictionary.cambridge.org/zhs/词典/英语-汉语-简体/discipline',
]

for dictionary in dictionaries:
    cmd = ['start', ]
    cmd.append(dictionary)
    subprocess.run(cmd)


