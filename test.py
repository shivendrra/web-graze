# from graze import britannica

# brit = britannica(max_limit=20)
# brit(outfile='./outputs.txt')

from graze import wikipedia

wiki = wikipedia()
wiki(out_file='./output.txt')