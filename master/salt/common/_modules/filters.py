# https://docs.saltstack.com/en/latest/topics/tutorials/jinja_to_execution_module.html#tutorial-jinja-to-execution-module
# https://github.com/saltstack/salt/issues/26792#issuecomment-268139623
#
# N.B., filter changes must be synced across minions `salt '*' saltutil.sync_modules`

# {% set fruit = ['apples', 'bananas'] %}
#
# moduletest:
#    cmd.run:
#        - name: echo I like {{ salt.filters.format_list(fruit, '--subset %s') | join(' ') }}
def format_list(list_, pattern):
    return [pattern % s for s in list_]
