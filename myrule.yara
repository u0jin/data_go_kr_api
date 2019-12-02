rule korea_public_api0
{
	meta:
		description = "도로명주소 우편번호 조회서비스"
	strings:
		$apikey0 = /"http:\/\/openapi.epost.go.kr:80\/postal\/retrieveNewAdressAreaCdService\?_wadl&type=xml"/
		$apikey1 = /[0-9A-Za-z%]{90,100}/

	condition:
		$apikey0 and $apikey1
}
rule korea_public_api1
{
	meta:
		description = "(신)동네예보정보조회서비스"
	strings:
		$apikey0 = /"http:\/\/newsky2.kma.go.kr\/service\/SecndSrtpdFrcstInfoService2"/
		$apikey1 = /[0-9A-Za-z%]{90,100}/

	condition:
		$apikey0 and $apikey1
}
