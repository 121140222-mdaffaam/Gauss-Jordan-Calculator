import os
import string
import random
import numpy as np


def SPL(list, jum_baris, jum_kolom):
  for i in range(0, jum_baris):
    k = 0
    line = ""
    for j in range(0, jum_kolom):
      if j == jum_kolom - 2 and list[i, j] == 0 and line == "":
        line += '0'
      elif j != jum_kolom - 1:
        if str(list[i, j]) != '0' and str(list[i, j]) != '0.0':
          if k == 0:
            if int(list[i, j]) == 1:
              line += 'X' + str(j + 1)
            elif int(list[i, j]) == -1:
              line += '-X' + str(j + 1)
            else:
              line += str(list[i, j]) + 'X' + str(j + 1)
            k += 1
          elif int(list[i, j]) > 0:
            if int(list[i, j]) == 1:
              line += ' + X' + str(j + 1)
            else:
              line += ' + ' + str(list[i, j]) + 'X' + str(j + 1)
            k += 1
          elif int(list[i, j]) < 0:
            if list[i, j] == -1:
              line += ' - X' + str(j + 1)
            else:
              line += ' - ' + \
                  str(list[i, j] * -1) + 'X' + str(j + 1)
            k += 1
      elif j == jum_kolom - 1:
        line += ' = ' + str(list[i, j])
    print(line)
  print('')


def OutputMatriks(list, jum_baris, jum_kolom):
  for i in range(0, jum_baris):
    line = ""
    for j in range(0, jum_kolom):
      if len(str(list[i, j])) > 3:
        line += str(list[i, j]) + "\t"
      else:
        line += str(list[i, j])  + "\t"
      if j == jum_kolom - 2:
        line += "| "
    print(line)
  print('')


def sorting(list, x, jum_baris, jum_kolom):
  for i in range(0, jum_baris):
    x[i] = 0
    for j in range(0, jum_kolom - 1):
      if list[i, j] == 0:
        x[i] += 1
      else:
        break
  for i in range(0, jum_baris):
    if x[i] != 0:
      for i in range(0, jum_baris):
        j = jum_baris - 1
        while j > i:
          if x[j] < x[j - 1]:
            x[j - 1], x[j] = x[j], x[j - 1]
            for k in range(0, jum_kolom):
              list[i, k], list[j, k] = list[j, k], list[i, k]
          j -= 1
      break


def gauss(list, x, jum_baris, jum_kolom):
  for i in range(0, jum_baris):
    sorting(list, x, jum_baris, jum_kolom)
    if x[i] != jum_kolom - 1:
      temp = list[i, 0 + int(x[i])]
      for j in range(0, jum_kolom):
        if list[i, j] != 0:
          if temp != 0:
            list[i, j] /= temp
          else:
            list[i, j] = temp and list[i, j] / temp   
      for k in range(i + 1, jum_baris):
        temp1 = list[k, 0 + int(x[i])]
        for l in range(0, jum_kolom):
          list[k, l] -= (temp1 * list[i, l])
          


def gaussjordan(list, x, jum_baris, jum_kolom):
  gauss(list, x, jum_baris, jum_kolom)
  i = jum_baris - 1
  while i >= 0:
    if x[i] != jum_kolom - 1:
      for j in range(0, i):
        temp1 = list[j, 0 + int(x[i])]
        for l in range(0, jum_kolom):
          list[j, l] -= (temp1 * list[i, l])
    i -= 1


