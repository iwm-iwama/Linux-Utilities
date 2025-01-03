#!/usr/bin/env ruby
#coding:utf-8
# Ver.iwm20250102

require "io/console"

# 必要なパッケージをインストール
%x(iwm_SubPkgInstall "yad")

print "\033[2J", "\033[1;1H"
puts
$Title = "整形する *.desktop ファイル？"
puts "\033[93m#{$Title}\033[0m"

Signal.trap(:INT) do
	exit
end

def SubExit()
	puts
	print "(END)"
	STDIN.getch
	puts
	exit
end

LN = "-" * 60

$AryFn = %x(
	yad --file \
		--multiple \
		--filename="#{Dir.getwd}" \
		--file-filter=".desktop | *.desktop" \
		--separator="\t" \
		--button="Cancel:1" --button="OK:0" \
		--title="#{$Title}" \
		--width="640" --height="480" --borders="4" --center --on-top \
		2>/dev/null \
).strip.split("\t")

if $AryFn.size > 0
	$AryFn.sort!

	$AryFn.delete_if do |_s1|
		Dir.exist?(_s1)
	end

	$AryFn.each do |_s1|
		puts "> \033[95m#{_s1}\033[0m"
	end
else
	SubExit()
end

puts LN
$Title = "テスト実行"
puts "\033[93m#{$Title}\033[0m"

$AryResult = []

$AryFn.each do |_s1|
	_sIn = ""
	File.read(_s1).split("\n").each do |_s2|
		_s2.strip!
		if _s2.length > 0
			_sIn << "#{_s2}\n"
		end
	end

	# "[Desktop Entry]" などが対象
	# "Name[ja]=..." にはヒットさせない
	_sOut = ""
	_sIn.split(/^\[/).each do |_s2|
		if _s2.length > 0
			_a2 = _s2.split("\n")
			_sOut << "[#{_a2[0]}\n#{_a2[1..].sort.join("\n")}"
		end
	end
	$AryResult << [_s1, _sOut]
end

$AryResult.each do |_a1|
	puts "> \033[95m#{_a1[0]}"
	puts "\033[96m#{_a1[1]}\033[0m"
	puts
end

puts LN
print "\033[95m実行しますか \033[97m\033[45m Yes=1 \033[49m\n\033[95m?\033[97m "
if STDIN.gets.strip != "1"
	SubExit()
end

# 元のファイルに上書き
$AryResult.each do |_a1|
	File.write(_a1[0], "#{_a1[1]}\n")
end

SubExit()
