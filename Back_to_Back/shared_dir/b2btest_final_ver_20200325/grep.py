import re
import yaml


# if len(sys.argv) < 2:
#         print('ERROR: 引数にAutowareのPathを指定してください')
#         exit()
# import_path = sys.argv[1] #テストしたいAutowareのPathを取得

import_path = './result_ruby' #入力元のファイルを指定
output_path = './config.yaml' #出力先のファイルを指定	


with open(import_path) as f:
	with open(output_path, 'w') as f2:
		yaml_data = yaml.safe_load(f) #yamlファイルとして読み込む
		# print(yaml_data)
		print('root:', file=f2) #出力先ファイルに書き込む

		for node in yaml_data:
			# print(node)
			node_name = re.sub('^/','',node['name']) # 正規表現を使った置換
			print('    '+ node_name + ':', file=f2) #出力先ファイルに書き込む

			line = '        input: \"\'' + node_name + '_topics.bag\''
			if 'publish' in node:
				for topic_name in node['publish']:
					line += ', \'' + topic_name + ':=' + topic_name + '_test\''
			line += '\"'
			print(line, file=f2) #出力先ファイルに書き込む

			line = '        output: ['
			if 'publish' in node:
				add_comma = False
				for topic_name in node['publish']:
					topic_name = re.sub('^/','', topic_name) # 正規表現を使った置換
					if add_comma:
						line += ','
					add_comma = True
					line += '\'' + topic_name + '\''
			line += ']'
			print(line, file=f2) #出力先ファイルに書き込む

