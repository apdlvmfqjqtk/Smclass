let num = 0;
let num2 = 0;
//제이쿼리 선언
$(function () {

  //우측버튼
  $("#right").click(function () {
    // alert("우측버튼클릭");
    if(num >= 900) {
      alert("영역을 벗어났습니다.")
      return false;
    }
    $("#box").stop();
    num += 100;
    num2 += 360;
    $("#box").animate({
      left: num, rotate: num2 + "deg"
    }, 1000);

  }); // 우측버튼 끝



  //좌측버튼
  $("#left").click(function () {
    // alert("좌측버튼클릭");
    if(num <= 0) {
      alert("영역을 벗어났습니다.")
      return false;
    }
    $("#box").stop();
    num -= 100;
    num2 -= 360;
    $("#box").animate({
      left: num, rotate: num2 + "deg"
    }, 1000);



  }); // 좌측버튼 끝


}); //제이쿼리 선언 끝