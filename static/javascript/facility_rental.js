//email 부분
$(document).ready(function(){
			$("select").on('change',function(){
				var email2 = $(this).val();
				if(email2=="직접"){
					$("#rn_email2").attr("readonly", false)
					$("#rn_email2").val('');
				}else{
				$("#rn_email2").attr("readonly", true)
				$("#rn_email2").val(email2);
				}
			});
		});



//달력관련 부분
		$(function() {
		$.datepicker.setDefaults({
                dateFormat: 'yy-mm-dd' //Input Display Format 변경
                ,showOtherMonths: true //빈 공간에 현재월의 앞뒤월의 날짜를 표시
                ,showMonthAfterYear:true //년도 먼저 나오고, 뒤에 월 표시
                ,yearSuffix: "년" //달력의 년도 부분 뒤에 붙는 텍스트,dayNamesMin: ['일','월','화','수','목','금','토'] //달력의 요일 부분 텍스트
                ,monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'] //달력의 월 부분 Tooltip 텍스트
                ,dayNames: ['일요일','월요일','화요일','수요일','목요일','금요일','토요일'] //달력의 요일 부분 Tooltip 텍스트
                ,minDate: "0" //최소 선택일자(-1D:하루전, -1M:한달전, -1Y:일년전)
                ,maxDate: "+6D" //최대 선택일자(+1D:하루후, -1M:한달후, -1Y:일년후)
            });
    $( "#testDatepicker").datepicker();
    var date = new Date();

    $( "#testDatepicker").val(date.yyyymmdd())
		});

		Date.prototype.yyyymmdd = function() {
      var yyyy = this.getFullYear().toString();
      var mm = (this.getMonth() + 1).toString();
      var dd = this.getDate().toString();
      return  yyyy + "-" + (mm[1] ? mm : "0" + mm[0]) + "-" + (dd[1] ? dd : "0" + dd[0]);
  };

function inputPhoneNumber(obj) {
    var number = obj.value.replace(/[^0-9]/g, "");
    var phone = "";

    if(number.length < 4) {
        return number;
    } else if(number.length < 7) {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3);
    } else if(number.length < 11) {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3, 3);
        phone += "-";
        phone += number.substr(6);
    } else {
        phone += number.substr(0, 3);
        phone += "-";
        phone += number.substr(3, 4);
        phone += "-";
        phone += number.substr(7);
    }
    obj.value = phone;
};

function check(){
//지금 쓰여있는 날짜의 값을 받아오는 부분
var day=$( "#testDatepicker").val();

//라디오버튼중 선택되어 있는부분의 값을 받아오는부분
var facility = $('input[name="rn_cgr"]:checked').val();

$.ajax({
                url : 'facility_reservation_check/'+day+'/'+facility,
                type : 'post',
                dataType : 'json',
                success : function(time){
                    //alert(time.length)
//                    alert(time[0])
                    var array = ['09:00~10:00', '10:00~11:00', '11:00~12:00',
'12:00~13:00','13:00~14:00', '14:00~15:00',
'15:00~16:00', '16:00~17:00', '17:00~18:00']

                    if(time.length==0){
                    $('input[name="h_time"]').removeAttr("disabled")
                    for(var i=0; i<9; i++) {
                    var text=array[i]
                    $('input[name="h_time"][value='+(i+1)+']').next().html(text);
                    $('input[name="h_time"][value='+(i+1)+']').next().removeAttr("style");
                    }
                    }
                    if (time.length>0){
                    for(var i=0; i<time.length; i++) {
//                    alert(time[i])
                    $('input[name="h_time"][value='+time[i]+']').attr("disabled", 'disabled');
                    $('input[name="h_time"][value='+time[i]+']').next().html('예약불가');
                    $('input[name="h_time"][value='+time[i]+']').next().attr("style", 'color:red');
                    }


                    }
                }
            })
}