#!/usr/bin/env python3
#coding:utf-8

PROGRAM = "YT-DLP+Tkinter"
VERSION = "Ver.iwm20250102"

import os
import shutil
import subprocess
import sys
import time
import tkinter as Tk
import tkinter.scrolledtext as Tk_St
import tkinter.ttk as Tk_Ttk

from ctypes import *
from ctypes.wintypes import *
from tkinter import messagebox

#-------------------------------------------------------------------------------
# My Config
#-------------------------------------------------------------------------------
# YT-DLP Command & Option
LIST_COMMAND = """
yt-dlp -f bestvideo*+bestaudio/best
yt-dlp -x --audio-format mp3
yt-dlp --help
echo
wget -rH -nc
"""

#-------------------------------------------------------------------------------
# W0 = Window[0]
#-------------------------------------------------------------------------------
class _Terminal:
	def Help():
		BG = " " * 60
		print(
			"\033[97;44m" +
			BG +
			"\033[2G" +
			"簡易ヘルプ" +
			"\033[0m" +
			"\n" +
			"\n" +
			"\033[2G" +
			"\033[93m" +
			"YT-DLP コマンド／オプション" +
			"\n" +
			"\n" +
			"\033[4G" +
			"\033[96m" +
			"yt-dlp -f bestvideo*+bestaudio/best" +
			"\n" +
			"\033[6G" +
			"\033[97m" +
			"動画ファイルを最高画質でダウンロード" +
			"\n" +
			"\n" +
			"\033[4G" +
			"\033[96m" +
			"yt-dlp -x --audio-format mp3" +
			"\n" +
			"\033[6G" +
			"\033[97m" +
			"音声ファイルをMC3でダウンロード" +
			"\n" +
			"\n" +
			"\033[4G" +
			"\033[96m" +
			"yt-dlp --help" +
			"\n" +
			"\033[6G" +
			"\033[97m" +
			"オプション・ヘルプ" +
			"\n" +
			"\n" +
			"\033[97;44m" +
			BG +
			"\033[2G" +
			"END" +
			"\033[0m" +
			"\n"
		)

	def Clear():
		# おまじない
		subprocess.run("clear || cls", shell = True)

	def YtDlp_Update():
		_Terminal.Clear()
		Cmd = "yt-dlp"
		if shutil.which(Cmd):
			rtn = messagebox.askyesno(PROGRAM, "YT-DLP の更新を確認しますか ?")
			if rtn == True:
				print(
					"\033[38;2;255;192;0m" +
					subprocess.run(
						(Cmd + " --update-to nightly"),
						shell = True,
						capture_output = True,
						text = True
					).stdout.strip() +
					"\033[0m"
				)
			print()
			_Terminal.Help()
		else:
			print(
				"\033[97;41m " +
				"YT-DLP は以下のサイトから入手できます。" +
				" \033[0m" +
				"\n" +
				"\033[5G" +
				"\033[97m" +
				"https://github.com/yt-dlp/yt-dlp#release-files" +
				"\n" +
				"\033[9G" +
				"\033[96m" +
				"Recommended（推奨版）" +
				"\033[0m"
			)

class _W0:
	#---------
	# 前処理
	#---------
	# ダイアログは最前面に "固定表示されない" ので別途表示
	_Terminal.YtDlp_Update()

	#-----
	# W0
	#-----
	global W0
	W0 = Tk.Tk()

class _C11:
	global C11
	C11 = Tk.Label(
		text = "YT-DLP コマンド",
		font = ("TkFixedFont", 9, "bold"),
		fg = "white",
		bg = "#555"
	)
	C11.place(x = 5, y = 4)

