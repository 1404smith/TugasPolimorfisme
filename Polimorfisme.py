class FakultasTeknik(object):
  def __init__(self, U, F, T):
      self.univ = U
      self.fak = F
      self.TA = T
  def CetakData(self):
      print('Universitas  :',self.univ)
      print('Fakultas :',self.fak)
      print('Tahun Ajaran :',self.TA)
class TeknikKomputer(FakultasTeknik):
  def __init__(self, U, F, T, JumlahAngkatan):
    self.JA= JumlahAngkatan
    FakultasTeknik.__init__(self, U, F, T)
  def CetakData(self):
      print(30 * '=')
      print('Teknik Komputer')
      print('Universitas  :',self.univ)
      print('Fakultas :',self.fak)
      print('Tahun Ajaran :',self.TA)
      print('Jumlah Angkatan :',self.JA)
      print(30 * '=')
class PTIK(FakultasTeknik):
    def __init__(self, U, F, T, JumlahAngkatan, Jurusan):
      self.JA = JurusanAngkatan
      self.J = Jurusan
      FakultasTeknik.__init__(self, U, F, T)
      def CetakData(self):
 
      print('Pendidikan Teknik Informatika dan Komputer')
      print('Universitas  :',self.univ)
      print('Fakultas :',self.fak)
      print('Jurusan : '.self.J)
      print('Tahun Ajaran :',self.TA)
      print('Jumlah Angkatan :',self.JA)
      print(30 * '=')
class Mekatronika(FakultasTeknik):
def __init__(self, U, F, T, JumlahAngkatan):
    self.JA= JumlahAngkatan
    FakultasTeknik.__init__(self, U, F, T)
  def CetakData(self):
 
      print('Mekatronika')
      print('Universitas  :',self.univ)
      print('Fakultas :',self.fak)
      print('Tahun Ajaran :',self.TA)
      print('Jumlah Angkatan :',self.JA)
      print(30 * '=')
      
def main():

  a = FakultasTeknik('UNM', ' Teknik', 2018)
  a.CetakData()
  
  a = TeknikKomputer('UNM', ' Teknik', 2018, 2)
  a.CetakData()
  
  b = PTIK('UNM', ' Teknik', 2018, 10, ' Pendidikan Teknik Informatika dan Komputer')
  b.CetakData()
  
  del b
  
  b = Mekatronika('UNM', ' Teknik', 2018,2)
  b.CetakData()
  
if __name__ == "__main__"
  main()
