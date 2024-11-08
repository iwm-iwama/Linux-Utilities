#!/usr/bin/env ruby
#coding:utf-8

VERSION = "iwm20241103"
TITLE   = "Windowsドライブを/media/${USER}/以下にマウント"

class Class_Lsblk
	X = %x(
		LANG=C \
		lsblk \
		--raw \
		-o PARTTYPENAME,LABEL,PATH \
		| grep -E '^Microsoft\\\\x20basic\\\\x20data' \
	)

	def getAry()
		rtn = []
		X.split("\n").each do |_s1|
			rtn << _s1.strip.split(/[ ]/)
		end
		return rtn
	end

	def p()
		getAry().each do |_a1|
			Kernel.p _a1
		end
	end
end
Lsblk = Class_Lsblk.new

##Lsblk.p()

# User Name
USER = ENV["USER"]

# sudo mkdir -v /media/iwm/Windows
# sudo mount /dev/nvme0n1p3 /media/iwm/Windows
Lsblk.getAry().each do |_a1|
	_media = "/media/#{USER}/#{_a1[1]}"
	[
		"sudo mkdir -v #{_media}",
		"sudo mount #{_a1[2]} #{_media}"
	]
	.each do |_s1|
		puts _s1
		system "#{_s1} 2>/dev/null"
	end
end