def penyelesaian(list, x, jum_baris, jum_kolom):
  #cek tipe penyelesaian
  gaussjordan(list, x, jum_baris, jum_kolom)
  tipe = 0
  for i in range(0, jum_baris):
    if x[i] == i:
      pass
    else:
      tipe = 1
      break
  if tipe == 1:
    for i in range(0, jum_baris):
      if x[i] == jum_kolom - 2 or list[i, jum_kolom - 1] == 0:
        tipe = 2
        break
      else:
        pass
  #start cari
  if tipe == 0:
    z = np.empty((jum_kolom - 1, jum_kolom))
    for i in range(0, jum_kolom - 1):
      for j in range(0, jum_kolom):
        if i == j:
          z[i, j] = 1
        else:
          z[i, j] = 0
    i = jum_baris - 1
    while i >= 0:
      j = jum_kolom - 1
      while j > x[i]:
        if j == jum_kolom - 1:
          z[i, jum_kolom - 1] += list[i, j]
        else:
          z[i, jum_kolom - 1] -= (list[i, j] * z[j, jum_kolom - 1])
        j -= 1
      i -= 1
  elif tipe == 2:
    print('Persamaan Memiliki Solusi Banyak')
    y = []
    z = np.empty((jum_kolom - 1, jum_kolom), dtype='object')
    temp = 0
    for i in range(0, jum_kolom - 1):
      if x[temp] != i:
        y.append(i)
      else:
        temp += 1
      for j in range(0, jum_kolom):
        if i == j:
          z[i, j] = '1'
        else:
          z[i, j] = '0'
    for ys in y:
      z[ys, jum_kolom - 1] = random.choice(string.ascii_letters)
    i = jum_baris - 1
    while i >= 0:
      j = jum_kolom - 1
      line = ''
      while j > x[i]:
        if j == jum_kolom - 1:
          line += str(list[i, j])
        else:
          if list[i, j] > 0:
            line += ' - ' + str(list[i, j])
          elif list[i, j] < 0:
            line += ' + ' + str(list[i, j] * -1)
          if len(z[j, jum_kolom - 1]) != 1 and list[i, j] != 0:
            line += '(' + z[j, jum_kolom - 1] + ')'
          elif list[i, j] != 0:
            line += z[j, jum_kolom - 1]
        j -= 1
      if line != '':
        z[int(x[i]), jum_kolom - 1] = str(line)
      i -= 1
  else:
    print('Persamaan Tidak Memiliki Solusi')
  SPL(z, jum_kolom - 1, jum_kolom)


def interpolasi_linear():
  n = int(input("Masukkan jumlah data = "))
  x = []
  y = []

  for i in range(n):
    x.append(float(input(f"Nilai x{i} = ")))

  print(" ")
  i = 0

  for i in range(n):
    y.append(float(input(f"Nilai y{i} = ")))

  print("")

  cari = float(input(f"Nilai f(x) yang ingin dicari, masukan nilai x = "))
  i = 0
  for i in range(n):
    if cari <= x[i]:
      print(f"x{i},y{i} = ", x[i], ',', y[i])
      print(f"x{i-1},y{i-1} = ", x[i - 1], ',', y[i - 1])
      print('\n')
      hasil = ((y[i] - y[i - 1]) /
               (x[i] - x[i - 1])) * (cari - x[i - 1]) + y[i - 1]
      print("f(x) = ", hasil)
      break



def caseD():
  penghasilan = float(input("Penghasilan  : "))
  csr = penghasilan / 10
  pajak_daerah = (penghasilan - csr) / 20
  pajak_federal = (penghasilan - csr - pajak_daerah) * 2 / 5
  print("DATA\npajak daerah :", pajak_daerah)
  print("pajak federal :", pajak_federal)
  print("CSR :", csr)
  print("SPL : X + Y + Z = ", pajak_daerah + pajak_federal + csr)


#main program
print("===========================================")
print("TUGAS BESAR MATRIKS DAN RUANG VEKTOR ")
print("===========================================")
print("Anggota Kelompok :")
print("1. Zeddhy Recca Fitracia (121140199) ")
print("2. Novita Rahmadhani (121140203) ")
print("3. Elika Eugenia Rahmadhani (121140212) ")
print("4. Muhammad Daffa Abiyyu Muhana (121140222)")
print("5. Fatur Arkan Syawalva (121140229)")
print("===========================================")

print("Pilihan Menu :")
print("1. Sistem persamaan linier")
print("2. Interpolasi Polinom")
print("3. Test Case Unik")
print("4. Keluar")
kode = int(input("Masukkan Kode(Angka saja): "))
print("===========================================")

