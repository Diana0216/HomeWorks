class MyXpaths():
  xpaths = {
      'smartphone': '//ul[@id="nav"]//a[@href="//allo.ua/ua/mobilnye-telefony-i-sredstva-svyazi/"]',
      'tv': '//ul[@id="nav"]//a[@href="//allo.ua/ua/televizory-i-mediapleery/"]',
      'earphones': '//ul[@id="nav"]//a[@href="//allo.ua/ua/naushniki-i-akustika/"]',
      'notebooks': '//ul[@id="nav"]//a[@href="//allo.ua/ua/planshety-i-gadzhety/"]',
      'apple': '//ul[@id="nav"]//a[@href="//allo.ua/ua/aksessuary-apple/"]',
      'xiaomi': '//ul[@id="nav"]//a[@ href="//allo.ua/ua/xiaomi-page/"]',
      'gadzhety': '//ul[@id="nav"]//a[@ href="//allo.ua/ua/gadzhety/"]',
      'bytovaya_tehnika': '//ul[@id="nav"]//a[@href="//allo.ua/ua/bytovaya-tehnika/"]',
      'sport': '//ul[@id="nav"]//a[@href="//allo.ua/ua/sport-i-zdorov-e/"]',
      'turizm': '//ul[@id="nav"]//a[@href="//allo.ua/ua/turizm-i-rybalka/"]',
      'santehnika': '//ul[@id="nav"]//a[@href="//allo.ua/ua/santehnika-i-remont/"]',
      'dom': '//ul[@id="nav"]//a[@href="//allo.ua/ua/dom-sad-remont/"]',
      'tovary_dlja_detej': '//ul[@id="nav"]//a[@href="//allo.ua/ua/tovary-dlja-detej/"]',
      'avtotovary': '//ul[@id="nav"]//a[@href="//allo.ua/ua/avtotovary/"]',
      'chasy_i_ukrashenija': '//ul[@id="nav"]//a[@href="//allo.ua/ua/chasy-i-ukrashenija/"]',
      'discounts': '//ul[@id="nav"]//a[@href="//allo.ua/ua/events-and-discounts/"]'

  }

  def test_smartphone(self):
      a = '//ul[@id="nav"]//a[@href="//allo.ua/ua/mobilnye-telefony-i-sredstva-svyazi/"]'
      assert self.xpaths.get('smartphone') == a, "Element  is  not found"


  def test_tv(self):
      b = '//ul[@id="nav"]//a[@href="//allo.ua/ua/televizory-i-mediapleery/"]'
      assert self.xpaths.get('tv') == b, "Element  not  found"


  def test_earphones(self):
      c = '//ul[@id="nav"]//a[@href="//allo.ua/ua/naushniki-i-akustika/"]'
      assert self.xpaths.get('earphones') == c, "Element  not  found"


  def test_notebooks(self):
      d = '//ul[@id="nav"]//a[@href="//allo.ua/ua/planshety-i-gadzhety/"]'
      if self.xpaths.get('notebooks') == d:
          print "Yours xpath is  correct"
      else:
          print "Yours xpath is  incorrect"


  def test_apple(self):
      e = '//ul[@id="nav"]//a[@href="//allo.ua/ua/aksessuary-apple/"]'
      if self.xpaths.get('apple') == e:
          print ("Yours xpath is  correct")
      else:
          print ("Yours xpath is incorrect")


  def test_xiaomi(self):
      f = '//ul[@id="nav"]//a[@ href="//allo.ua/ua/xiaomi-page/"]'
      if self.xpaths.get('xiaomi') == f:
          print("Yours xpath is correct")
      else:
          print("Yours xpath is incorrect")


  def test_gadzhety(self):
      g = '//ul[@id="nav"]//a[@ href="//allo.ua/ua/gadzhety/"]'
      if self.xpaths.get('gadzhety') == g:
          print("Yours xpath is correct")
      else:
          print("Yours xpath is incorrect")


  def test_bytovaya_tehnika(self):
      h = '//ul[@id="nav"]//a[@href="//allo.ua/ua/bytovaya-tehnika/"]'
      if self.xpaths.get('bytovaya_tehnika') == h:
          print("Your xpath is correct")
      else:
          print("Yours xpath is incorrect")


  def test_sport(self):
      j = '//ul[@id="nav"]//a[@href="//allo.ua/ua/sport-i-zdorov-e/"]'
      assert self.xpaths.get('sport') == j, "Element  not  found"


  def test_turizm(self):
      k = '//ul[@id="nav"]//a[@href="//allo.ua/ua/turizm-i-rybalka/"]'
      assert self.xpaths.get('turizm') == k, "Element  not  found"


  def test_santehnika(self):
      L = '//ul[@id="nav"]//a[@href="//allo.ua/ua/santehnika-i-remont/"]'
      assert self.xpaths.get('santehnika') == L, "Element  not  found"


  def test_dom(self):
      j = '//ul[@id="nav"]//a[@href="//allo.ua/ua/dom-sad-remont/"]'
      if self.xpaths.get('dom') == j:
          print("Your xpath is correct")
      else:
          print("Yours xpath is incorrect")


  def test_tovary_dlja_detej(self):
      p = '//ul[@id="nav"]//a[@href="//allo.ua/ua/tovary-dlja-detej/"]'
      assert self.xpaths.get('tovary_dlja_detej') == p, "Element  not  found"


  def test_avtotovary(self):
      o = '//ul[@id="nav"]//a[@href="//allo.ua/ua/avtotovary/"]'
      if self.xpaths.get( 'avtotovary') == o:
          print("Your xpath is correct")
      else:
          print("Yours xpath is incorrect")


  def test_chasy_i_ukrashenija(self):
      m = '//ul[@id="nav"]//a[@href="//allo.ua/ua/chasy-i-ukrashenija/"]'
      if self.xpaths.get('chasy_i_ukrashenija') == m:
          print("Your xpath is correct")
      else:
          print("Yours xpath is incorrect")


  def test_discounts(self):
      t = '//ul[@id="nav"]//a[@href="//allo.ua/ua/events-and-discounts/"]'
      if self.xpaths.get('discounts') == t:
          print("Your xpath is correct")
      else:
          print("Yours xpath is incorrect")


test = MyXpaths()
test.test_smartphone()
test.test_tv()
test.test_earphones()
test.test_notebooks()
test.test_apple()
test.test_xiaomi()
test.test_gadzhety()
test.test_bytovaya_tehnika()
test.test_sport()
test.test_turizm()
test.test_santehnika()
test.test_dom()
test.test_tovary_dlja_detej()
test.test_avtotovary()
test.test_chasy_i_ukrashenija()
test.test_discounts()

