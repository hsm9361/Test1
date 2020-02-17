//email 부분
$(document).ready(function(){
			$("select").on('change',function(){
				var email2 = $(this).val();
				if(email2=="직접"){
					$("#sp_email2").attr("readonly", false)
					$("#sp_email2").val('');
				}else{
				$("#sp_email2").attr("readonly", true)
				$("#sp_email2").val(email2);
				}
			});
			$("input:text[numberOnly]").on("keyup", function() {
            $(this).val($(this).val().replace(/[^0-9]/g,""));
            });
		});

// 주소 부분
function DaumPostcode() {
        new daum.Postcode({
            oncomplete: function(data) {
                // 팝업에서 검색결과 항목을 클릭했을때 실행할 코드를 작성하는 부분.

                // 각 주소의 노출 규칙에 따라 주소를 조합한다.
                // 내려오는 변수가 값이 없는 경우엔 공백('')값을 가지므로, 이를 참고하여 분기 한다.
                var addr = ''; // 주소 변수
                var extraAddr = ''; // 참고항목 변수

                //사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
                if (data.userSelectedType === 'R') { // 사용자가 도로명 주소를 선택했을 경우
                    addr = data.roadAddress;
                } else { // 사용자가 지번 주소를 선택했을 경우(J)
                    addr = data.jibunAddress;
                }

                // 사용자가 선택한 주소가 도로명 타입일때 참고항목을 조합한다.
                if(data.userSelectedType === 'R'){
                    // 법정동명이 있을 경우 추가한다. (법정리는 제외)
                    // 법정동의 경우 마지막 문자가 "동/로/가"로 끝난다.
                    if(data.bname !== '' && /[동|로|가]$/g.test(data.bname)){
                        extraAddr += data.bname;
                    }
                    // 건물명이 있고, 공동주택일 경우 추가한다.
                    if(data.buildingName !== '' && data.apartment === 'Y'){
                        extraAddr += (extraAddr !== '' ? ', ' + data.buildingName : data.buildingName);
                    }
                    // 표시할 참고항목이 있을 경우, 괄호까지 추가한 최종 문자열을 만든다.
                    if(extraAddr !== ''){
                        extraAddr = ' (' + extraAddr + ')';
                    }
                    // 조합된 참고항목을 해당 필드에 넣는다.
                    document.getElementById("sp_extraAddress").value = extraAddr;

                } else {
                    document.getElementById("sp_extraAddress").value = '';
                }

                // 우편번호와 주소 정보를 해당 필드에 넣는다.
                document.getElementById('sp_postcode').value = data.zonecode;
                document.getElementById("sp_address").value = addr;
                // 커서를 상세주소 필드로 이동한다.
                document.getElementById("sp_detailAddress").focus();
            }
        }).open();
    }

function validation(){

var sp_name=$("#sp_nm").val()
var sp_gender=$("#sp_gnr").val()
var sp_yy=$("#sp_birY").val()
var sp_mm=$("#sp_birM").val()
var sp_dd=$("#sp_birD").val()
var sp_email1=$("#sp_email1").val()
var sp_email2=$("#sp_email2").val()
var sp_phone=$("#sp_phone").val()
var sp_cgr=$("#sp_cgr").val()
var sp_month=$("#month").val()
var sp_rt=$("#sp_rt").val()
var sp_py=$("#sp_py").val()
var sp_num=$("#sp_num").val()
var sp_dpst=$("#sp_dpst").val()
var sp_bk=$("#sp_bk").val()
var sp_wd=$("#sp_wd").val()

if(sp_name.length==0){
    alert('이름을 입력해주세요')
    $("#sp_nm").focus()
    return false;
}

if(sp_gender.length==0){
    alert('성별을 입력해주세요')
    $("#sp_gnr").focus()
    return false;
}

if(sp_yy.length==0 || sp_mm.length==0 || sp_dd.length==0){
    alert('생년월일을 입력해주세요')
    $("#sp_birY").focus()
    return false;
}

if(sp_email1.length==0 || sp_email2.length==0){
    alert('이메일을 입력해주세요')
    $("#sp_email1").focus()
    return false;
}

if(sp_phone.length==0){
    alert('전화번호를 입력해주세요')
    $("#sp_phone").focus()
    return false;
}

if(sp_cgr.length==0){
    alert('후원종류를 선택해주세요')
    $("#sp_cgr").focus()
    return false;
}

if(sp_month.length==0){
    alert('기간을 선택해주세요')
    $("#month").focus()
    return false;
}

if(sp_rt.length==0){
    alert('후원방법을 선택해주세요')
    $("#sp_rt").focus()
    return false;
}

if(sp_py.length==0){
    alert('후원금액을 선택해주세요')
    $("#sp_py").focus()
    return false;
}

if(sp_num.length==0){
    alert('계좌번호를 입력해주세요')
    $("#sp_num").focus()
    return false;
}

if(sp_dpst.length==0){
    alert('예금주명을 입력해주세요')
    $("#sp_dpst").focus()
    return false;
}

if(sp_bk.length==0){
    alert('거래은행을 입력해주세요')
    $("#sp_bk").focus()
    return false;
}

if(sp_wd.length==0){
    alert('출금일을 선택해주세요')
    $("#sp_wd").focus()
    return false;
}


}