class _C21:
	def Clear(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			if select_all == True:
				obj.delete("0", "end")
			else:
				obj.delete("sel.first", "sel.last")
		return inner

	def Copy(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all == True:
				obj.clipboard_append(obj.get())
			else:
				obj.clipboard_append(obj.selection_get())
		return inner

	def Cut(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all == True:
				obj.clipboard_append(obj.get())
				obj.delete("0", "end")
			else:
				obj.clipboard_append(obj.selection_get())
				obj.delete("sel.first", "sel.last")
		return inner

	def Paste(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			text = obj.selection_get(selection = "CLIPBOARD").rstrip()
			if select_all == True:
				pass
			else:
				obj.delete("sel.first", "sel.last")
			obj.insert("insert", text)
		return inner

	def Button_1(e):
		try:
			global C21_ContextMenu
			C21_ContextMenu.destroy()
		except:
			pass

	def ButtonRelease_1(e):
		obj1 = Tk.Menu(W0, tearoff = 0, font = ("TkFixedFont", 10))
		if C21.selection_present():
			obj1.add_command(label = "クリア", command = _C21.Clear(obj = C21, select_all = False))
			obj1.add_separator()
			obj1.add_command(label = "コピー", command = _C21.Copy(obj = C21, select_all = False))
			obj1.add_command(label = "カット", command = _C21.Cut(obj = C21, select_all = False))
			obj1.add_command(label = "ペースト", command = _C21.Paste(obj = C21, select_all = False))
		obj1.post(e.x_root, e.y_root)
		global C21_ContextMenu
		C21_ContextMenu = obj1

	def Button_3(e):
		obj1 = Tk.Menu(W0, tearoff = 0, font = ("TkFixedFont", 10))
		obj1.add_command(label = "全クリア", command = _C21.Clear(obj = C21, select_all = True))
		obj1.add_separator()
		obj1.add_command(label = "全コピー", command = _C21.Copy(obj = C21, select_all = True))
		obj1.add_command(label = "全カット", command = _C21.Cut(obj = C21, select_all = True))
		obj1.add_command(label = "ペースト", command = _C21.Paste(obj = C21, select_all = True))
		obj1.post(e.x_root, e.y_root)
		global C21_ContextMenu
		C21_ContextMenu = obj1

	a1 = LIST_COMMAND.strip().split("\n")

	global C21
	C21 = Tk_Ttk.Combobox(
		W0,
		font = ("TkFixedFont", 11),
		values = (a1)
	)
	C21.place(x = 5, y = 23, height = 20)
	C21.bind("<Button-1>", Button_1)
	C21.bind("<ButtonRelease-1>", ButtonRelease_1)
	C21.bind("<Button-3>", Button_3)
	C21.insert("end", a1[0])

class _C22:
	def Click(e = None):
		_Terminal.Clear()
		TmBgn = time.time()
		s1 = C41.get("1.0", "end-1c").strip()
		s2 = C21.get().strip()
		a1 = []
		if len(s1) > 0:
			for _opt in s1.split("\n"):
				_opt = _opt.strip()
				if len(_opt) > 0:
					# DLファイル名の文字数制限
					#   (例) "あ" = １文字／3byte
					#     255 / 3 ≒ 85 > 80
					#     80 - DLフォルダ長
					_opt += f" --trim-filenames {(80 - len(os.getcwd()))}"
					# エラーになる文字を変換
					a1 += [(s2 + " " + _opt.replace("&", "%26"))]
		else:
			a1 += [s2]
		List_PS = []
		Cnt = 0
		for _s1 in a1:
			Cnt += 1
			print(f"\033[97;44m({Cnt}) {_s1} \033[0m")
			try:
				# Linux対応
				# NG: _ps = subprocess.Popen(_s1, shell=False)
				_ps = subprocess.Popen(_s1.split(), shell=False)
				# 同期／非同期
				if C23_Var.get() == 1:
					# 終了待ち
					_ps.wait()
				else:
					# PSリスト作成
					List_PS.append(_ps)
			except:
				print(
					"\033[91m" +
					"[Err] コマンドを間違っていませんか？"
				)
		# 終了処理
		for _ps in List_PS:
			_ps.wait()
		TmEnd = time.time()
		s1 = "counts" if Cnt > 1 else "count"
		s2 = "(%.3f sec)" % (TmEnd - TmBgn)
		print(f"\n\033[97;44m(END) {Cnt} {s1} {s2} \033[0m")
		print()

	global C22
	C22 = Tk.Button(
		W0,
		text = "実行",
		font = ("TkFixedFont", 9),
		fg = "#fff",
		bg = "crimson",
		highlightthickness = 0,
		relief = "flat",
		cursor = "hand2",
		command = Click
	)
	C22.place(y = 23, width = 62, height = 20)

class _C23:
	global C23, C23_Var
	C23_Var = Tk.IntVar()
	C23 = Tk.Checkbutton(
		W0,
		text = "同期処理",
		font = ("TkFixedFont", 9),
		fg = "#fff",
		bg = "#555",
		highlightthickness = 0,
		cursor = "hand2",
		selectcolor = "#111",
		variable = C23_Var
	)
	C23.place(y = 23, width = 75, height = 20)

# C41 < C32, C32
class _C41:
	def Clear(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			if select_all == True:
				obj.delete("1.0", "end")
			else:
				obj.delete("sel.first", "sel.last")
		return inner

	def Copy(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all == True:
				obj.clipboard_append(obj.get("1.0", "end-1c"))
			else:
				obj.clipboard_append(obj.get("sel.first", "sel.last"))
		return inner

	def Cut(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			obj.clipboard_clear()
			if select_all == True:
				obj.clipboard_append(obj.get("1.0", "end-1c"))
				obj.delete("1.0", "end")
			else:
				obj.clipboard_append(obj.get("sel.first", "sel.last"))
				obj.delete("sel.first", "sel.last")
		return inner

	def Paste(obj = None, select_all = False, e = None):
		if obj == None:
			return
		def inner():
			text = obj.selection_get(selection = "CLIPBOARD").rstrip()
			if select_all == True:
				pass
			else:
				obj.delete("sel.first", "sel.last")
			obj.insert("insert", text)
			obj.see("insert")
		return inner

	def Add(obj = None, e = None):
		if obj == None:
			return
		def inner():
			s1 = obj.get("1.0", "end").strip()
			if len(s1) > 0:
				s1 += "\n"
			obj.delete("1.0", "end")
			s2 = ""
			try:
				s2 = obj.selection_get(selection = "CLIPBOARD").strip()
				if len(s2) > 0:
					s2 += "\n"
			except:
				pass
			obj.insert("insert", (s1 + s2))
			obj.see("insert")
		return inner

	def Button_1(e):
		try:
			global C41_ContextMenu
			C41_ContextMenu.destroy()
		except:
			pass

	def ButtonRelease_1(e):
		obj1 = Tk.Menu(W0, font = ("TkFixedFont", 10), tearoff = 0)
		if C41.tag_ranges("sel"):
			obj1.add_command(label = "クリア", command = _C41.Clear(obj = C41, select_all = False))
			obj1.add_separator()
			obj1.add_command(label = "コピー", command = _C41.Copy(obj = C41, select_all = False))
			obj1.add_command(label = "カット", command = _C41.Cut(obj = C41, select_all = False))
			obj1.add_command(label = "ペースト", command = _C41.Paste(obj = C41, select_all = False))
		obj1.post(e.x_root, e.y_root)
		global C41_ContextMenu
		C41_ContextMenu = obj1

	def Button_3(e):
		obj1 = Tk.Menu(W0, font = ("TkFixedFont", 10), tearoff = 0)
		obj1.add_command(label = "全クリア", command = _C41.Clear(obj = C41, select_all = True))
		obj1.add_separator()
		obj1.add_command(label = "全コピー", command = _C41.Copy(obj = C41, select_all = True))
		obj1.add_command(label = "全カット", command = _C41.Cut(obj = C41, select_all = True))
		obj1.add_command(label = "ペースト", command = _C41.Paste(obj = C41, select_all = True))
		obj1.post(e.x_root, e.y_root)
		global C41_ContextMenu
		C41_ContextMenu = obj1

	global C41
	C41 = Tk_St.ScrolledText(
		W0,
		font = ("Courier", 12),
		relief = "flat",
		borderwidth = 0,
		undo = "true",
		insertofftime = 0
	)
	C41.place(x = 5, y = 73)
	C41.bind("<Button-1>", Button_1)
	C41.bind("<ButtonRelease-1>", ButtonRelease_1)
	C41.bind("<Button-3>", Button_3)
	C41.configure(state = "normal")

class _C31:
	global C31
	C31 = Tk.Label(
		text = "YouTube URL（改行区切り）",
		font = ("TkFixedFont", 9, "bold"),
		fg = "white",
		bg = "#555"
	)
	C31.place(x = 5, y = 52)

class _C32:
	global C32
	C32 = Tk.Button(
		W0,
		text = "クリア",
		font = ("TkFixedFont", 9),
		fg = "white",
		bg = "navy",
		highlightthickness = 0,
		relief = "flat",
		cursor = "hand2",
		command = _C41.Clear(obj = C41, select_all = True)
	)
	C32.place(y = 53, width = 70, height = 20)

class _C33:
	global C33
	C33 = Tk.Button(
		W0,
		text = "ペースト",
		font = ("TkFixedFont", 9),
		fg = "white",
		bg = "mediumblue",
		highlightthickness = 0,
		relief = "flat",
		cursor = "hand2",
		command = _C41.Add(obj = C41)
	)
	C33.place(y = 53, width = 75, height = 20)

class _W0_Main:
	def Resize(e):
		if e.widget is W0:
			C21.place(width = e.width - 155)
			C22.place(x = e.width - 149)
			C23.place(x = e.width - 83)
			C32.place(x = e.width - 149)
			C33.place(x = e.width - 79)
			C41.place(width = e.width - 10, height = e.height - 79)

	# Window 初期サイズ
	min = {
		"W": 480,
		"H": 240
	}
	# Window 初期ポジション
	pos = {
		"X": int((W0.winfo_screenwidth() - min["W"]) / 2),
		"Y": int((W0.winfo_screenheight() - min["H"]) / 2)
	}
	W0.bind("<Configure>", Resize)
	W0.configure(bg = "#555")
	W0.geometry(f'{min["W"]}x{min["H"]}+{pos["X"]}+{pos["Y"]}')
	W0.minsize(width = min["W"], height = min["H"])
	W0.resizable(width = True, height = True)
	W0.title(PROGRAM + " " + VERSION)
	# 使用不可：Windows, Linux 互換問題
	#   W0.attributes()

	#---------------
	# 表示位置変更
	#---------------
	# Windows以外で例外発生
	try:
		hwnd = windll.user32.GetForegroundWindow()
		windll.user32.MoveWindow(
			hwnd,
			30,
			60,
			int((W0.winfo_screenwidth() / 2) - 240),
			int(W0.winfo_screenheight() - 120),
			True
		)
	except(NameError, SyntaxError):
		pass

	#---------------------------------
	# 引数のファイル名からリスト読込
	#---------------------------------
	AryC41 = []
	for _s1 in sys.argv:
		AryC41.append(_s1.strip())
	del AryC41[0]
	for _s1 in AryC41:
		try:
			with open(_s1) as iFs:
				C41.insert("insert", iFs.read().rstrip() + "\n")
		except:
			pass
	C41.see("insert")

	#-------------
	# フォーカス
	#-------------
	C21.focus_force()

	#-------
	# Main
	#-------
	W0.mainloop()
	W0.quit()

