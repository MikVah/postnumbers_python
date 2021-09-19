import postinumerot

TOIMIPAIKAT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

ERIKOISTAPAUKSET = {
    "43800": "KIVIJÄRVI",
    "91150": "YLI-OLHAVA",
    "65374": "SMART POST",
    "90210": "BEVERLY HILLS"
}

def test_postinumerot_ei_tyhja():
    assert len(postinumerot.postinumerot) > 0

def test_nahkela_loytyy():
    assert postinumerot.postinumerot['04350'] == 'NAHKELA'

def test_korvatunturi_postinumero():
    tulos = postinumerot.postinumerot['99999']
    assert tulos == 'KORVATUNTURI'

#def test_postinumerot_oma_data(mocker):
 #   oma_data = ERIKOISTAPAUKSET
  #  mocker.patch('http_request.hae_postinumerot', return_value=oma_data)
   # tulos = postinumerot.postinumerot['90210']

    # assert tulos == 'BEVERLY HILLS'