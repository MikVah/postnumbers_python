import postinumerot

TOIMIPAIKAT = {
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}

def test_ryhmittele_kiuruvesi():
    tulos = postinumerot.toimipaikat['KIURUVESI']
    assert tulos == ['74701', '74700']

def test_kiuruvesi_pituus():
    tulos = len(postinumerot.toimipaikat['KIURUVESI'])
    assert tulos == 2

def test_juupajoki():
    tulos = postinumerot.postinumerot['35540']
    assert tulos == 'JUUPAJOKI'

# def test_oma_data_muuruvesi(mocker):
#    oma_data = TOIMIPAIKAT
#    mocker.patch('http_request.hae_postinumerot', return_value=oma_data)
#    tulos = postinumerot.postinumerot['73460']
#    assert tulos == 'MUURUVESI'
