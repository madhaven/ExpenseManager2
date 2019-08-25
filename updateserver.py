try:
    from os import listdir, system, path
    
    fromloc=input('Enter files location : ')
    if fromloc and fromloc[-1]!='\\':fromloc=fromloc+'\\'
    if fromloc:fromfiles=listdir(fromloc)
    else:fromfiles=listdir()
    toloc=input('Enter server location : ')
    if toloc and toloc[-1]!='\\':toloc=toloc+'\\'
    tofiles=listdir(toloc)
    fileexists=False
    
    print('\nFiles to be copied')
    for x in fromfiles:print(x);fileexists=True
    if not fileexists:print('--none--')
    fileexists=False
    print('\nFiles in location')
    for x in tofiles:print(x);fileexists=True
    if not fileexists:print('--none--')
    fileexists=False
    
    print()
    for x in fromfiles:
        if x in tofiles:
            print(x)
            fileexists=True
    if (fileexists) and ('n' in input('\nReplace files? : ')): exit()
    for x in fromfiles:
        if x!=path.basename(__file__):
            if fromloc:system('copy %s\\%s %s\\%s'%(fromloc, x, toloc, x))
            else:system('copy %s %s\\%s'%(x, toloc, x))
    input('\nServer Updated')
except Exception as e: input(e)