if kode == 1:
  print("1. Input Manual")
  print("2. Input File")
  pilihan = int(input("Masukkan Kode(Angka saja): "))
  print("===========================================")
  if pilihan == 1:
    py_address = os.getcwd()
    print('Input Manual')
    print("")
    jum_baris = int(input('Masukan Jumlah Baris : '))
    jum_kolom = int(input('Masukan Jumlah Kolom  : '))
    print('')
    jum_kolom += 1
    arr = np.empty((jum_baris, jum_kolom))
    x = np.empty((jum_baris))
    for i in range(0, jum_baris):
      for j in range(0, jum_kolom):
        if j == jum_kolom - 1:
          arr[i, j] = input('matriks ' + '[' + str(i + 1) + ']' + '[' +
                            str(j + 1) + ']' + ': ')
        else:
          arr[i, j] = float(
            input('matriks ' + '[' + str(i + 1) + ']' + '[' + str(j + 1) +
                  ']' + ': '))
    print("")
    print('1. Gauss')
    print('2. Gauss Jordan')
    m = input('Inputkan pilihan anda : ')
    if m == '1':
      print('')
      print('Gauss : ')
      OutputMatriks(arr, jum_baris, jum_kolom)
      print('Setelah di OBE : ')
      gauss(arr, x, jum_baris, jum_kolom)
      OutputMatriks(arr, jum_baris, jum_kolom)
      penyelesaian(arr, x, jum_baris, jum_kolom)

    elif m == '2':
      print('')
      print('Gauss Jordan : ')
      OutputMatriks(arr, jum_baris, jum_kolom)
      print('Setelah di OBE : ')
      gaussjordan(arr, x, jum_baris, jum_kolom)
      OutputMatriks(arr, jum_baris, jum_kolom)
      penyelesaian(arr, x, jum_baris, jum_kolom)

    else:
      print("Menu salah")
    print('')
    print('Solusi :')
    SPL(arr, jum_baris, jum_kolom)
    copy_arr = np.copy(arr)
  elif pilihan == 2:
    print('Input File')
    print('')
    f = input("Masukkan Nama File : ")
    file = open(str(f) + ".txt", "r")
    cetak = file.readlines()

    jum_baris = int(cetak[0])
    jum_kolom = int(cetak[1]) + 1
    arr = np.empty((jum_baris, jum_kolom))
    x = np.empty((jum_baris))
    a = 2
    print("Jumlah Baris = " + str(jum_baris))
    print("Jumlah Kolom = " + str(jum_kolom - 1))
    for i in range(0, jum_baris):
      for j in range(0, jum_kolom):
        if j == 4 - 1:
          print('matriks ' + '[' + str(i + 1) + ']' + '[' + str(j + 1) + ']' +
                ': ' + str(cetak[a]))
          arr[i, j] = cetak[a]
          a += 1
        else:
          print('matriks ' + '[' + str(i + 1) + ']' + '[' + str(j + 1) + ']' +
                ': ' + str(cetak[a]))
          arr[i, j] = cetak[a]
          a += 1
    file.close()
    print("")
    print('1. Gauss')
    print('2. Gauss Jordan')

    m = input('Masukkan Pilihan(angka saja) : ')
    if m == '1':
      print('')
      print('Gauss : ')
      OutputMatriks(arr, jum_baris, jum_kolom)
      print('Setelah di OBE : ')
      gauss(arr, x, jum_baris, jum_kolom)
      OutputMatriks(arr, jum_baris, jum_kolom)
      penyelesaian(arr, x, jum_baris, jum_kolom)
    elif m == '2':
      print('')
      print('Gauss Jordan : ')
      OutputMatriks(arr, jum_baris, jum_kolom)
      print('Setelah di OBE : ')
      gaussjordan(arr, x, jum_baris, jum_kolom)
      OutputMatriks(arr, jum_baris, jum_kolom)
      penyelesaian(arr, x, jum_baris, jum_kolom)
    else:
      print("Menu salah")
      exit

    print('')
    print('Solusi :')
    SPL(arr, jum_baris, jum_kolom)
    copy_arr = np.copy(arr)

elif kode == 2:  #interpolasi polinom
  print("1. Input Manual")
  print("2. Input file")
  pilihan = int(input("Masukkan Kode(Angka saja): "))
  print("===========================================")
  if pilihan == 1:
    print("Interpolasi Linear")
    print("===========================================")
    interpolasi_linear()
  elif pilihan == 2:
    f = input("Masukkan Nama File : ")
    print("===========================================")
    file = open(str(f) + ".txt", "r")
    cetak = file.readlines()
    print('Masukkan jumlah data = ' + str(cetak[0]))
    n = int(cetak[0])
    x = []
    y = []

    for i in range(n):
      print(f"Nilai x{i} = " + str(cetak[i + 1]))
      x.append(float(cetak[i + 1]))
    print(" ")

    a = n
    for i in range(n):
      print(f"Nilai y{i} = " + str(cetak[a + 1]))
      y.append(float(cetak[a + 1]))
      a += 1

    print(f"Nilai f(x) yang ingin dicari, masukan nilai x = " + str(cetak[a + 1]))
    cari = float(cetak[a])
    i = 0
    for i in range(n):
      if cari <= x[i]:
        print(f"x{i},y{i} = ", x[i], ',', y[i])
        print(f"x{i-1},y{i-1} = ", x[i - 1], ',', y[i - 1])
        print('\n')
        hasil = ((y[i] - y[i - 1]) /
                 (x[i] - x[i - 1])) * (cari - x[i - 1]) + y[i - 1]
        print("f(x) = ", hasil)
        break

elif kode == 3:
  print("=== Test case Unik ==== ")
  print("1. Case D ")
  kode_case = int(input("Masukkan Kode(Angka saja): "))

  if kode_case == 1:
    print("Penyelesaian Case D")
    caseD()
  else:
    print("Menu Salah")
    exit

elif kode == 4:
  exit