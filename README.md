# Git praise

Like git blame, except it's the opposite.

## install

It's still heavy WIP, so it's not on pypi (yet), it's already perfectly usable (except for really ugly error messages).

- Just clone the repo. And `cd` to its directory
- run 'pip install --user .' (or run it in a venv)
- add `praise=!'path_to_gitpraise'` to your `.gitconfig` file. (run `which gitpraise` if you don't know about it)
- share some love

## use

FIXME `--help` on a git alias will just give info about the alias. 

Run `gitpraise --help` (so it circumvent the call to git), for help.

Here's a copy:

```
Usage: gitpraise [OPTIONS] [FILES]...

  Sometimes you have no-one to blame, spread the love.

  Options:
    -r, --revision TEXT  specify a commit hash to praise back in time
    --help               Show this message and exit.
```

## demo

![screenshot](http://i.imgur.com/xhtsZfH.png)
