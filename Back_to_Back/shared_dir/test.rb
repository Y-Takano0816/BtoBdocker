# /autoware.aiに移動して
# find -name interface.yaml > all_interface_files.txt
# を実行

open("all_interface_files.txt").each{|file_name|
	tmp = []
	flag = false
	open(file_name.to_s.chomp).each{|line|
		tmp << line
		flag = true if line.index("publish")
	}
	next if !flag
	tmp.each{|line| puts line} 
}