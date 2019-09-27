from git import Repo
import sys
import emoji
from colorama import Fore, init
from random import choice
import click
from os import path, getcwd

@click.command()
@click.option('--revision', '-r', type=click.STRING, default=None,
                help='specify a commit hash to praise back in time')
@click.argument('files', nargs=-1, type=click.Path(exists=True, dir_okay=False, readable=True))
def praise(revision, files):
    '''Sometimes you have no-one to blame, spread the love.'''

    repo = Repo('.', search_parent_directories=True)
    init()
    colors =  [Fore.MAGENTA, Fore.LIGHTGREEN_EX, Fore.RED, Fore.BLUE, Fore.CYAN, Fore.GREEN]
    heart_names = [':blue_heart:', ':green_heart:', ':yellow_heart:', ':purple_heart:', ':orange_heart:']
    hearts = [emoji.emojize(heart) for heart in heart_names]
    knowns = {}

    for file in files:
        abs_filepath = file if path.isabs(file) else path.join(getcwd(), file)
        blames = repo.blame(revision, abs_filepath)

        for blame in blames:
            for line in blame[1]:
                email = blame[0].author.email
                if email not in knowns.keys():
                    knowns[email] = [ choice(hearts), choice(colors) ]
                if blame[0].hexsha == b'0000000000000000000000000000000000000000'.decode():
                    print("%s %s%s %s %s : %s%s" %
                        ('0' * 8,
                        emoji.emojize(':broken_heart:') * 5,
                        Fore.YELLOW,
                        " ---- Not commited yet! ---- ",
                        emoji.emojize(':broken_heart:') * 5,
                        line,
                        Fore.RESET
                        )
                        )
                else:
                    print("%s %s %s %s - %s %s %s : %s" % 
                        (blame[0].hexsha[:8],
                        knowns[email][0],
                        knowns[email][1],
                        blame[0].author.name[:15].ljust(15, ' '),
                        blame[0].committed_datetime,
                        Fore.RESET,
                        knowns[email][0],
                        line))

if __name__ == '__main__':
    praise()
