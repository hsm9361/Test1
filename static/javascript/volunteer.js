
	// 우편번호 API활용방법
	//참고사이트 URL : http://ktsmemo.cafe24.com/s/dev/314
		function openZipSearch() {
	new daum.Postcode({
		oncomplete: function(data) {
			$('[name=zip]').val(data.zonecode); // 우편번호 (5자리)
			$('[name=vn_zp]').val(data.address);
			$('[name=vn_addr]').val(data.buildingName);
		}
	}).open();
};
	// 정기적 비정기적 활성화 처리하는 부분
		$(document).ready(function(){

    // 라디오버튼 클릭시 이벤트 발생
    $("input:radio[name=vn_rc]").click(function(){
        if($("input[name=vn_rc]:checked").val() == "2"){
            $("input:text[name=vn_rc_etc]").attr("disabled",false);
            // radio 버튼의 value 값이 1이라면 활성화

        }else if($("input[name=vn_rc]:checked").val() == "1"){
              $("input:text[name=vn_rc_etc]").attr("disabled",true);
            // radio 버튼의 value 값이 0이라면 비활성화
        }
    });
});
