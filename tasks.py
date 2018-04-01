from invoke import task


@task
def lint(ctx):
    paths = 'base/ core/'
    print('pycodestyle:')
    pycodestyle = ctx.run('pycodestyle {}'.format(paths), warn=True)
    print('flake8:')
    flake8 = ctx.run('flake8 {}'.format(paths), warn=True)

    if pycodestyle.exited != 0:
        exit(pycodestyle.exited)

    if flake8.exited != 0:
        exit(flake8.exited)
