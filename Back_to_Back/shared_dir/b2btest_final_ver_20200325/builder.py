import sys
import yaml
from jinja2 import Template, Environment, FileSystemLoader
#----------------------------------------------------------------
# Convert the value of boolean to 'true' or 'false'.
# def boolstr(value):
#     if value: return 'true'
#     return 'false'
# # Convert to 0x00 format.
# def hex(value):
#     return format(value, '#04x')
#----------------------------------------------------------------
# Generate file from Jinja2 template.
def genJ2(templateFile, configFile, genFile):
    # Load template.
    env = Environment(loader=FileSystemLoader('.', encoding='utf_8_sig'))
    # env.filters['boolstr'] = boolstr
    # env.filters['hex'] = hex
    tpl = env.get_template(templateFile)
    # Load config.
    with open(configFile, encoding='utf_8_sig') as stream:
        data = yaml.load(stream)
    if len(sys.argv) < 2:
        print('ERROR: 引数にノード名を指定してください')
        exit()
    data['target_node'] = sys.argv[1] #テストしたいノード名を取得
    # Render
    render = tpl.render(data)
    # Output
    with open(genFile, 'w', encoding='utf_8_sig') as stream:
        stream.write(render)
# ----------------------------------------------------------------
genJ2('template.j2', 'config.yaml', 'source1.py')
# genJ2('template2.j2', 'config.yaml', 'source2.cpp')